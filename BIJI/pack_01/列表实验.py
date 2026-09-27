n = int(input())
count = 0 
while n > 0 :
    m = str(n)
    lis = [int(t) for t in m]
    n = n - sum(lis)
    count += 1
print(count)

