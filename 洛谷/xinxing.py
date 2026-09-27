comet = input().strip()
team = input().strip()
def calc(name):
    result = 1 
    for char in name:
        value = ord(char) - ord('A') + 1
        result *= value
    return result
comet_value = calc(comet)
team_value = calc(team)
if comet_value % 47 == team_value % 47:
    print("GO")
else:
    print("STAY")