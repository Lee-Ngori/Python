class Time():
    def __init__(self,hour,minute):
        self.hour = hour
        self.minute = minute
    def display(self):
        print(f'{self.hour:02d}:{self.minute:02d}')
    def add_minutes(self,minutes):
        total_minute = self.hour * 60 + self.minute + minutes
        new_min = total_minute % 60
        new_hour = (total_minute // 60) %24 
        self.minute = new_min
        self.hour = new_hour
def test():
    t = Time(10,10)
    t.display()
    t.add_minutes(50)
    t.display()

test()
