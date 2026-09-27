class ReverseIterator:
    def __init__(self,lis):
        self.lis = lis
        self.index = len(lis) - 1 
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < 0 :
            raise StopIteration
        else:
            self.index = self.index - 1
            return self.lis[self.index + 1]
def test():
    data = ['1','2','3','4','5']
    for item in ReverseIterator(data):
        print(item)
test()