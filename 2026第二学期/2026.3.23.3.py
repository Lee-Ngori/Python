class Product():
    def __init__(self,name,price,quantity):
        self.name= name
        self.price = price
        self.quantity = quantity
    def totle_price(self):
        return self.price * self.quantity
def test():
    a= input()
    b= int(input())
    c= int(input())
    apple = Product(a,b,c)
    print('Output:')
    print(apple.name)
    print(apple.totle_price())
test()