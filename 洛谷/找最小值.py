n = int(input())
min = float('inf')
nums = list(map(int, input().split()))
for m in range (n):
    if nums[m] < min :
        min = nums[m]
print(min)