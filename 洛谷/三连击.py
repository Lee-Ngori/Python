def check(a,b,c):
    s = str(a) + str(b) + str(c)
    if sorted(s) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True
def main():
    result =[]
    for a in range(100,334):
        b = 2*a
        c = 3*a 
        if c >999:
            break
        if check(a,b,c):
            result.append((a,b,c))
    for a,b,c in sorted(result):
        print(f'{a} {b} {c}')
main()