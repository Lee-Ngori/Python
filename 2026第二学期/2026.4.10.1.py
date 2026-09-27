class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.append(item)
        print(f'Enqueue:{item}')
    def dequeue(self):
        if len(self.items) == 0 :
            print('None')
        else:
            print(f'Dequeue:{self.items.pop(0)}')
    def front(self):
        if len(self.items) == 0:
            print('None')
        else:
            print(f'Front:{self.items[0]}')
    def display(self):
        for item in self.items:
            return self.items
def test():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    queue.dequeue()
    queue.front()
    print(queue.display())
test()