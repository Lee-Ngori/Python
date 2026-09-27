'''for i in range (1,1001):
    s=i
    for j in range (1,i):
        if i%j==0:
            s -= j 
    if s == 0:
        print(i,end=' ')

# ...existing code...
for i in range (1,1001):        # 遍历 1 到 1000
    s = i                       # 把 i 的初值赋给 s，后面从 s 中减去所有真约数
    for j in range (1,i):       # 遍历 1 到 i-1 的每个可能约数
        if i % j == 0:          # 如果 j 是 i 的约数
            s -= j              # 从 s 中减去该约数
    if s == 0:                  # 如果减完后 s 为 0，说明真约数之和等于 i
        print(i, end=' ')       # 打印该完美数，之间以空格分隔
# ...existing code...'''

'''for i in range(1,10):
    for j in range(1,10):
        if j>=i:
            print(f"{i}*{j}={i*j:2}",end=' ',)
        else:
            print(" "*6,end=' ')
    print()
'''
'''
a=int(input("请输入一个三位数："))
i = (a//100)
j=(a//10)%10
k = a%10
print(f"{i}{j}{k}",end=' ')
'''
'''
n, m = map(int, input().split())

# 初始化猴子列表，编号从1到n
monkeys = list(range(1, n + 1))
current = 0  # 当前报数的位置索引

# 当列表中不止一只猴子时继续循环
while len(monkeys) > 1:
    # 计算要移除的猴子的索引
    # (current + m - 1) % len(monkeys) 确保索引在有效范围内
    remove_index = (current + m - 1) % len(monkeys)
    # 移除选中的猴子
    monkeys.pop(remove_index)
    # 更新当前位置索引
    current = remove_index % len(monkeys) if len(monkeys) > 0 else 0

# 输出最后剩下的猴子编号，即大王
print(monkeys[0])
'''
'''year,month = map(int,input ().split())
if month in [1,3,5,7,8,10,12]:[print("31")]
elif month in[4,6,9,11]:print("30")
else:
    if year%4==0 and year%100!=0 or year%400==0:
        print("29")
    else:
        print("28") 
'''
'''
xingbie,age=input().split()
age=int(age)    
if xingbie=="m":
    if age>=18 and age<=22:
        print("Ture")
    else:
        print("False")
if xingbie=="f":
    if age>=17 and age<=21:
        print("Ture")
    else:
        print("False")          
'''
'''
idcard  = input ().strip()
if len(idcard) != 18:
    print(f"{idcard}是非法身份证号")    
else:
    if not idcard[:17].isdigit():
        print(f"{idcard}是非法身份证号")
    else:
        weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code_map = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 
                          5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
        total = sum(int(idcard[i]) * weights[i] for i in range(17))
        z = total % 11
        expected_code = check_code_map[z]
        actual_code = idcard[-1].upper()
        if actual_code == expected_code:
            print(f"{idcard}是合法身份证号")
        else:
            print(f"{idcard}是非法身份证号")
'''
'''
import random
daxie = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
xiaoxie = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
chars = daxie + xiaoxie + num
length = int(input("请输入密码长度："))
password = ''.join(random.choice(chars) for _ in range(length))
print("生成的随机密码是：", password)
'''
'''
count = 0
for num in range(100,201):
    if num % 3 != 0:
        print(num,end=' ')
        count += 1
    if count%10==0:
        print()
'''
'''
count = 0
for num in range (100,201):
    if num % 3 !=0:
        print(num,end=' ')
        count =count+1
    if count %10==0:
        print()
        '''


    