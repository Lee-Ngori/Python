class Node():
    def __init__(self,value,):
        self.value = value
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self,value):
        new_node = Node(value)
        if self.head is None :
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def display(self):
        if self.head is None:
            print('None')
            return
        current = self.head
        while current is not None:
            print(current.value,end= '=>' if  current.next is not None else' None' )
            current = current.next
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count
    def search(self,target):
        current =self.head
        while current is not None:
            if current.value == target:
                return True 
            current = current.next
        return False
def test():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    li.display()
    print('search 20',li.search(20))
    print('search 99',li.search(99))
    print('长度',li.length())
test()