# coding=utf-8

# 创建并初始化munu_list列表
menu_list = []
while True:
    food = input()
    if not food:
        break
    menu_list.append(food)

# 请在此添加代码，对menu_list进行元祖转换以及元祖计算等操作，并打印输出元祖及元祖最大的元素
########## Begin ##########
menu=tuple(menu_list)
print(menu)
print(max(menu))

########## End ########## 

# 寻找菜单中首字母最小的元素，输出其索引和值。
########## Begin ##########
print(menu.index(min(menu)))
print(min(menu))

########## End ########## 