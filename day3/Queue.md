# Queue 

Queue là một cấu trúc dữ liệu tuyến tính tuân theo quy tắc First-In-First-Out, Các thao tác cơ bản ta có thể thực hiện với Queue là: 

- Enqueue: Thêm phần tử mới vào Queue
- Dequeue: Xóa và trar lại phần tử đầu của Queue
- Peek: Trả lại phần tử đầu của Queue
- isEmpty: Chekc xem liệu Queue có rỗng 
- Size: Trả về số lượng elements trong Queue

    queue = []

    #Enqueue
    queue.append('A')
    queue.append('B')
    queue.append('C')
    print("Queue: ", queue)

    #Peek
    frontElement = queue[0]
    print("Peek: ", frontElement)

    #Dequeue
    poppedElement = queue.pop(0)
    print("Dequeue: ", poppedElement)

    #isEmpty
    isEmpty = not bool(queue)
    print("isEmpty: ", isEmpty)

    #Size
    print("Size: ", len(queue))