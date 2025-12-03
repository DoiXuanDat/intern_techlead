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

    employee_1 = Employee('Van', 'A', 1000000)
    employee_2 = Employee('Van', 'B', 2000000)

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
            self.email = f"{first_name}.{last_name}@techlead.com"
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

Tính kế thừa đa được thể hiện như sau. Ta tạo một class Salary_Calculation chưa logic tính lương và tạo thêm một class nữa tên là Accountant. 

    class Salary_Calculation:
        def calculate_pay(self, salary, tax):
            pay = salary * (1 - tax)
            return pay

    class Accountant(Employee, Salary_Calculation):
        def __init__(self, full_name, salary, tax=0.1):
            super().__init__(full_name, salary)
            self.tax = tax
        
        def pay_summary(self):
            final_pay = self.calculate_pay(self.salary, self.tax)
            return f"{self.full_name()} has completed the calculation. Net pay (after {self.tax*100}% tax): ${final_pay}"

Ta đẽ dang nhận ra class Accountant lấy cả thông tin từ class nhân viên và khả năng tính toán từ class Salary_Calculation.

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


# 3. Tính Đa hình (Polymorphism)

Đa hình trong đây có thể hiểu là cùng một thao tác, hành vi khác nhau. Nó cho phép các hàm hoặc các phương thức có cùng tên hoạt động khác nhau tùy thuộc thei kiểu đối tượng mà chúng tác động lên. Ví dụ như cùng một hành động là work() nhưng Employee có thể đang viết báo cáo, Manager lại là giám sát, Accountant lại là đang tính toán lương, thuế. Có 2 loại đa hình là đa hình tại thời điểm biên dịch (Compile-Time Polymorphism) và đa hình tại thời điểm chạy.

1. đa hình tại thời điểm biên dịch:
  
Là một loại biên dịch được xác định trong quá trình biên dịch trương trình. Nó cho phép các phương thức hoặc toán tử có cùng tên thực tên các hành vi khác nhau dựa trên các input hoặc cách sử dụng của chúng

    class Employee:
        
        def work(self):
            return f"{self.full_name()} ({self.dept}) is writing a general report."

    class Manager(Employee):

        
        def work(self):  
            return f"{self.full_name()} ({self.dept}) is supervising {len(self.team)} employees."

    class Accountant(Employee, Salary_Calculation):

        def work(self):  
            tax = self.salary * 0.1
            return f"{self.full_name()} ({self.dept}) is calculating payroll and tax (${tax})."

