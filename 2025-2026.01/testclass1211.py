# absencenum = int(input())#缺席学生的索引（从1开始）
# studentname = []
# inputlist = input()
# for i in inputlist.split(','):
#    result = i
#    studentname.append(result)
# count = 0
# # 请在此添加代码，填入循环遍历studentname列表的代码
# ########## Begin ##########
# for student in studentname:
#     if count + 1 == absencenum:
#         count += 1
#         continue
# ########## End ##########
#     count += 1
# 	# 请在此添加代码，跳过缺席学生
# 	########## Begin ##########
#     if count == absencenum:
#         continue    

# 	########## End ##########
# print(student,"的试卷已阅")

# -*- coding:utf-8 -*-
# import random
# people_guess = [ x for x in map( str, input("").split(",") ) ]
# computer_lst = ["石头","剪刀","剪刀","布","布","石头","布"] # 电脑出拳的方式
# computer_win_condition = [["布","石头"],["石头","剪刀"],["剪刀","布"]] # 每次电脑赢的情况
# balance_condition = [["布","布"],["石头","石头"],["剪刀","剪刀"]] # 每次平局的情况
# computer_win_number = 0 # 电脑赢的次数
# people_win_number = 0   # 玩家赢得次数

# #********* Begin *********#
# for i in range(7):
#     computer_choice = computer_lst[i]
#     people_choice = people_guess[i]
#     if [computer_choice, people_choice] in computer_win_condition:
#         computer_win_number += 1
#     elif [computer_choice, people_choice] in balance_condition:
#         continue
#     else:
#         people_win_number += 1
# #********* End *********#

# # 游戏进行 7 次之后，进行输赢的判别
# if computer_win_number > people_win_number:
# 	print("电脑赢!",end="")
# elif computer_win_number < people_win_number:
# 	print( "玩家赢!", end="" )
# else:
# 	print("平局!") 

# 创建并初始化Guests列表
# guests = []

# while True:
#     guest = input()
#     #请在此添加代码，输入客人名字，空输入退出循环
#     ########## Begin ##########
#     if guest =="":
#         break
#     guests.append(guest)
#     ########## End ########## 

	
# # 请在此添加代码，对guests列表进行插入、删除等操作
# ########## Begin ##########
# delete_guest = guests.pop()
# del guests[-1]
# guests.insert(2,delete_guest)
# del guests[1]
# print(guests)
# ########## End ########## 

# # 请在此添加代码，对新的guests列表排序
# ########## Begin ##########
# guests_sorted = sorted(guests,reverse=True)
# print(guests_sorted)
# ########## End ########## 
# print(guests)


# # 创建并初始化Guests列表
# guests = []

# while True:
#     guest = input()
#     #请在此添加代码，输入客人名字，空输入退出循环
#     ########## Begin ##########
#     if guest == "":
#         break
#     guests.append(guest)
#     ########## End ########## 

	
# # 请在此添加代码，对guests列表进行插入、删除等操作
# ########## Begin ##########
# # step1: 删除列表末尾元素并保存到deleted_guest
# if guests:  # 防止列表为空时报错
#     deleted_guest = guests.pop()
# else:
#     deleted_guest = ""

# # step2: 将deleted_guest插入到索引2的位置
# if len(guests) >= 2:  # 确保索引2存在
#     guests.insert(2, deleted_guest)
# elif len(guests) == 1:  # 列表长度为1时，索引2等同于末尾
#     guests.insert(2, deleted_guest)
# elif len(guests) == 0 and deleted_guest:  # 原列表只有1个元素的情况
#     guests.insert(2, deleted_guest)

# # step3: 删除索引1的元素
# if len(guests) > 1:  # 确保索引1存在
#     guests.pop(1)

# # 打印step1的deleted_guest变量
# print(deleted_guest)
# # 打印step3改变后的guests列表
# print(guests)
# ########## End ########## 

