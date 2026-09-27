n = int(input())
lis = list(map(int,input().split()))
count = 0 
s = set(lis)
counted = set()
for i in range(n):
    for m in range (i+1,n):
        now = lis[i] +lis[m]
        if now in s and now not in counted:
            counted.add(now)
            count +=1 
print(count)