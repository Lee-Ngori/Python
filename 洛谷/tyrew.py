k = int(input())
n = 1 
s1 = 0.0
count = 0
while s1 <= k:
    s1 = s1+(1.0/n)
    n = n+1
    count = count+1
print(count)