class Circle:
    def draw(self):
        print('Draw Circle')
class Rectangle:
    def draw(self):
        print('Draw Rectangle')
class ShapeFactory:
    def creat_shape(self,value):
        if value == 'circle':
            return Circle()
        elif value == 'rectangle':
            return Rectangle()
        else:
            print('no shape')
def test():
    fac = ShapeFactory()
    shape1 = fac.creat_shape('circle')
    shape1.draw()
    shape2 = fac.creat_shape('rectangle')
    shape2.draw()
test()