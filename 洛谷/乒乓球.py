import sys 
def get_re():
    lis = []
    stop = False
    for line in sys.stdin:
        if stop:
            break
        pos = line.find('E')
        if pos != -1:
            line = line[:pos]
            stop = True
        lis.append(line)
    raw = ''.join(lis)
    record = ''.join(n for n in raw if n =='W' or n == 'L')
    return record
def calculate(record,target):
    ans = []
    w_sc = 0
    l_sc = 0 
    for m in record:
        if m == 'W':
            w_sc +=1 
        else:
            l_sc +=1 

        if (w_sc >= target or l_sc >= target ) and abs(w_sc - l_sc) >=2:
            ans.append(f'{w_sc}:{l_sc}')
            w_sc = 0
            l_sc = 0 
    ans.append(f'{w_sc}:{l_sc}')
    return ans 

record = get_re()
re_11 = calculate(record,11)
re_21 = calculate(record,21)
print('\n'.join(re_11))
print()
print('\n'.join(re_21))