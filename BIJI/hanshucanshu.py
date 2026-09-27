#必备参数（位置参数）
#含义：传递和定义的参数位置相同
#格式：def 函数名(参数1,参数2,...):
def funa(name,age,sex):
    print(name)
    print(age)
    print(sex)
funa("张三",20,"男")#写了几个就传几个参数


#默认参数
#含义：在定义函数时给参数设置默认值，调用函数时可以不传递参数，使用默认值
#格式：def 函数名(参数1=默认值1,参数2=
#注意：默认参数必须放在位置参数的后面
def funb(b,a=8):
    print(b)
    print(a)
funb(5,11)# 不传参数，使用默认值8
funb(10,5)# 传参数，使用传递的值10

#可变参数
#含义：传入的值的数量可以改变，可以传入多个也可不传。
#语法格式： def func(*args)   一般用args，但是一般你想用啥用啥，规范来讲一般用args
def func(*name):
    print(*name)    #以元组形式接收
    print(type(name))
func('海绵宝宝','派大星','章鱼哥')

#关键字参数
#格式 ： def func(**kwargs)
#除了以字典的形式接收的以外无与上个函数不同
def fund(**kwargs):
    print(kwargs)
    print(type(kwargs))
fund()  #空字典
#要用字典的关键字参数传值
fund(name = 'LEE',future='None')    #传值的时候需要采用 键=值 的形式
#作用：可以扩展函数的功能

#函数调用
# #含义：在一个函数里面调用另一个函数
def study():
    print('晚上在学习')
def course():
    study()
    print('Python基础')
course()


#嵌套定义
#含义：在一个函数中定义另一个函数
def todo():
    print('晚上在学习')
    def clsw():             
        print('Python基础')
    clsw()                          #注意缩进，定义和调用是同级的！！
todo()