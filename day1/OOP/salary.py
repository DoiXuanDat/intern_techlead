class Salary:
    def calculate_salary(self, salary, tax):
        pay = salary * (1 - tax)
        return pay