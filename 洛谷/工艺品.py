w, x, h = map(int,input().split())
cube = []
q = int(input())
count= 0 
for i in range(w+1):
    layer_1 = [] 
    for j in range(x+1):
        layer_2 = []
        for k in range(h+1):
            layer_2.append(0)
        layer_1.append(layer_2)
    cube.append(layer_1)
for n in range(q):
    x1 , y1 ,z1 ,x2,y2,z2 = map(int,input().split())
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            for k in range(z1,z2+1):
                cube[i][j][k] = 1 
for i in range(1,w+1):
    for j in range(1,x+1):
        for k in range(1,h+1):
            if cube[i][j][k] == 0:
                count +=1 
print(count)