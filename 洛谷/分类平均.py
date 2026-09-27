n , k = map(int,input().split())
ke = []
buke = []
ke_cou = 0 
ke_zs = 0 
buke_zs = 0 
buke_cou = 0 
for i in range(1,n+1):
    if  i % k == 0 :
        ke.append(i)
        ke_cou += 1 
    else:
        buke.append(i)
        buke_cou += 1 
for m in ke : 
    ke_zs += m 
ke_pj = ke_zs /ke_cou
for m in buke:
    buke_zs += m 
buke_pj = buke_zs / buke_cou
print(f'{ke_pj:.1f} {buke_pj:.1f}')