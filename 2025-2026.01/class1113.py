'''
def happy():
    print('Happy Birthday!')
happy()
def happy2():
   return 'Happy Birthday!'
info = happy2()
print(info)
def happy3(person):
    return f'Happy Birthday! Dear {person}.'.format(person)
person = input()
print(happy3(person))
'''
'''
########## Begin ########## 
#定义self_divisor函数。
#当该数为自除数，返回值为True
def self_divisor(num):
    temp = num  # 保存原始数字以便后续使用
    while temp > 0:  # 循环取出每一位数字进行判断
        digit = temp % 10  # 取出最后一位数字
        if digit == 0 or num % digit != 0:  # 如果该位数字为0或不能整除num，则num不是自除数
            return False
        temp //= 10  # 去掉最后一位数字，继续判断下一位
    return True  # 如果所有位数字都能整除num，则num是自除数
########## End ########## 



def output(n):
    """输出不小于n的自除数，无返回值"""
    for num in range(1, n + 1):  # 注意不大于包括等于n
        if self_divisor(num):  # 调用函数，当返回值为True时，该数为自除数，输出这个数
            print(num, end=' ')  # 输出以空格结尾


if __name__ == '__main__':
    m = int(input())
    output(m)

    '''
'''
# 以下面程序中补充你的代码
########## Begin #######
#car_info函数，输入参数3个，输出参数1个（格式化字符串）
def car_info(year,id,brand):
    if brand =="":
        brand = "宝马"
    return"这是一辆%s年生产，型号是%s的%s牌汽车。" %(year,id,brand)
########## End ##########

# 以下内容不要修改
ls = input().split()  # 根据空格切分输入字符串为列表，列表元素可能是两个或三个
print(car_info(*ls))       # 调用函数，取列表中的全部数据做参数
'''
'''
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def palindromic(num):
    str_num = str(num)
    if str_num==str_num[::-1]:
        return True
def reverse_num(shu):
    str_num=str(shu)
    rev_str_num=str_num[::-1]
    return int(rev_str_num)
def reverse_prime(number):
    i = 2
    count = 0
    while True:
        if not palindromic(i) and is_prime(i) and is_prime(reverse_num(i)):
            print(i, end=' ')  # i为回文素数时输出i，输出后不换行
            count = count + 1
            if count == number:
                break
        i = i + 1

if __name__ == "__main__":
    n = int(input())
    reverse_prime(n) 
    '''
'''
#输出**月有多少天

########## Begin ########
#函数is_leap：输入参数year，判断是闰年或平年，返回True或False
def is_leap(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
########## End ########## 

########## Begin ########
#函数days_of_month：输入参数年月字符串（如200101），返回对应月份的天数（31）
def days_of_month(date):
    year = int(date[:4])
    month = int(date[4:])
    #每个月的天数
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #判断是否为闰年，若是则2月天数为29
    if is_leap(year):
        month_days[1] = 29
    return month_days[month - 1]
########## End ##########  


if __name__ == '__main__':
    date_in = input()  # 输入一个年月
    print(days_of_month(date_in)) 
    '''
# import string
# #string.ascii_lowercase即'abcdefghijklmnopqrstuvwxyz'

# ########## Begin ########
# #函数found：输入参数m，判断是否'ERROR'，然后再调用input函数输入n字符串判断 'FOUND', 'NOT FOUND'，函数返回值为'ERROR'，'FOUND', 'NOT FOUND'。
# def found(m):
#     m = m.strip().lower()   # 去掉首尾空白并转小写，允许多字母单词
#     if not m or any(ch not in string.ascii_lowercase for ch in m):
#         return 'ERROR'
#     n = input().strip().lower()
#     if not n or any(ch not in string.ascii_lowercase for ch in n):
#         return 'ERROR'
#     elif m in n:
#         return 'FOUND'
#     else:
#         return 'NOT FOUND'
# ########## End ##########   
# if __name__ == '__main__':
#     m = input()
#     output = found(m)
    # print(output)

# import string
# #string.ascii_lowercase即'abcdefghijklmnopqrstuvwxyz'

# ########## Begin ########
# def found(m):
#     for relax in m:
#         if relax not in string.ascii_lowercase:
#             return 'ERROR'
#     # 输入n并检查n是否只包含小写字母（题目虽未明确要求，但按输入逻辑保持一致性）
#     n = input()
#     for relax in n:
#         if relax not in string.ascii_lowercase:
#             # 题目未明确n含非字母的处理，但按题意默认n符合要求？此处按输入规范处理，若n有非字母返回ERROR
#             return 'ERROR'
#     # 转换n为集合，判断m的每个字符是否都在n的集合中
#     n_chars = set(n)
#     for char in m:
#         if char not in n_chars:
#             return 'NOT FOUND'
#     return 'FOUND'
# ########## End ##########   
# if __name__ == '__main__':
#     m = input()
#     output = found(m)
#     print(output)

# import string
# def found(m):
#     for chat in m:
#         if chat not in string.ascii_lowercase:
#             return 'ERROR'
#     n = input()
#     for chat in n :
#         if chat not in string.ascii_lowercase:
#             return 'ERROR'

#输出**月有多少天

########## Begin ########
#函数is_leap：输入参数year，判断是闰年或平年，返回True或False
# def is_leap(year):
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         return True
#     else:
#         return False
# ########## End ########## 

# ########## Begin ########
# #函数days_of_month：输入参数年月字符串（如200101），返回对应月份的天数（31）
# def days_of_month(date):
#     year = int(date[:4])
#     month = int(date[4:])
#     #每个月的天数
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     #判断是否为闰年，若是则2月天数为29
#     if is_leap(year):
#         month_days[1] = 29
#     return month_days[month - 1]
# ########## End ##########  


# if __name__ == '__main__':
#     date_in = input()  # 输入一个年月
#     print(days_of_month(date_in)) 
import string
def found(m):
    for chat_m in m:
        if chat_m not in string.ascii_lowercase:
            return 'ERROR'  

    n = input()
    for chat_n in n :
        if chat_n not in string.ascii_lowercase:
            return 'ERROR'
    n_chars = set(n)
    for detai in m :
        if detai not in n_chars:                   
            return 'NOT FOUND'
        
    return 'FOUND'
if __name__ == '__main__':
    m = input()
    output = found(m)
    print(output)
