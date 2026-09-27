class Employee():
    def __init__ (self,name,salary,bouns):
        self.name =name
        self.salary = salary 
        self.bouns =bouns 
    def add_bouns(self):
        self.salary += self.bouns
    def total_salary(self):
        return self.salary
    def display(self):
        print(f'Name:{self.name}')
        print(f'Salary:{self.salary}')
def test():
    a = str(input())
    b= int(input())
    c = int(input())
    e=Employee(a,b,c)
    e.add_bouns()
    e.display()
test()