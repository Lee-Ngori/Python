from itertools import combinations, permutations


def find_min_by_formula(n, max_val=60):
    best = None
    vals = list(range(1, max_val+1))
    for comb in combinations(vals, n-1):
        prod = 1
        s = 0
        for x in comb:
            prod *= x
            s += x
            if prod > 10**12:
                break
        if prod <= 1:
            continue
        y_num = s
        denom = prod - 1
        if y_num % denom != 0:
            continue
        y = y_num // denom
        if y <= 0 or y in comb or y > max_val*100:
            continue
        # now construct all permutations with y inserted
        elems = list(comb) + [y]
        for perm in permutations(elems):
            p = 1
            sm = 0
            from itertools import combinations, permutations


            def find_min_by_formula(n, max_val=60):
                best = None
                vals = list(range(1, max_val+1))
                for comb in combinations(vals, n-1):
                    prod = 1
                    s = 0
                    for x in comb:
                        prod *= x
                        s += x
                        if prod > 10**12:
                            break
                    if prod <= 1:
                        continue
                    y_num = s
                    denom = prod - 1
                    if y_num % denom != 0:
                        continue
                    y = y_num // denom
                    if y <= 0 or y in comb or y > max_val*100:
                        continue
                    # now construct all permutations with y inserted
                    elems = list(comb) + [y]
                    for perm in permutations(elems):
                        p = 1
                        sm = 0
                        for x in perm:
                            p *= x
                            sm += x
                            if p > 10**12:
                                break
                        if p == sm:
                            if best is None or list(perm) < best:
                                best = list(perm)
                return best

            for n in range(4,9):
                ans = find_min_by_formula(n, max_val=50)
                print(n, ans)
