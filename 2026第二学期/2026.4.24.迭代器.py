class CountIterator:
    def __init__(self,n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        else:
            result = self.current
            self.current += 1 
            return result
def test():
    n = 5
    counter = CountIterator(n)
    for num in counter:
        print(num)
test()