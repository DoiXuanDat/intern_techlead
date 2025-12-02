# 1. Class 
Câu hỏi đầu tiên là tại sao ta phải dùng class?

Không chỉ riêng một mình python. Class hiện diện trong toàn bộ các ngôn ngữ lập trình ngày nay. Nó giúp chúng ta gộp dữ liệu và các chức năng lại một cách logic và dễ dàng maintain

Để nói về điểm khác biệt về class và Instance. Giả sử ta muốn tạo ứng dụng quản lý nhân viên cho một công ty, mỗi nhân viên sẽ có tên, địa chỉ mail và mức lương. 

Đầu tiên ta tạo class nhân viên 

    class Employee(): 
        pass

    employee_1 = Employee()
    employee_2 = Employee()

    employee_1.first_name = 'Van'
    employee_1.last_name = 'A'
    employee_1.email = 'VanA@techlead.com'
    employee_1.salary = 100000

    employee_2.first_name = 'Van'
    employee_2.last_name = 'B'
    employee_2.email = 'VanB@techlead.com'
    employee_2.salary = 2000000

Nhưng nếu có rất nhiều nhân viên thì sao, ta lại phải tạo chay từ đầu đến cuối? -> code nó sẽ dài, rất dễ bị sai đặc biệt khi ta để tên sai. 

Để setup tự động tạo, ta sử phương thức __init__. Đây gọi là hàm khởi tạo. 
    
    class Employee(): 
        
        def __init__(self, first_name, last_name, salary):
            self.first_name = first_name
            self.last_name = last_name
            self.email = first_name + '.' + last_name + '@techlead.com'
            self.salary = salary

Vậy từ đây ta chỉ cần thêm thông tin tương ứng vào mỗi nhân viên ta tạo 

    employee_1.Employee('Van','A','VanA@techlead.com', 1000000)
    employee_2.Employee('Van','B','VanB@techlead.com', 2000000)

Trong class ta có thể tạo ra nhiều phương thức khác nhau ví dụ để hiện thị toàn bộ tên của nhân viên

        def fullname(self):
            return '{} {}'.format(self.first_name, self.last_name)

# 
