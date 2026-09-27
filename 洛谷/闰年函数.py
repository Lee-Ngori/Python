a,b = map(int,input().split())
lis = []
def runnian(a,b):
    count = 0 
    for i in range(a,b+1):
        if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0) :
            count +=1
            lis.append(i)
    return count,lis

count,years = runnian(a,b)
print(count)
if count > 0 :
    print(*years)
else:
    print()
