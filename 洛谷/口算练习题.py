i = int(input())
lis = []
current_op = ' ' 
for p in range(i):
    mun = input().split()
    lis.append(mun)
for ch in lis:
    if ch[0] in ('a','b','c'):
        current_op = ch[0]
        x = int(ch[1]); y = int(ch[2])
    else:
        x = int(ch[0]); y = int(ch[1])

    if current_op == 'a':
        result = x + y
        expr = f"{x}+{y}={result}"
    elif current_op == 'b':
        result = x - y
        expr = f"{x}-{y}={result}"
    else:  
        result = x * y
        expr = f"{x}*{y}={result}"

    print(expr)
    print(len(expr))