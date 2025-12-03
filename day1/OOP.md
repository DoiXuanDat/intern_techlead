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

# 2. Tính kế thừa (Inheritance)

Nó cho phép một class con có thể truy cập các thuộc tính cũng như các phương thức của các class cha khác. Mục đích chính là phân cấp cũng như tăng tính tái sử dụng code

Các loại kế thừa gồm có:
    
- kế thừa đơn (Single Inheritance): Một lớp con kế thừa từ một lớp cha duy nhất
- kế thừa đa (Multiple Inheritance): Một lớp con kế thừa từ nhiều hơn một lớp cha
- kế thừa bậc thang (Multilevel Inheritance): Một lớp con kế thừa từ một lớp cha, và lớp cha này lại kế thừa từ một lớp khác
- kế thừa phân cấp (Hierarchical Inheritance): Nhiều lớp con cùng kế thừa từ một lớp cha duy nhất
- kế thừa lai (Hybrid Inheritance): Là sự kết hợp của hai hoặc nhiều loại hình kế thừa kể trên

Ta quay lại với class nhân ciên ở mục trên 

    class Employee:
    def __init__(self, first_name, last_name, salary, dept=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f"{first_name}.{last_name}@company.com"
        self.salary = salary
        self.dept = dept

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

Tính kế thừa đơn được thể hiện như sau. Giải sử ta tạo lớp quản lý cũng là nhân viên nhưng vẫn có thêm danh sách nhân viên cấp dưới. 

    class Manager(Employee):
        def __init__(self, first_name, last_name, salary, dept, team):
            super().__init__(first_name, last_name, salary, dept)
            self.team = team

        def manage(self):
            return f"{self.full_name()} manages {len(self.team)} people in {self.dept}"

Ở đây class Manager(Employee) là phần khai báo quan hệ cha-con. Hàm super() được sử dụng để gọi phương thức từ class cha, giúp ta đỡ phải đi gán lại các thuộc tính ta đã gán lại ở class cha

Tính kế thừa đa được thể hiện như sau. Ta tạo một class Salari_Calculation chưa logic tính lương và tạo thêm một class nữa tên là Accountant. 

    class Salari_Calculation:
        def calculate_pay(self, salary, tax):
            pay = salary * (1 - tax)
            return pay

    class Accountant(Employee, Salari_Calculation):
        def __init__(self, full_name, salary, tax=0.1):
            super().__init__(full_name, salary)
            self.tax = tax
        
        def pay_summary(self):
            final_pay = self.calculate_pay(self.salary, self.tax)
            return f"{self.full_name} has completed the calculation. Net pay (after {self.tax*100}% tax): ${final_pay}"

Ta đẽ dang nhận ra class Accountant lấy cả thông tin từ class nhân viên và khả năng tính toán từ class Salari_Calculation.

Tính kế thừa bậc thang thể hiện như sau. Giả sử ta có lớp giám đốc là cấp trên của quản lý ta có chuỗi kế thừa Employee -> Manager -> Director

    class Director(Manager): 
        def approve_budget(self, amount):
            return f"{self.full_name()} approved a budget of ${amount}"

Do kế thừa Director() kế thừa từ Manager cho nên giám đốc kế thừa toàn bộ thuộc tính và phương thức của nhân viên và team và manage() từ manager

Tính kế thừa phân cấp là khi có nhiều lớp con ví dụ như Director, Accountant, Manager ké thừa cùng từ một lớp cha (Employee)

    class Employee:
        def __init__(self, full_name, salary):
            self.full_name = full_name
            self.salary = salary
    
    def work_report(self):
        print(f"Reported: {self.full_name} still in working")


    class Manager(Employee):
        def work_report(self):
            print(f"Reported: {self.full_name} supervise employee A")


    class Accountant(Employee):
        def calculate_tax(self):
            tax = self.salary * 0.1
            print(f"Reported: {self.full_name} calculated ${tax}.")


# 3. Tính Đa hình 

Đa hình trong đây có thể hiểu là cùng một thao tác, hành vi khác nhau. Nó cho phép các hàm hoặc các phương thức có cùng tên hoạt động khác nhau tùy thuộc thei kiểu đối tượng mà chúng tác động lên. Ví dụ như cùng một hành động là work() nhưng Employee có thể đang viết báo cáo, Manager lại là giám sát, Accountant lại là đang tính toán lương, thuế. Có 2 loại đa hình là đa hình tại thời điểm biên dịch (Compile-Time Polymorphism) và đa hình tại thời điểm chạy.

1. đa hình tại thời điểm biên dịch:
  


