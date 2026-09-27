n = int(input())
h = list(map(int, input().split()))
count = 0 
i = 1 
while i < n-1:
    if h[i] < h[i-1]:
        while i < n-1 and h[i] <= h[i+1]:
            if h[i] < h[i+1]:
                count += 1
                break
            i += 1
        else:
            pass
    i += 1

print(count)