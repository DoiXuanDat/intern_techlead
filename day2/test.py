class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def sortLinkedList(head):
    current = head
    index = None

    if head is None:
        return
    
    while current is not None:
        index = current.next
        
        while index is not None:
            if current.data > index.data:
                temp = current.data
                current.data = index.data
                index.data = temp
            
            index = index.next
        current = current.next

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Trước khi sắp xếp:")
traverseAndPrint(node1)

sortLinkedList(node1)

print("Sau khi sắp xếp:")
traverseAndPrint(node1)