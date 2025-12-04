# Array trong Python

Array là một vùng chứa có thể lưu trữ một số lượng mục cố định và các mục này phải cùng kiểu dữ liệu. Mỗi mục được lưu trữ trong một mảng được gọi là một element và chúng có thể thuộc bất kỳ kiểu dữ liệu nào, bao gồm số nguyên, số thực, chuỗi,... Không như các ngôn ngữ như C, C++, Java. Array trong Python không hỗ trợ tích hợp sẵn, tuy nhiên ta có một loạt các loại data types hỗ trợ mạnh hơn khác là List, tuple thường được sử dụng như array nhưng, các mục được lưu trữ trong các loại chuỗi này không nhất thiết phải cùng kiểu. 

- Truy cập các phần tử trong mảng

Ta truy cập một phần tử trong mảng bằng cách sử dụng index 

    cars = ['red','blue','green']

    x = cars[0] -> x = red

- The Length of an Array

Sử dụng phương thức len() để trả lại độ dài của chuỗi

    x = len(cars) -> x = 3

- Looping Array Elements

Sử for in để lặp qua tất cả các phần từ của một mảng

    for x in cars:
        print(x) 

- Adding Array Elements

Sử dụng append() để thêm phần tử vàng trong mảng 

    cars.append('yellow')

- Removing Array Elements

Sử dụng pop() hoặc remove() để xóa một phần tử ở trong mảng 

    cars.pop('red')
