import math
class Shape:
    def __init__ (self,color:str):
        self.color: str = color
    def get_color(self):
        return self.color
class  Circle(Shape):
    def __init__(self,radius:float,color:str):
        self.radius: float = radius
        super().__init__(color)
    def get_area(self):
        return math.pi * self.radius**2
    def get_radius(self):
        return self.radius
    def __str__ (self):
        return f"Circle : Radius = {self.get_radius()} ,Color = {self.get_color()} ,Area = {self.get_area()}"
class Rectangle(Shape):
    def __init__ (self,width:float,length:float,color:str):
        self.width: float = width
        self.length: float = length
        super().__init__(color)
    def get_area(self):
        return self.width * self.length
    def get_perimeter(self):
        return 2 *(self.width + self.length)
    def __str__ (self):
        return f'Rectangle : Width = {self.width} , length = {self.length} , Color = {self.get_color()},Area = {self.get_area()} , Perimeter = {self.get_perimeter()}'
class Cylinder(Circle):
    def __init__(self,height:float,color,radius:float):
        self.height:float =height
        super().__init__(radius,color)
    def get_area(self):
        return 2 * math.pi *self.radius**2 + 2 * math.pi * self.radius * self.height
    def get_volume(self):
        return math.pi * self.radius ** 2 * self.height
    def __str__ (self):        return f'Cylinder : Height = {self.height} , Color = {self.get_color()} , Radius = {self.get_radius()} , Area = {self.get_area()} , Volume = {self.get_volume()}'
def test_shape():
    print('-'*50)
    print('Shape类测试')
    shape = Shape('red')
    print(f'颜色是:{shape.get_color()}')
    print('='*50)

    print('Circle类测试')
    circle = Circle(5,'blue')
    print(f'颜色是:{circle.get_color()}')
    print(f'半径是:{circle.get_radius()}')
    print(f'面积是:{circle.get_area():.3f}')
    print('='*50)

    print('Rectangle类测试')
    rectangle = Rectangle(4,6,'yellow')
    print(f'颜色是:{rectangle.get_color()}')
    print(f'面积是:{rectangle.get_area()}')
    print(f'周长是:{rectangle.get_perimeter()}')
    print('='*50)

    print('Cylinder类测试')
    cylinder = Cylinder(10,'green',3)   
    print(f'颜色是:{cylinder.get_color()}')
    print(f'底面半径是:{cylinder.get_radius()}')
    print(f'高是:{cylinder.height}')
    print(f'表面积是:{cylinder.get_area():.3f}')
    print(f'体积是:{cylinder.get_volume():.3f}')
    print('='*50)



if __name__ == '__main__':
    test_shape()