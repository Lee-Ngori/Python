n = int(input())
jieguo = [0,0,0,0,0,0,0]
zhongjiang = list(map(int,input().split()))
for i in range(n):
    count = 0
    maide = list(map(int,input().split()))
    for j in maide :
        for k in zhongjiang:
            if j == k :
                count += 1 
    if count == 7 :
        jieguo[0] += 1 
    elif count == 6:
        jieguo[1] += 1 
    elif count == 5 :
        jieguo[2] += 1 
    elif count == 4 :
        jieguo[3] += 1
    elif count == 3 :
        jieguo[4] += 1
    elif count == 2 :
        jieguo[5] += 1 
    elif count == 1 :
        jieguo[6] += 1 
    
print(*jieguo)
     
