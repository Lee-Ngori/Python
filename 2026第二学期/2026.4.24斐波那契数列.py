def fibonacci(n):
    a,b = 0,1
    count = 0
    while count < n:
        a,b = b,a+b
        yield a 
        count +=1
n = int(input('你要几项斐波那契?'))
for num in fibonacci(n):
    print(num)