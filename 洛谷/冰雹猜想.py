n = int(input())
lis = [n]                    
while n != 1:
    if n % 2 == 0:             
        n //= 2               
    else:
        n = 3 * n + 1
    lis.append(n)
print(*lis[::-1])
