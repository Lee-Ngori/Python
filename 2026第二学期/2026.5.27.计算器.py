class AddStrategy:
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    def calculate(self,a,b):
        print(f'Add result:{a+b}')
class MultiplyStrategy:
    def __init__(self,a,b):
        self.a = a 
        self.b = b 
    def calculate(self,a,b):
        print(f'Multiply result:{a*b}')
class Calulator:
    def __init__(self,strategy):
        self.strategy = strategy
    def excute(self,a,b):
        return self.strategy.calculate(a,b)
def test():
    a = 3
    b = 5
    cal1 = Calulator(AddStrategy(a,b))
    cal1.excute(a,b)
    cal2 = Calulator(MultiplyStrategy(a,b))
    cal2.excute(a,b)
test()