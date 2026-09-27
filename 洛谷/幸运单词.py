from collections import Counter

word = input().strip()         
freq = Counter(word)
maxn = max(freq.values())      
minn = min(freq.values())      
diff = maxn - minn
if diff < 2:
    is_prime = False
else:
    is_prime = True
    i = 2
    while i * i <= diff:       
        if diff % i == 0:
            is_prime = False
            break
        i += 1
if is_prime:
    print("Lucky Word")
    print(diff)
else:
    print("No Answer")
    print(0)