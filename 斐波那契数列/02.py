momo = {}
def F(n):
    if n == 0:
        return 1
    else:
        res= n*F(n-1)
        momo[n]=res
        return res

def jisuan(n):
    count = 0
    for i in range(1,n+1):
        count = count + F(i)
    return count
    
n = int(input())
print(jisuan(n))