n = float(input())
start = 2 
s = 0 
count = 0 
while s < n :
    s += start
    start = 0.98*start 
    count += 1 
    
print(count)
