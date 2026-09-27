def fun(lis):
    name = lis[0]
    grade = lis[1]
    suzhi = lis[2]
    total  = grade  +suzhi
    zonghe = grade *7 +suzhi*3
    return name ,total,zonghe

n = int(input())
lll = []
for _ in range(n):
    stu = list(map(int,input().split()))
    name,zongfen ,zonghe = fun(stu)
    lll.append([zongfen,zonghe])
for i in range(n):
    if (lll[i][0] > 140) and (lll[i][1]>=800):
        print('Excellent')
    else:
        print('Not excellent')