def insertion_sort(lis):
    n = len(lis)
    for i in range(1,n):
        now = lis[i]
        j = i - 1
        while j >= 0 and lis[j] > now: 
            lis[j+1] = lis[j]
            j = j-1
        lis[j+1] = now
    return lis
def test():
    lis = [8,4,3,7,6,5,2,1]
    print(insertion_sort(lis))
test()