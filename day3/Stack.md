# Stacks

Stack là một cấu trúc dữ liệu tuyến tính tuân theo quy tắc Last-In-First-Out. Các thao tác cơ bản ta có thể thực hiện với stack là:

- Push: Thêm một phần tử mới vào stack
- Pop: Xóa và trả về phần tử trên cùng của stack 
- Peek: Trả về phần tử cuối cùng của stack 
- isEmpty: Xem stack liệu có rỗng không
- Size: Trả về số lượng elements trong stack

    stack = []

    #Push
    stack.append('A')
    stack.append('B')
    stack.append('C')
    print("Stack: ", stack)

    #Peek
    topElement = stack[-1]
    print("Peek: ", topElement)

    #Pop
    poppedElement = stack.pop()
    print("Pop: ", poppedElement)

    #isEmpty
    isEmpty = not bool(stack)
    print("isEmpty: ", isEmpty)

    #Size
    print("Size: ",len(stack))
