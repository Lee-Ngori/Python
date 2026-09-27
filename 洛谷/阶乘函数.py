def whu(i):
    if i <= 1:
        return 1
    return whu(i-1) * i



n = int(input())
print(whu(n))