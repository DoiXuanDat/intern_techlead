from base import Employee
from salary import Salary

class Dev(Employee):
    def work(self):
        return f"{self.full_name()} ({self.dept}) is writing code and debugging."

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, dept, team=None):
        super().__init__(first_name, last_name, salary, dept)
        self.team = team or []

    def work(self, *tasks, urgent=False, **context):
        if not tasks:
            return f"{self.full_name()} ({self.dept}) supervises the team."
        
        tasks_str = ", ".join(tasks)
        urgent_tag = " [URGENT]" if urgent else ""
        extra = " | ".join(f"{k}={v}" for k, v in context.items())
        
        return f"{self.full_name()} will: {tasks_str}{urgent_tag}" + (f" ({extra})" if extra else "")

class Director(Manager):
    def approve_budget(self, amount):
        return f"{self.full_name()} approved a budget of ${amount}"
    
    def work(self):
        return f"{self.full_name()} is holding a strategic meeting with board members."

class Accountant(Employee, Salary):
    def __init__(self, first_name, last_name, salary, tax_rate=0.1):
        super().__init__(first_name, last_name, salary, dept="Accounting")
        self.tax_rate = tax_rate
    
    def work(self):
        return f"{self.full_name()} is auditing financial records."

    def pay_summary(self):
        # Sử dụng method từ class cha thứ 2 (Salary_Calculation)
        final_pay = self.calculate_salary(self.salary, self.tax_rate)
        return f"{self.full_name()} calculated salary: ${final_pay}"

class Mentor:
    def __init__(self, name):
        self.name = name
    

    def work(self):
        return f"{self.name} (Mentor) runs a major upskilling session."