def running_total(data):
    total = 0 
    for i in data:
        total = total + i
        yield total
    return total
        
def test():
    data = [3,1,4,2]
    for total in running_total(data):
        print(total)
test()