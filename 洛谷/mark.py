k = int(input())
found = False
for wuweishu in range(10000,30001):
    sanwei1 = int(str(wuweishu)[0:3])
    sanwei2 = int(str(wuweishu)[1:4])
    sanwei3= int(str(wuweishu)[2:5])
    if sanwei1 % k == 0 and sanwei2 % k == 0 and sanwei3 % k == 0:
        print(wuweishu)
        found = True
if not found:
    print("No")