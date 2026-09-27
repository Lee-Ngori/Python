#作用域
#含义：指变量生效的范围，分为 全局变量 和 局部变量

#1、全局变量：
#函数外部定义的变量，在整个文件中都有效
a = 100 
def test1():
    print('这是test1 中a的值：',a )
def test2():
    a =120
    print('这是test2 中a的值：',a )
test1()
test2() 
print('调用函数后a的值：',a )
#a的值在test2后并未被覆盖成120是因为：函数内部如果要使用变量会先从函数内部找，没有才去函数外部找
#test2中的a的值只在该函数中生效

#局部变量
#含义：函数内部定义的变量，从定义开始位置到函数结束位置有效
def funa():
    num = 10 #局部变量
    print('funa中的num:',num)
funa()
#局部变量只能在被定义的函数中使用，函数外部不能使用
#作用：在函数体内部临时保存变量数据，当函数调用完成后就销毁局部变量
def funb():
    num = 18 
    print('funb中的num值：',num )
funb()

#在函数内部修改全局变量的值   global 关键字
#作用：将变量修改为全局变量
#格式： global 变量名
b = 100 
print('修改前的b:',b)
def funi():
    global b    #申明全局变量    若有多个变量要全局化可用 global a,b 的形式
    b = 1231    #可以修改全局变量
    print('修改后的b:',b)
funi()
print('测试修改的b',b)

#nonlocal 关键字----->将变量声明为外层变量（是外层函数的局部变量，而且不能是全局变量）。只能在嵌套函数中使用
e = 10 #全局
def outer():
    e = 5  #局部变量
    def inner():
        # nonlocal e 
        e =20
        def inner2():
            nonlocal e      #nonlocal 只能在上一层进行修改，没有办法修改两层及以上
            e = 30
            print('inner2中的e值',e)
        inner2()
        print('inner函数中e的值：',e)
    inner()
    print('outer函数中的e:',e)
outer()

#匿名函数
#基本语法 ： 函数名 = lambda 形参 :返回值（表达式）
#调用： 结果 = 函数名（实参）

add = lambda a,b : a+b #a,b 是匿名函数的形参，a+b是返回值的表达式
#lambda 函数不需要写return来返回值，表达式本身结果就是返回
print(add(1,4))

#lambda 的参数形式
#基本语法 ： 函数名 = lambda 形参 :返回值（表达式）
#1、无参数
funx = lambda : '一杯水'
print(funx())

#2、一个参数
funz = lambda name : name
print(funz('Blue Archive'))

#3、默认参数
funt = lambda future , age = 2103: (future ,age) #返回值是以元组的形式，所以此处要加括号
print(funt('LIhua'))
print(funt('NIUmo',100))
#默认参数一定要写在非默认参数后面

#4、可变\关键字参数
funp  =  lambda **kwargs :kwargs
print(funp(fas = 'ljsd',pods= 100))