Nhưng trong python việc đa hình tại thời điểm biên dịch không được hỗ trợ, thay vào đó python mô phỏng bằng cách sử dụng các tham số mặc địch hoặc sử dụng *args/**kwargs. 

    def pay_summary(employee, bonus=None):
        if bonus is None:
            return f"{employee.full_name()} base pay: ${employee.salary}"
        if isinstance(bonus, (int, float)):
            return f"{employee.full_name()} pay + bonus: ${employee.salary + bonus}"
        if isinstance(bonus, (list, tuple)):
            return f"{employee.full_name()} pay + bonuses: ${employee.salary + sum(bonus)}"
        return f"{employee.full_name()} pay: ${employee.salary}"

Ta gán một giá trị là None hoặc 0 cho một tham số ngay trong định nghĩa hàm. nếu không truyền giá trị cho tham số đó khi gọi hàm sẽ tự động dùng giá trị mặc định 

    class Manager(Employee):
        def __init__(self, first, last, salary, dept=None, team=None):
            super().__init__(first, last, salary, dept)
            self.team = team or []

        def work(self, *tasks, urgent=False, **context):
            if not tasks:
                return f"{self.full_name()} ({self.dept}) supervises the team."
            tasks_str = ", ".join(tasks)
            urgent_tag = " [URGENT]" if urgent else ""
            extra = " | ".join(f"{k}={v}" for k, v in context.items())
            return f"{self.full_name()} will: {tasks_str}{urgent_tag}" + (f" ({extra})" if extra else "")
    
Đây là cơ chế mạnh mẽ hơn, cho phép hàm chấp nhận số lượng đối số bất kỳ mà không cần phải liệt kê hết trong định nghĩa hàm. *args là thu thập tất cả các đối số vị trí (positional arguments) không khớp với các tham số đã đặt tên khác, và đóng gói chúng thành một tuple. **kwargs Thu thập tất cả các đối số từ khóa (keyword arguments) không khớp với các tham số đã đặt tên khác, và đóng gói chúng thành một dictionary. 

2. Đa hình tại thời điểm chạy

Đa hình tại thời điểm chạy được xác định trong quá trình thực thi chương trình. Nó bao gồm nhiều hình thức trong Python
- Ghi đè phương thức (Method Overriding): một lớp con định nghĩa một phương thức từ lớp cha của nó 

    class Employee:
        def __init__(self, name, salary, dept=None):
            self.name = name 
            self.salary = salary 
            self.dept = dept

        def work(self): 
            return f"{self.name} ({self.dept}) writes a general report."

    class Manager(Employee):
        def __init__(self, name, salary, dept=None, team=None):
            super().__init__(name, salary, dept) 
            self.team = team or []
        def work(self): 
            return f"{self.name} ({self.dept}) supervises {len(self.team)} employees."

    people = [Employee("Van A",100000,"Dev"), Manager("Van B",150000,"Finance",team=["A","B"])]
    for p in people: print(p.work())

- Duck Typing (Duck Typing): Nếu một đối tượng thực hiện phương thức được yêu cầu, thì nó sẽ hoạt động bất kể kiểu của nó là gì

    def perform_learning(person):
        return person.provide_learning()

    class Mentor:
        def __init__(self, name):
            self.name = name
        def provide_learning(self):
            return f"{self.name} (mentor) runs a major upskilling session."

- Tải chồng toán tử (Operator Overloading): Các phương thức đặc biệt như __add__, __sub__,..., định nghĩa lại cách các toán tử hoạt động đối với các đối tượng do ta định nghĩa 

    from abc import ABC, abstractmethod

    class Employee:
        def __init__(self, full_name, salary):
            self.full_name = full_name
            self.salary = salary
        def __repr__(self): 
            return f"{self.full_name()}(${self.salary})"
        def __add__(self, other):
            if isinstance(other, Employee): 
                return Team([self, other])
            if isinstance(other, Team): 
                return Team([self] + other.members)
            return NotImplemented

    class Team:
        def __init__(self, members=None):
            self.members = members or []
        def __repr__(self):
            return "Team(" + ", ".join(repr(m) for m in self.members) + ")"

# 4. Tính đóng gói (Encapsulation)

Là việc gom nhóm thuộc tính và các phương thức vào bên trong một lớp, đồng thời hạn chế quyền truy cập vào một số thành phần để kiểm soát cách chúng được sử dụng hoặc tương tác. Một class là ví dụ điển hình của tính đóng gói, vì nó bao bọc toàn bộ dữ liệu gồm các biến, phương thức trong một cấu trúc thống nhất.

Các kiểu đóng gói:

- Public: Truy cập được từ bất cứ đâu

    class Employee:
        def __init__(self, full_name):
            self.full_name = full_name

    name = Employee("A")
    print(name.full_name)

- Protected: Chỉ được truy cập trong class của nó và các class kế thừa 

    class Employee:
        def __init__(self, full_name, salary):
            self._salary = salary 

    class Manager(Employee):
        def show_salary(self):
            return f"Manager salary: {self._salary}"

    manager = Manager("A", 1000000)
    print(manager._salary)

- Private: chỉ có thể truy cập bên trong chính class đó  

    class Employee:
        def __init__(self, name, salary):
            self.__salary = salary

        def get_salary(self):
            return self.__salary

    employee = Employee("B", 2000000)
    print(employee.get_salary())  # Hợp lệ
    print(employee.__salary)      # Lỗi AttributeError 


# 5. Tính trừu tượng (Abstraction)

Là việc che giấu các chi tiết cài đặt nội bộ và chỉ lộ ra những chức năng cần thiết. Nó giúp ta tập trung vào “làm gì” thay vì “làm như thế nào”

Các Loại trùy tượng:
- Trừu tượng hóa một phần: class trừu tượng chứa cả phương thức trừu tượng và phương thức thường 

    class Employee(ABC):
        def __init__(self, first_name, last_name, salary, dept=None):
            self.first_name = first_name
            self.last_name = last_name
            self.salary = salary
            self.dept = dept

        def full_name(self): -> phương thức thường
            return f"{self.first_name} {self.last_name}"

        @abstractmethod -> phương thức trừu tượng
        def work(self):
            pass

    class Manager(Employee):
        def work(self):
            return f"{self.full_name()} ({self.dept}) supervises the team."

    class Accountant(Employee):
        def work(self):
            tax = self.salary * 0.1
            return f"{self.full_name()} ({self.dept}) calculated pay. Tax=${tax}"


- Trừu tượng toàn phần: class chứa toàn bộ phương thức trừu tượng

    from abc import ABC, abstractmethod

    class Employee(ABC):
        
        def __init__(self, full_name, salary):
            self.full_name = full_name
            self.salary = salary

        @abstractmethod
        def work(self):
            pass

        @abstractmethod
        def bonus_salary(self):
            pass

    class Developer(Employee):
        def work(self):
            return f"{self.full_name} debugging"

        def bonus_salary(self):
            return self.salary * 1.15  

    class Test(Employee):
        def work(self):
            return f"{self.full_name} tesing"

        def bonus_salary(self):
            return self.salary * 1.05 


# 6. SOLID

Nó là viết tắt của 5 quy tắc: Single Responsibility Principle, Open/Closed Principle, Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle. đó là bộ 5 quy tắc thiết kế hướng đối thượng tập trung vào việc tạo ra mỗ mã nguồn dễ nhìn dễ bảo trì. 

- Single Responsibility Principle: Class đó được thiết kế để giải quyết chỉ một vấn đề hoặc phục vụ chỉ một đối tượng trong hệ thống 
- Open/Closed Principle: Các class, modules, functions có thể được mở rộng mà không cần thay đổi code hiện có. Điều này thường được thực hiện thông qua kế thừa, đa hình và nên đóng để sửa đổi một khi một thực thể đã được phát triển và kiểm thử, code nguồn của nó không nên bị thay đổi để thêm các chức năng mới. Việc sửa đổi code hiện có sẽ làm tăng nguy cơ phát sinh lỗi trong các chức năng đã hoạt động
- Liskov Substitution Principle: Các đối tượng của một lớp cha nên có thể được thay thế bằng các đối tượng của các lớp con mà không làm ảnh hưởng đến tính đúng đắn của chương trình
- Interface Segregation Principle: Client không nên bị buộc phải phụ thuộc vào những giao diện mà họ không sử dụng. Thay vì tạo ra một giao diện lớn, chung chung chứa rất nhiều phương thức, ISP khuyên chúng ta nên chia nhỏ nó thành nhiều giao diện nhỏ hơn, chuyên biệt hơn. 
- Dependency Inversion Principle: Các module cấp cao không nên phụ thuộc vào các module cấp thấp. Cả hai nên phụ thuộc vào các trừu tượng. Hơn nữa, các trừu tượng không nên phụ thuộc vào các chi tiết; các chi tiết nên phụ thuộc vào các trừu tượng.


