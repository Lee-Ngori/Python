def fun(shu):
    if shu == 0:
        return 1
    return (fun(shu-1)+1)*2
    

n = int(input())
print(fun(n-1))