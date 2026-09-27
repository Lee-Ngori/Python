import sys
# 填上你觉得需要的其他模块

def main():
    T = int(input())
    if T == 1:
        # 粘贴问题 1 的主函数代码
        print("I love Luogu!")
    elif T == 2:
        # 粘贴问题 2 的主函数代码
        print(2 + 4, 10 - 2 - 4)
    elif T == 3:
        # 请自行完成问题 3 的代码
        a = 14 // 4
        b = 4*a
        c=  14 % 4
        print(a,b,c,sep = '\n')
        pass
    elif T == 4:
        # 请自行完成问题 4 的代码
        a = 500 / 3
        print(f'{a:.6g}')
        pass
    elif T == 5:
        # 请自行完成问题 5 的代码
        a = 480/32
        print(f'{a:.0f}')
        pass
    elif T == 6:
        # 请自行完成问题 6 的代码
        a = (9**2 + 6**2)**0.5
        print(f'{a:.2f}')
        pass
    elif T == 7:
        # 请自行完成问题 7 的代码
        print(110,90,0,sep = '\n')
        pass
    elif T == 8:
        # 请自行完成问题 8 的代码
        pi = 3.141593
        zhouchang = 2 * pi * 5 
        mianji = pi * 5 **2 
        tiji = 4/3 * pi * 5 ** 3
        print(zhouchang,mianji,tiji,sep = '\n')
        pass
    elif T == 9:
        # 请自行完成问题 9 的代码
        print(22)
        pass
    elif T == 10:
        # 请自行完成问题 10 的代码
        print(9)

        pass
    elif T == 11:
        # 请自行完成问题 11 的代码
        print(100/3)
        pass
    elif T == 12:
        # 请自行完成问题 12 的代码
        print(13,'R',sep = '\n')
        pass
    elif T == 13:
        # 请自行完成问题 13 的代码
        pi = 3.141593
        v1 = 4/3 * pi * 4**3
        v2 = 4/3 * pi * 10**3
        total = v2+v1
        l = total**(1/3)
        print(f'{l:.0f}')
        pass
    elif T == 14:
        # 请自行完成问题 14 的代码
        print(50)
        pass

if __name__ == "__main__":
    main()
