# #从键盘输入一个人名
# name = input()
     
# #1 请定义一个名为Person的类及其初始化方法，在初始化方法中有一个参数name，用于初始化对象obj的姓名obj.name
# ########## Begin #######

# class Person:
#         def __init__(self,name):
#              self.name =name
# ########## End ##########

# #2 请调用Person类构造一个p1对象，p1.name为name变量（name是在第一行代码键盘输入的）
# ########## Begin #######
# p1 = Person(name)
# ########## End ##########
# print(p1.name)


# #3 请在下面给Person2类添加一个show方法，该方法会print出：Hello Lucy! （假设对象姓名self.name为Lucy）
# class Person2(Person):
#     ########## Begin #######
# 	def show(self):
#             print(f'Hello {name}!')
#     ########## End ##########

# #4 请调用Person2类构造一个p2对象，p2.name为name（name是在第一行代码键盘输入的），接着调用p2的show方法。
# ########## Begin #######
# p2 = Person2(name)
# p2.show()
# ########## End ##########


# class Animal():
#     def __init__(self, name):
#         self.name = name
#     def breath(self):
#         print(f'{self.name}在呼吸。')
#     def eat(self):
#         print(f'{self.name}在进食。')
        
# # 请在下面填入定义Fish类的代码，fish类继承自animals类，有一个swim方法输出print(f"{self.name}可以游泳。")
# ########## Begin ##########
# class Fish(Animal):
#     def swim(self):
#         print(f"{self.name}可以游泳")
# ########## End ##########  

# # 请在下面填入定义Bird类的代码，Bird类继承自Animal类，有一个方法fly输出print(f"{self.name}可以飞翔。")，有一个eat方法print(f"{self.name}可以吃鱼。")
# #********** Begin *********#
# class Bird(Animal):
#     def fly(self):
#         print(f"{self.name}可以飞翔。")

#     def eat(self):
#         print(f"{self.name}可以吃鱼。")
# ########## End ##########  
		
# fName = input()
# f = Fish(fName)
# f.breath()
# f.swim()
# f.eat()

# bName = input()
# b = Bird(bName)
# b.breath()
# b.fly()
# b.eat()

def findPayment(loan, r, m):
    # 请在此添加代码，补全函数findPayment
    #********** Begin *********#
    if r == 0:
        huankuan = loan / m
        return huankuan
    else:
        huankuan = loan * (r * (1 + r)**m) / ((1 + r)**m - 1)
    return huankuan
    #********** End *********#

class Mortgage(object):
     def __init__(self, loan, annRate, months):
        # 请在此添加代码，补全函数__init__
        #********** Begin *********#
        self.loan = loan
        self.months = months
        self.rate = annRate / 1200
        self.payment = findPayment(loan, self.rate, months)
        self.paid=[0.0]
        self.owed=[loan]
        
         #********** End *********#
        self.legend = None

     def makePayment(self):
         # 请在此添加代码，补全函数makePayment
         #********** Begin *********#
        lixi = self.owed[-1] * self.rate
        benjin = self.payment - lixi
        self.paid.append(self.payment)
        new_owed = self.owed[-1] - benjin
        self.owed.append(new_owed)
         #********** End *********#

     def getTotalPaid(self):
         # 请在此添加代码，补全函数getTotalPaid
         #********** Begin *********#
        return sum(self.paid)

         #********** End *********#

     def __str__(self):
        return 'The Mortgage is {self.legend}, Loan is {self.loan}, Months is {self.months}, Rate is {self.rate:.2f}, Monthly payment is {self.payment:.2f}'.format(self=self)

if __name__=="__main__": 
    loan, annRate, months = [float(x) for x in input().split()]
    m1 = Mortgage(loan, annRate, months)
    print(m1)
    m1.makePayment()
    m1.makePayment()
    print('Two months payment is {:.2f}'.format(m1.getTotalPaid()))
 