#快读模板，可以提高读入数据效率
import sys 
input = lambda :sys.stdin.readline().strip()
#readline()方法可以从标准输入中读取一行数据，并返回一个字符串。strip()方法用于去除字符串两端的空白字符（包括换行符）。通过将input函数重新定义为lambda表达式，我们可以使用input()来快速读取输入数据，并且去除多余的空白字符。
#读取一行的时候
nums = list(map(int, input().split()))

#sorted()函数
#可以对任何可迭代对象进行排序，返回一个新的列表
#语法：sorted(iterable（可迭代对象）, key=None（排序规则）, reverse=False（是否逆序）)
#默认升序排序
nums= [5,3,8,6,7,2,4,1]
print(sorted(nums,key=None,reverse=False)) #升序排序]
print(sorted(nums,key=None,reverse=True)) #降序排序

#按照字符串长度排序
words = ['apple','banana','cherry','date']
print(sorted(words,key=len))

#sort
nums.sort() #直接修改原列表，默认升序排序
print(nums)

sort_words = sorted(words,key=lambda x: x[1]) 
print(sort_words) #按照字符串的第二个字符排序

#单行多个整数输入
a,b,c = map(int,input().split())
print(a,b,c)
#split()方法将输入的字符串按照空格分割成一个列表，map()函数将列表中的每个元素转换为整数，最后通过多变量赋值将结果分别赋值给a、b、c三个变量。

#多行多个输入
n = int(input()) #输入行数
lst = [int(input())for _ in range(n)] #使用列表推导式读取多行输入，每行输入一个整数，并将其转换为整数类型，最终得到一个整数列表
print(lst)

#矩阵输入
n,m = map(int,input().split()) #输入矩阵的行数和列数
matrix = [list(map(int,input().split())) for _ in range(n)] #使用列表推导式读取矩阵的每一行输入，每行输入m个整数，并将其转换为整数类型，最终得到一个二维列表（矩阵）
print(matrix)