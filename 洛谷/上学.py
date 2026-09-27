import math
s , v  = map(float, input().split())
t_minute = s/v
start_float = 8*60 -10- t_minute
start_int = math.floor(start_float)
if start_int < 0:
    start_int += 1440
hour = start_int // 60
minute = start_int % 60
print(f"{hour:02d}:{minute:02d}")