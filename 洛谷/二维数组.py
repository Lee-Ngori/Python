n = int(input())
score = [] 
for i in range (n):
    chinese ,math,english  = map(int,input().split())
    score.append([chinese,math,english])
count = 0 
for i in range(n -1 ):
    for j in range(i+1,n):
        dif_c = abs(score[i][0]-score[j][0])
        dif_m = abs(score[i][1]-score[j][1])
        dif_e = abs(score[i][2]-score[j][2])
        sum_i = score[i][0] + score[i][1] + score[i][2]
        sum_j = score[j][0] + score[j][1] + score[j][2]
        diff_sum = abs(sum_i - sum_j)
        if dif_c <= 5 and dif_m <= 5 and dif_e <= 5 and diff_sum <= 10:
            count += 1 
print(count) 