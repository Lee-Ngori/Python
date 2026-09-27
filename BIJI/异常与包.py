#抛出异常 raise
#1、创建一个Exception类的对象,XXX---异常提示信息
#2、raise抛出异常对象
#raise Exception("这是一个异常提示信息")
# def funa():
#     raise Exception('我抛出了一个异常')
#     print('哈哈哈笑死我了')     #执行了raise之后,后续的代码就不会再执行了,所以这行代码不会被执行到
# funa()

#需求：密码长度不足，就报异常
#分析：用户输入密码，判断输入长度是否大于等于6，如果输入长度不足6位，就报错，即抛出自定义异常，并捕获该异常
# def login():
#     password = input('请输入密码: ')
#     if len(password) >=6:
#         return('登录成功')
#     raise Exception('密码长度不足,请重新输入')
# # print(login())
# try: #隔离危险代码：告诉python去执行，如果出错了别崩溃就行了
#     print(login())
# except Exception as e: #except捕获异常：如果try中的代码出现了异常，就会执行except中的代码，e是一个变量，接收异常对象
#     print(e)
# #捕获异常：为了检测到代码异常时能保证代码接着运行，保证程序不中止

#模块 ：本质上就是一个py文件，导入模块就是执行一个py文件
#内置模块
# 如：random模块，time模块，datetime模块，math模块，os模块，sys模块等
#第三方模块
#下载：cmd窗口输入 pip install 模块名
#自定义模块：自己以及自己在项目中定义的模块 ，不要和内置模块起冲突  

#导入模块 方式一
# 格式 ：import 模块名 , 虽然可以一个import导入多个模块，但不建议这么做，建议每行只导入一个模块
#调用：模块名.功能名
# import pytry
# print(pytry.name)

#导入模块 方式二
#格式：from 模块名 import 功能名 (只导入指定部分)
#调用：直接输入功能功能名，不需要导入模块名
# from pytry import fund
# from pytry import name #需要的功能一定要导入
# fund()
# print(name)

# 方式三
#语法 ： from 模块名 import * (导入模块中的所有功能)
# from pytry import *
# fund()
#不建议过多使用 from 模块名 import * 这种方式，因为可能会导入一些不需要的功能，造成命名冲突，导致代码难以维护

#as 给模块起别名
#语法 import 模块名 as 别名
# import pytry as pt
# pt.fund()
# print(pt.name)

#as 给功能起别名
#语法 from 模块名 import 功能名 as 别名
# from pytry import fund as d , name , func as c
# d()
# print(name)
# c()
#注意：导入多个功能要用逗号将功能与功能隔开，后面的功能也可以取别名

#内置全局变量 __name__ :表示当前模块的名字
#语法： 
#if __name__ == '__main__':  #当模块被直接运行时，__name__的值为'__main__'，当模块被导入时，__name__的值为模块名
#作用：用来控制py文件在不同运用场景执行不同的逻辑。同一py文件在自行运行和被导入运行的两种情况下运行与显示的内容将会不同

#第一种 自己执行自己 文件在当前程序执行
#if __name__ == '__main__':

#第二种：文件被当作模块被其他文件导入运行
# __name__ == 模块名 可见pytry2.py

# import pytry2
# pytry2.test()

#4.1 包 （pycharm中的python file）
#含义：项目结构中的文件夹/目录
#与普通文件夹的关系 ：包是一个特殊的文件夹，包中必须有一个__init__.py文件，包中可以包含模块和子包，包的作用是为了组织模块和子包，使得项目结构更加清晰，便于维护和管理
#作用：将有联系的模块放到同一个文件夹中，有效避免模块名称冲突，让结构更清晰
#新建包：右键项目名 -> new -> python package -> 输入包名 -> 点击enter
#在pycharm中我创建出来了

#4.5 import 导入包时，首先执行__init__.py文件的代码
#导包方式一：
# import pack_01

#导包方式二：
# from pack_01 import register
 #会先执行init中的代码

#4.6不建议在initial文件中写过多代码，尽量保证init文件的内容简单
#4.7__all__: 本质上是一个列表，列表里面的元素就代表要导入的模块
#作用：可以控制要引入的东西
from pack_01 import *
register.reg()
login.log()