n = int(input())
s = abs(n)
if s != 0:
    while s % 10 == 0:
        s = s // 10
else:
    s = 0
t = str(s)
m = t[::-1]
if n < 0:
    print('-' + m)
elif n > 0:
    print(m)
else:
    print(0)