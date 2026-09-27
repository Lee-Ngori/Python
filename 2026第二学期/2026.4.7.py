class Employee:
    def __init__(self,name,salary):
        self.name =name
        self.salary = salary
    def display(self):
        print(self.name)
class Manager(Employee):
    def __init__(self,name,salary,bouns):
        super().__init__(name,salary)
        self.bouns = bouns
    def display(self):
        print(f'Manager:{self.name},Salary:{self.salary},Bouns:{self.bouns},Total:{self.salary+self.bouns}')
class Worker(Employee):
    def __init__(self,name,salary,work_hours):
        super().__init__(name,salary)
        self.work_hours = work_hours
    def display(self):
        print(f'Worker:{self.name},Salary:{self.salary},Hours:{self.work_hours}')
def test():
    Tom = Manager('Tom',5000,1000)
    Tom.display()
    Alice = Worker('Alice',3000,100)
    Alice.display()
test()