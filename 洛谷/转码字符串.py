n=int(input())
s= input().strip()
res = []
for c in s :
    new_code = (ord(c)-ord('a')+n) % 26 +ord('a')
    res.append(chr(new_code))
print(''.join(res))