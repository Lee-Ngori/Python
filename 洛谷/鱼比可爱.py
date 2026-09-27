n = int(input())
lis = list(map(int, input().split()))
ans= []
for i in range(n):
    count = 0
    for m in range(i):
        if lis[m] < lis[i]:
            count += 1
    ans.append(str(count))
print(' '.join(ans))