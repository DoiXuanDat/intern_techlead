# Linked Lists

Linked Lists là một cấu trúc dữ liệu tuyến tính, trong đó các phần tử (nút) không cần phải nằm ở các vị trí bộ nhớ liền kề. Thay vào đó, chúng được kết nối bằng các con trỏ để tạo thành một chuỗi. Một danh sách liên kết bao gồm các nút chứa một loại dữ liệu nào đó, và một con trỏ, hoặc liên kết, trỏ đến nút kế tiếp. Một lợi ích lớn khi sử dụng danh sách liên kết là các nút được lưu trữ ở bất cứ nơi nào có không gian trống trong bộ nhớ, các nút không cần phải được lưu trữ liền kề ngay sau nhau như cách các phần tử được lưu trữ trong array

Có 3 loại Linked Lists

- Singly linked lists 
- Doubly linked lists
- Circular linked lists

Những thao tác ta có thể làm với link list là duyệt, xóa một node, chèn một node, sắp xếp

- Duyệt 

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


    node1 = Node(7)
    node2 = Node(11)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    node4.next = node5
    print(Traversal(node1))


- Xóa một node

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

    def deleteSpecificNode(head, nodeToDelete):
        if head == nodeToDelete:
            return head.next

        currentNode = head
        while currentNode.next and currentNode.next != nodeToDelete:
            currentNode = currentNode.next

            if currentNode.next is None:
                return head

            currentNode.next = currentNode.next.next

        return head

    node1 = Node(7)
    node2 = Node(11)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print("Trước khi xóa:")
    traverseAndPrint(node1)

    node1 = deleteSpecificNode(node1, node4)

    print("Sau khi xóa:")
    traverseAndPrint(node1)

- Chèn một node 

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

    def insertNodeAtPosition(head, newNode, position):
        if position == 1:
            newNode.next = head
            return newNode

        currentNode = head
        for _ in range(position - 2):
            if currentNode is None:
            break
            currentNode = currentNode.next

        newNode.next = currentNode.next
        currentNode.next = newNode
        return head

    node1 = Node(7)
    node2 = Node(3)
    node3 = Node(2)
    node4 = Node(9)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("Truớc khi chèn:")
    traverseAndPrint(node1)

    newNode = Node(97)
    node1 = insertNodeAtPosition(node1, newNode, 2)

    print("Sau khi chèn:")
    traverseAndPrint(node1)

- sắp xếp 

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