n = int(input())
mar = []
y_k_1 = 0 
x_k_1 = n//2
for _ in range(n):
    mar.append([0]*n)
mar[y_k_1][x_k_1] = 1 #先是行后是列
k = 1

while k < n*n: 
    if y_k_1 == 0 and x_k_1 != n-1 :
        y_k_1 = n-1
        x_k_1 = x_k_1 + 1 
    elif y_k_1 != 0 and x_k_1 == n -1:
        y_k_1 = y_k_1 - 1 
        x_k_1 = 0 
    elif y_k_1 == 0 and x_k_1 == n-1 :
        y_k_1 = y_k_1 + 1
    else:
        if mar[y_k_1 -1][x_k_1 +1] == 0 :
            y_k_1 = y_k_1 - 1 
            x_k_1 = x_k_1 + 1 
        else :
            y_k_1 = y_k_1 + 1
    k = k+1
    mar[y_k_1][x_k_1] = k
for i in range(n):
    for j in range(n):
        print(mar[i][j], end='') 
        if j != n - 1:
            print(' ', end='')     
    print()                         