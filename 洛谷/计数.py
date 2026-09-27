n ,tar = map(int,input().split())
count = 0
for i in range(1,n+1):
    for chao in str(i):
        if  int(chao) == tar:
            count += 1
print(count)