import math
class Shape():
    def __init__(self,colour):
        self.colour=colour
    def get_colour(self):
        return self.colour
class Circle(Shape):
    def __init__(self, radius:float,colour):
        super().__init__(colour)
        self.radius:float=radius
    def get_area(self):
        area=(self.radius**2) * math.pi
        return area
    def get_radius(self):
        return self.radius
    def __str__(self):
        return f"颜色：{self.colour} 半径{self.radius} 面积{self.get_area():.2f}"
class Rectangle(Shape):
    def __init__(self, colour,width:float,length:float):
        super().__init__(colour)
        self.width:float=width
        self.length:float=length
    def get_area(self):
        area=self.width * self.length
        return area  
    def get_perimeter(self):
        perimeter=(self.width+self.length)*2
        return perimeter
    def __str__(self):
        return f"颜色:{self.colour} 长：{self.length} 宽:{self.width} 面积:{self.get_area()} 周长:{self.get_perimeter()}"
class Cylinder(Circle):
    def __init__(self, radius:float, colour,height:float):
        super().__init__(radius, colour)
        self.height=height
    def get_area(self):
        area=2*math.pi*self.radius*self.height+2*math.pi*(self.radius)**2
        return area
    def get_volume(self):
        volume=self.radius**2 * math.pi * self.height
        return volume
    def __str__(self):
        return f" 颜色:{self.colour} 高:{self.height}  底面半径:{self.radius}体积:{self.get_volume()}表面积:{self.get_area()} "
a=Circle(2,'red')
b=Rectangle('yellow',1,2)
c=Cylinder(1,'blue',2)
def test_shapes():
    print(f'面积：{a.get_area():.2f}')
    print(f'面积：{b.get_area()}周长：{b.get_perimeter()} ')
    print(f'表面积：{c.get_area():.2f}体积：{c.get_volume():.2f}')
test_shapes()