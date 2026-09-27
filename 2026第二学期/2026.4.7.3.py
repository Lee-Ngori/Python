import math
class Circle():
    def __init__ (self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius **2
class Cylinder():
    def __init__(self,radius,height):
        self.base = Circle(radius)
        self.height = height
    def get_mianji (self):
        base_minaji = self.base.area()
        ce_mianji = 2* math.pi * self.base.radius * self.height
        return f'{base_minaji * 2+ ce_mianji:.2f}'
    def get_tiji(self):
        return f'{self.base.area() * self.height:.2f}'
def test():
    a = int(input('Radius:'))
    b = int(input('Height:'))
    cyl = Cylinder(a,b)
    print(cyl.get_mianji())
    print(cyl.get_tiji())
test()