def fun(score):
    total = sum(score) - min(score) - max(score)
    count = len(score) - 2
    return total, count
# def fun(score):
#     score = score.copy()  # 防止修改外部列表
#     score.remove(min(score))
#     score.remove(max(score))
#     return sum(score), len(score)
n , m = map(int,input().split())
max_ave = 0.0
for i in range(n):
    scores = list(map(int,input().split()))
    total ,count = fun(scores)
    ave = total / count
    if ave > max_ave :
        max_ave = ave 
print(f'{max_ave:.2f}')