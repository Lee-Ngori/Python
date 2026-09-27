# m,n = map(int,input().split())
# count = [0] *10
# for i in range(m,n+1):
#     temp = i 
#     while temp > 0:
#         temp , mowei  = divmod(temp,10)
#         count[mowei] += 1
# print(*count)

import sys

def main():
    m, n = map(int, sys.stdin.buffer.read().split())
    cnt = [0] * 10 
    for i in range(m, n + 1):
        temp = i
        while temp:
            digit = temp % 10
            cnt[digit] += 1
            temp //= 10
    print(*cnt)

main()