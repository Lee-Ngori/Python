def zhishu(num):
    if num <= 1 :
        return False
    if num == 2 :
        return True
    if num % 2 == 0:
        return False
    limit  = int(num**0.5) +1
    for i in range (3,limit,2):
        if num % i == 0 :
            return False
    return True

n = int(input())
lis = list(map(int,input().split()))
ans = []
for x in lis :
    if zhishu(x) is True:
        ans.append(x)
print(' '.join(map(str,ans)))