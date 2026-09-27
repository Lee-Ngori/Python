import math
class Vector3d:
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def length(self):
        # 请在这里补充代码，完成本关任务
    	#********** Begin *********#
        return math.sqrt(self.__x**2 + self.__y**2 + self.__z**2)

    	#********** End *********#
    # 请在这里增加3个特殊方法，分别用来支持加法运算符、减法运算符以实现两个三维向量间的加法和减法运算
    	#********** Begin *********#
    def __add__(self,other):
        if isinstance(other,Vector3d):
            new_x = self.__x + other.__x
            new_y = self.__y + other.__y
            new_z = self.__z + other.__z
            return Vector3d(new_x, new_y, new_z)
    def __sub__(self,other):
        if isinstance(other,Vector3d):
            new_x = self.__x - other.__x
            new_y = self.__y - other.__y
            new_z = self.__z - other.__z
            return Vector3d(new_x, new_y, new_z)
    def __str__(self):
        return f'({self.__x:.2f} {self.__y:.2f} {self.__z:.2f})'
    	#********** End *********#
        
if __name__=="__main__": 
    x1, y1, z1 = [float(x) for x in input().split()]
    m1 = Vector3d(x1, y1, z1) 
    print('The m1 is', m1)
    print('Length of m1 is {:.2f}'.format(m1.length())) 

    x2, y2, z2 = [float(x) for x in input().split()]
    m2 = Vector3d(x2, y2, z2) 
    print('The m2 is', m2)    
    print('Length of m2 is {:.2f}'.format(m2.length()))
    
    m3 = m1 + m2
    print('The m3 is', m3)
    print('Length of m1+m2 is {:.2f}'.format(m3.length()))
    m4 = m1 - m2
    print('The m4 is', m4)
    print('Length of m1-m2 is {:.2f}'.format(m4.length()))