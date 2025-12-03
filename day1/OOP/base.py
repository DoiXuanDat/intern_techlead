from abc import ABC, abstractmethod

class Team:
    def __init__(self, members=None):
        self.members = members or []

    def add(self, member):
        self.members.append(member)

    def total_pay(self):
        return sum(m.salary for m in self.members)

    def __repr__(self):
        member_names = ", ".join(m.full_name() for m in self.members)
        return f"Team({member_names})"

    def __add__(self, other):
        new_members = self.members[:]
        if isinstance(other, Team):
            new_members.extend(other.members)
        elif hasattr(other, 'salary'): # Duck typing check cho Employee
            new_members.append(other)
        return Team(new_members)

class Employee(ABC):
    def __init__(self, first_name, last_name, salary, dept=None):
        self.first_name = first_name
        self.last_name = last_name
        
        # Encapsulation: Protected attribute
        self._email = f"{first_name}.{last_name}@techlead.com"
        
        # Encapsulation: Private attribute 
        self.__real_salary = salary 
        
        # Public salary 
        self.salary = salary 
        self.dept = dept

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_real_salary(self):
        return self.__real_salary

    @abstractmethod
    def work(self):
        pass

    def __add__(self, other):
        if isinstance(other, Employee):
            return Team([self, other])
        if isinstance(other, Team):
            return Team([self] + other.members)
        return NotImplemented
    