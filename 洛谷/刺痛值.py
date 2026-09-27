n,m = map(int,input().split())
lis = []
for _ in range(n):
    lis.append(int(input()))
if m == 0 :
    print(0)
else : 
    min_sum = float('inf')
    for i in range(n-m+1):
        current = 0 
        for j in range(i,i+m):
            current += lis[j]
        if current < min_sum:
            min_sum= current
    print(min_sum)
