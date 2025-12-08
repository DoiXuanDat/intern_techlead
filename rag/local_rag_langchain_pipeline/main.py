import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM  

def load_faiss_index(index_path, embedding_model):
    embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
    vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    return vector_store

def create_rag_system(index_path, embedding_model='sentence-transformers/all-MiniLM-L6-v2', model_name='qwen3:1.7b'):
    vector_store = load_faiss_index(index_path=index_path, embedding_model=embedding_model)
    retriever = vector_store.as_retriever()
    llm = OllamaLLM(model=model_name, base_url="http://localhost:11434")

    prompt_template = '''
        You are an expert assistant with access to the following context extracted from documents. 
        Your job is to answer the user question as accurately as possible, using the context below.
        Context:
        {context}
        Given this information, please provide a comprehensive
        and relevant answer to the following question:
        Question: {question}
        If the context does not contain enough information,
        clearly state that the information is not
        available in the context provided.
        If possible, provide a step-by-step explanation and highlight key details.
    '''

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])


    rag_chain = (
        {
        'context': RunnableLambda(lambda x: x['question']) | retriever,
        'question': RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain                       

def get_answer(question, rag_chain):
    return rag_chain.invoke({"question": question})

if __name__ == '__main__':
    index_path = 'DataIndex'
    rag_system = create_rag_system(index_path)

    while True:
        user_questions = input('Câu hỏi (nhấn exit để thoát):').strip()
        if user_questions == 'exit':
            break

        answer = get_answer(user_questions, rag_system)
        print(f'Answer: {answer}')
    
