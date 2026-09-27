n = int(input())
min_cost = float('inf')
for i  in range (3):
    count,price = map(int,input().split())
    pack = (n + count-1) // count
    total = pack * price
    if total < min_cost:
        min_cost = total
print(min_cost)
