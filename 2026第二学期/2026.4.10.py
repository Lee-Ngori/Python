class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
        print(f'Push:{item}')
    def pop(self):
        if len(self.items) == 0 :
            print('None')
        else:
            print(f'Pop:{self.items.pop()}')
    def peek(self):
        if len(self.items) == 0 :
            print('None')
        else:
            print(f'Peek:{self.items[-1]}')
    def display(self):
        for item in self.items:
            return self.items
def test():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.peek()
    stack.pop()
    print(stack.display())
test()