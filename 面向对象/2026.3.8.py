# print("-" * 35)
# print(f"{'摄氏度 (°C)':<15} | {'华氏度 (°F)':<15}")
# print("-" * 35)
# for wendu in range(1,101,10):
#     huashi = wendu * 9 / 5 +32
#     print(f"{wendu:<15} | {huashi:<15.1f}")

# a = str(input())
# b = a[::-1]
# if a == b:
#     print('It is a palindrome!')
# else:
#     print('It is not a palindrome!')

# def test(a):
#     a = str(a)
#     return len(a) >= 8 and any(c.isupper() for c in a) and any(c.islower() for c in a) and any(c.isdigit() for c in a)

# awd = input()
# if test(awd):
#     print('密码强度合格')
# else:
#     print('密码强度不合格')

import random
num = random.sample(range(1,50),6)
li = sorted(num)
print(li)
    
