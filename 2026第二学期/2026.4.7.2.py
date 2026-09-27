class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
class Shape():
    def __init__(self,color,center):
        self.color = color
        self.center = center
    def display(self):
        print(f'Shape color:{self.color}')
        print(f'center point:{self.center}')
def test():
    ce = Point(2,3)
    sh = Shape('Blue',ce)
    sh.display()
test()
