pi =3.14
h , r  = map(int,input().split())
v = pi * r**2 * h
total = 20000
times = total / v 
if type(times) == int:
    print(times)
elif type(times) == float:
    print(int(times)+1)