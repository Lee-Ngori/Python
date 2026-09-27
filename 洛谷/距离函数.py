points = []
for i in range(3):
    x, y = map(float, input().split()) 
    points.append((x, y))
def distance(p1,p2):
    return  ((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2)**0.5
a = distance(points[0],points[1])
b = distance(points[1],points[2])
c = distance(points[2],points[0])

zhouchang = a+b+c
print(f'{zhouchang:.2f}')
