n, s = map(int, input().split())
t = s
for _ in range(n):
    word = input().strip()
    if 'daishuki' in word:
        t += 2
    elif 'shuki' in word:
        t += 1
    elif 'kirai' in word:
        if t >= 0:
            t = 0
    else:
        t -= 1

if t > 0:
    print(t - s)
else:
    print('shuki')