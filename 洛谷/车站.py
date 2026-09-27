a, n, m, x = map(int, input().split())

if x == n:
    print(0)
    exit()

U_A = [0, 1, 0]   
U_B = [0, 0, 1]
P_A = [0, 1, 1] 
P_B = [0, 0, 0]

max_station = max(n - 1, x)
if max_station < 2:
    max_station = 2

for k in range(3, max_station + 1):
    ua_cur = U_A[k - 1] + U_A[k - 2]
    ub_cur = U_B[k - 1] + U_B[k - 2]
    U_A.append(ua_cur)
    U_B.append(ub_cur)
    pa_cur = P_A[k - 1] + ua_cur - U_A[k - 1]
    pb_cur = P_B[k - 1] + ub_cur - U_B[k - 1]
    P_A.append(pa_cur)
    P_B.append(pb_cur)

if n - 1 == 1:    
    t = 0
else:
    ua_n1 = U_A[n - 1]
    ub_n1 = U_B[n - 1]
    t = (m - ua_n1 * a) // ub_n1   

if x == 1 or x == 2:
    ans = a
else:
    ans = P_A[x] * a + P_B[x] * t

print(ans)