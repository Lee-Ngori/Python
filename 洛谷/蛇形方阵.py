n = int(input())
a= [[0]*n for _ in range(n)]
top, bottom = 0,n-1
left,right = 0,n-1
num =1 
while num <= n**2 :
    for i in range(left,right+1):
        a[top][i] = num 
        num += 1 
    top += 1 
    for i in range(top,bottom+1):
        a[i][right] = num
        num +=1 
    right -= 1
    for i in range(right,left-1,-1):
        a[bottom][i] = num 
        num += 1 
    bottom -= 1 
    for i in range(bottom,top-1,-1):
        a[i][left] = num 
        num+=1 
    left +=1 

for m in a :
    print(''.join(f'{x:>3}' for x in m ))