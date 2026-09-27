def selection_sort_report(num):
    n = len(num)
    for i in range(n):
        min_index = i 
        for j in range(i+1, n):
            if num[j] < num[min_index]:
                min_index = j 
        num[i],num[min_index] = num[min_index],num[i]
        print(num)
def test():
    num = [29,10,14,37,13]
    selection_sort_report(num)
test()