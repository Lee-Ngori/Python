def fun(lis):
    name = lis[0]
    s_c = int(lis[1])
    s_m = int(lis[2])
    s_e = int(lis[3])
    total = s_c +s_e +s_m
    return name ,s_c,s_m,s_e,total

n = int(input())
lis = []
for _ in range(n):
    stu = input().split()
    info = fun(stu)
    lis.append(info)
for i in range(n):
    for m in range(i+1,n):
        name1,sc1,sm1,se1,total1 = lis[i]
        name2,sc2,sm2,se2,total2 = lis[m]
        if (abs(sc1-sc2) <=5) and (abs(sm1-sm2) <= 5) and (abs(se1-se2)<=5) and (abs(total1 - total2) <= 10):
            print(f'{name1} {name2}')
