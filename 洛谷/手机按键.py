s = input()
count = 0
for i in s :
    if i =='a' or i == 'd' or i =='g' or i =='j' or i == 'm' or i == 'p' or i == 't' or i == 'w' or i == ' ':
        count += 1
    elif i =='b' or i == 'e' or i =='h' or i =='k' or i == 'n' or i == 'q' or i == 'u' or i == 'x' :
        count +=2 
    elif i =='c' or i == 'f' or i =='i' or i =='l' or i == 'o' or i == 'r' or i == 'v' or i == 'y':
        count += 3 
    else:
        count +=4
print(count)