memo = {}  # 存储已计算的结果

def F(n):
    if n == 1 or n == 2:
        return 1
    if n not in memo:
        res=  F(n-1) + F(n-2)    # 没算过才递归
        memo.setdefault(n, res)  # 存储结果
    return memo[n]         # 算过直接返回

print(F(100))  # 瞬间输出：354224848179261915075
print(memo)  # 输出已计算的结果