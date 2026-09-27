def des (n):
    if n == 0:
        return "0"
    i = 0 
    while (2**i) <= n :
        i += 1
    i -= 1

    if i == 0:
        part = "2(0)"
    elif i == 1:
        part = "2"
    else:
        part = '2(' + des(i) + ')'

    rest = n - (2**i)
    if rest == 0:
        return part
    else:
        return part + '+' + des(rest)
n = int(input())
print(des(n))