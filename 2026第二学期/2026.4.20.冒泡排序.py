def bubble_sort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis
def test():
    lis = [5,2,4,1,3]
    soted_lis = bubble_sort(lis)
    print(soted_lis)
test()