# # 请在此添加代码，对新的guests列表排序
# ########## Begin ##########
# # 按首字母从大到小排序
# guests_sorted = sorted(guests, key=lambda x: x[0] if x else "", reverse=True)
# print(guests_sorted)
# ########## End ##########

# coding=utf-8

# 创建并初始化munu_list列表
# menu_list = []
# while True:
#     food = input()
#     if not food:
#         break
#     menu_list.append(food)

# # 请在此添加代码，对menu_list进行元祖转换以及元祖计算等操作，并打印输出元祖及元祖最大的元素
# ########## Begin ##########
# # 转换为元组并打印元组与元组中按字典序最大的元素
# menu_tuple = tuple(menu_list)
# print(menu_tuple)
# if menu_tuple:
#     print(max(menu_tuple))
# else:
#     # 如果为空，打印空元组和提示（可根据需要调整）
#     print(())
# ########## End ########## 

# # 寻找菜单中首字母最小的元素，输出其索引和值。
# ########## Begin ##########
# if menu_list:
#     # 按第一个字符比较（空字符串视为空）
#     min_item = min(menu_list, key=lambda s: s[0] if s else "")
#     min_index = menu_list.index(min_item)
#     print(min_index)
#     print(min_item)
# else:
#     # 列表为空时输出占位结果
#     print(-1, "")
# ########## End ##########

# capitals = {'湖南':'长沙','湖北':'武汉','广东':'广州','广西':'南宁','河北':'石家庄','河南':'郑州','山东':'济南','山西':'太原',
# '江苏':'南京','浙江':'杭州','江西':'南昌','黑龙江':'哈尔滨','新疆':'乌鲁木齐','云南':'昆明','贵州':'贵阳','福建':'福州','吉林':'长春','安徽':'合肥',
# '四川':'成都','西藏':'拉萨','宁夏':'银川','辽宁':'沈阳','青海':'西宁','甘肃':'兰州','陕西':'太原',
# '内蒙古':'呼和浩特','台湾':'台北','北京':'北京','上海':'上海','天津':'天津','重庆':'重庆',
# '香港':'香港','澳门':'澳门'}
# while True:
#     province = input()
# 	########## Begin ##########        
#     if province in capitals:
#         print(capitals[province])
#     else:
#         break
# 	########## End ########## 


# num = input() 
# hole_dic = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
# ########## Begin ########## 
# while num:
#     count_of_hole = 0
#     for digit in num:
#         count_of_hole += hole_dic.get(digit, 0)
#     break
# ########## End ########## 

# print(count_of_hole)  

# def menu():
#     print('''\n欢迎使用PYTHON学生通讯录
# 1：添加学生
# 2：删除学生
# 3：修改学生信息
# 4：搜索学生
# 5：显示全部学生信息
# 6：退出并保存''')

# dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}

# #print(dic)
# print('--'*10)
# menu()
# c=input()
# print('=='*10)
# print('选择', c)
# if c=='4':
#     name = input()
#     print('**' * 10)
#     # ########## Begin ##########
#     if name in dic:
#         print(name,*dic[name])
#         print("Success")
#         print(dic)
#     else:
#         print("No Record")
        
#     # ########## End ##########
# else:
#     print("ERROR")


# 

import string
#string.ascii_lowercase即'abcdefghijklmnopqrstuvwxyz'

########## Begin ########
#函数found：输入参数m，判断是否'ERROR'，然后再调用input函数输入n字符串判断 'FOUND', 'NOT FOUND'，函数返回值为'ERROR'，'FOUND', 'NOT FOUND'。
def found(m):
    for check_m in m:
        if check_m not in string.ascii_lowercase:
            return"ERROR"
        n  = input()
        for check_n in n:
            if check_n not in string.ascii_lowercase:
                return"ERROR"
        n_run =set(n)
        for chei in m:
            if chei not in n_run:
                return"NOT FOUND"
        return"FOUND"
        
########## End ##########   
if __name__ == '__main__':
    m = input()
    output = found(m)
    print(output)