'''
changeOne = int(input())
changeTwo = int(input())
plus = int(input())
a = changeOne
b= changeTwo
c=plus
a,b=b,a 
e = a+c
print(e)
'''
'''
workYear = int(input())
if workYear < 5:
    print("工资涨幅为0")
elif  workYear >= 5 and workYear < 10:
    print("工资涨幅为5%")

elif workYear >= 10 and workYear < 15:
    print("工资涨幅为10%")
else:
    print("工资涨幅为15%")
    '''
'''
jimscore = int(input())
jerryscore = int(input())
if jimscore > jerryscore:
    print("jim ")
else:
    print("jerry")      
    '''
'''
# 第一题 ##############
from math import *  

i = 1 # 当前计算的值  
s = 0 # 计算出来的和   
########### begin ##########
while i <=999:
	######### end     ####
    s = s + i ** 2  
    i = i + 2  

print(s)  

########## 第二题 ##############
x = int(input())  

if x<0:  
	print('无实数解')  
else:  
	g = x/2  		
while abs(x-g*g)>=1e-6:
    g = (g + x/g)/2   
print('{:.10f}'.format(g))  
''' 
'''
studentnum = int(input())
for student in range(1,studentnum+1):
    sum = 0
    inputlist = input()
    subjectscore=list(map(int,inputlist.split((","))))
    for score in subjectscore:
        score = int(score)
        sum = sum + score
    print("第%d位同学的总分为:%d" %(student,sum))
'''
# import math
# row = int(input())
# if row == 1:
#     print("*", end = "" )
#     exit()
# if row % 2 == 0 :
#     raise ValueError
# row = math.ceil( row / 2.0 )
# for n in range(1, row + 1 ):
#     i = 2 * n - 1  #每一行*的个数
#     j = ( row - n ) * 2  #每一行空格的个数
#     for jj in range(j):#控制输出每一行的空格
#         print(" ", end="")
#     if i > 1:  #如果一行字母*的个数大于1，则要控制*和*之间的空格格式然后输出
#         for ii in range(i):
#             if ii != i - 1:
#                 print("* ", end="")
#             else:
#                 print("*")
#     else:  #如果一行的字母*的个数等于1，则直接输出*
#         print("*")

# # 输出完菱形的上半部分，下半部分直接通过反向控制输出
# ########## Begin ##########
# # 注意最后一层一个*的时候，不需要换行，去掉换行
# for n in range(row - 1, 0, -1):
#     i = 2 * n - 1  # 每一行*的个数（与上半部分对称）
#     j = (row - n) * 2  # 每一行空格的个数（与上半部分对称）
#     # 输出空格
#     for jj in range(j):
#         print(" ", end="")
#     # 输出*及中间的空格
#     if i > 1:
#         for ii in range(i):
#             if ii != i - 1:
#                 print("* ", end="")
#             else:
#                 print("*")
#     else:
#         # 最后一行（1个*），去掉换行符
#         print("*", end="")
# ########## End ##########
'''
i = 1
while i <=5:
    print(f"the number is {i}")
    if i ==3:
        print("hello")    
        break
    i+=1
    '''
'''
alex =list(map(int,input().split(",")))
if len(alex)!=5:
    print("输入错误")
else:
    for num in alex:
        print(f"数字{num}的位数是{len(str(abs(num)))}")
    stnum = sorted(alex)
    print(f"从小到大排序后的数字是：{','.join(map(str,stnum))}")
    '''
'''
studs = [
    [('SID', 101), ('Chinese', 90), ('English', 100), ('Math', 95)],
    [('SID', 102), ('Math', 95), ('Chinese', 85), ('English', 92)],
    [('SID', 103), ('Chinese', 60), ('Math', 100), ('English', 70)]
]
scores = {}
for student in studs:
    sid = None
    sub_scores = {}
    for item in student:
        key, value = item
        if key == 'SID':
            sid = value
        else:
            sub_scores[key] = value
    if sid is not None:
        scores[sid] = sub_scores
sorted_sids = sorted(scores.keys())
for sid in sorted_sids:
    print(f"SID {sid}")
    for subject, score in scores[sid].items():
        print(f"{subject:<10} {score}")
    print()
    '''
'''
list_dict = [{'a': 1, 'b': 2}, {'b': 3, 'a': 4}, {'b': 1}]
key_count = {}
for d in list_dict:
    for key in d:
        if key in key_count:
            key_count[key] += 1
        else:
            key_count[key] = 1
result = [key for key, count in key_count.items() if count >= 2]
print(result)
'''
def flatten_dict(d, parent_key='', sep='_'):
    items = {}
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten_dict(v, new_key, sep))
        else:
            items[new_key] = v
    return items
source_dict = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
flattened = flatten_dict(source_dict)
print(flattened)