from itertools import combinations, permutations


def find_min(n, max_val=30):
    best = None
    vals = list(range(1, max_val+1))
    for comb in combinations(vals, n):
        # quick bound: product grows fast; skip if product too big
        prod = 1
        s = 0
        for x in comb:
            prod *= x
            s += x
            if prod > 10**9:
                break
        if prod > 10**9:
            continue
        for perm in permutations(comb):
            p = 1
            sm = 0
            for x in perm:
                p *= x
                sm += x
                if p > 10**9:
                    break
            if p == sm:
                if best is None or list(perm) < best:
                    best = list(perm)
    return best

for n in range(1,9):
    ans = find_min(n, max_val=30)
    print(n, ans)
