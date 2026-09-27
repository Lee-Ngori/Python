def draw_line(length,lable=''):
    line = '-' * length
    if lable :
        line += ' ' +str(lable)
    print(line)
def draw_interval(center_length):
    if center_length <= 0:
        return 
    draw_interval(center_length - 1)
    draw_line(center_length)
    draw_interval(center_length - 1)
def draw_ruler(num_inches,major_length):
    draw_line(major_length,lable= '0')
    for i in range(1,num_inches +1):
        draw_interval(major_length - 1)
        draw_line(major_length,lable=str(i))
def test():
    draw_ruler(2,4)
test()