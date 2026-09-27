class Node():
    def __init__(self,value):
        self.value = value 
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def display(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            print(current.value,end='->')
            current = current.next
        print('None')
    def insert_after(self,target,value):
        new_node = Node(value)
        current = self.head
        while current is not None:
            if current.value == target:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
    def delete(self,target):
        if self.head is None :
            print('List is empty')
            return
        if self.head.value == target:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current is not None :
            if current.value == target:
                prev.next = current.next
                return
            prev = current
            current = current.next
def test():
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    li.display()
    li.insert_after(20,25)
    li.display()
    li.delete(20)
    li.display()
test()