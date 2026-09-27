n = int(input())
num = 1
for i in range(1,n+1):
    for m in range(n-i +1):
        print(f'{num:02d}',end='')
        num +=1 
    print()