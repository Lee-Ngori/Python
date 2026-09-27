s1 ,s2 ,s3 = map(int,input().split())
fre = [0] *81
max_count = 0 
ans = 0 
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            total = i +j + k 
            fre[total] += 1
            if fre[total] >max_count:
                max_count = fre[total]
                ans = total

print(ans)