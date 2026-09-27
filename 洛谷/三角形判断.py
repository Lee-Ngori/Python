a,b,c = map(int, input().split())
a,b,c = sorted([a,b,c])
if a + b < c:
    print('Not triangle')
if a**2 + b**2 == c**2:
    print('Right triangle')
if a**2 + b**2 > c**2:
    print('Acute triangle')
if a**2 + b**2 <c ** 2 :
    print('Obtuse triangle')
if a==b or b == c or a == c:
    print('Isosceles triangle')
if a==b and b==c:
    print('Equilateral triangle')
    