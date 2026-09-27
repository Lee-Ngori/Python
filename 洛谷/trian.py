l, m = map(int, input().split())
regions = []
for i in range(m):
    u, v = map(int, input().split())
    regions.append((u, v))
removed = [False]*(l+1)
for u,v in regions :
    for i in range(u,v+1):
        removed[i] = True
answer = removed.count(False)
print(answer)