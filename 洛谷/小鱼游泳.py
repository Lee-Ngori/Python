a,b,c,d = map(int,input().split())
first_time = a*60 + b 
end_time = c*60 + d 
time = end_time - first_time
hour = time // 60
minute = time %60
print(f'{hour} {minute}')
