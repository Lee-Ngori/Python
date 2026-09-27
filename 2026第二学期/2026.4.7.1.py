class Animal():
    def speak(self):
        print(' is ...')
class Dog(Animal):
    def speak(self):
        print('WOOF!')
class Cat(Animal):
    def speak(self):
        print('Meow!')
def test():
    animal = [Dog(),Cat(),Dog(),Cat()]
    for ani in animal:
        ani.speak()
test()