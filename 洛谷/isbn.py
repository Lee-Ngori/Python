n = input().strip()
digits = n.replace('-','')
front = digits[:9]
check = digits[-1]
total = 0 
for i ,ch in enumerate(front,start = 1 ):
    total += i * int(ch)
correct_code = total % 11
if correct_code == 10:
    correct_char = 'X'
else:
    correct_char = str(correct_code)    

if check == correct_char:
    print("Right")
else:
    print(n[:-1]+correct_char)