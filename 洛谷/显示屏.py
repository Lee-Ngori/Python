n = int(input())
s = input().strip()
digital = {
    '0' : ['XXX','X.X','X.X','X.X','XXX'],
    '1' : ['..X','..X','..X','..X','..X'],
    '2' : ['XXX','..X','XXX','X..','XXX'],
    '3' : ['XXX','..X','XXX','..X','XXX'],
    '4' : ['X.X','X.X','XXX','..X','..X'],
    '5' : ['XXX','X..','XXX','..X','XXX'], 
    '6' : ['XXX','X..','XXX','X.X','XXX'],
    '7' : ['XXX','..X','..X','..X','..X'],
    '8' : ['XXX','X.X','XXX','X.X','XXX'],
    '9' : ['XXX','X.X','XXX','..X','XXX'] 
    }
for row in range(5):
    line = ''
    for i in range(len(s)):
        ch = s[i]
        line += digital[ch][row] 
        if i != len(s) - 1: 
            line += '.'
    print(line)
