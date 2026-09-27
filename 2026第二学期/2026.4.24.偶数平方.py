def even_squares(n):
    count = 1
    while  count <= n :
        if count% 2 == 0:
            yield count **2
        count += 1 
n = int(input('你要几个偶数的平方?   :'))
for num in even_squares(n):
    print(num)
