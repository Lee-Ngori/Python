def fun(student):
    name = student[0]
    chinese = int(student[1])  
    math = int(student[2])      
    english = int(student[3])
    total = chinese + math + english
    return name , total ,chinese,math ,english

n = int(input())
now = ''
max_sc = -1 
new_c = new_e = new_m = 0
for i in range(n):
    stu = input().split()
    name , total,chinese,math ,english= fun(stu)
    if total > max_sc:
        max_sc = total
        new_c = chinese
        new_m = math
        new_e = english
        now = name 
print(f'{now} {new_c} {new_m} {new_e}')
