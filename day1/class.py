class Employee(): 
    
    def __init__(self, first_name, last_name, salary):
        self.first = first_name
        self.last = last_name
        self.email = first_name + '.' + last_name + '@techlead.com'
        self.salary = salary

