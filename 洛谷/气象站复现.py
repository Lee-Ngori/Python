class Observer:
    def update(self,temp):
        pass 
class WeatherStation:
    def __init__(self):
        self.temperature = 0 
        self.observers = []
    def add_observer(self,obs):
        self.observers.append(obs)
    def notify_observers(self):
        for obs in self.observers:
            obs.update(self.temperature)
    def set_temperature(self,temp):
        self.temperature = temp
        self.notify_observers()
class PhoneDisplay(Observer):
    def update(self,temp):
        print(f'Phone Display:{temp}°C')
class WindowDisplay(Observer):
    def update(self,temp):
        print(f'Window Display:{temp}°C')
def test():
    st = WeatherStation()
    phone = PhoneDisplay()
    window = WindowDisplay()
    st.add_observer(phone)
    st.add_observer(window)
    st.set_temperature(26)
    st.set_temperature(30)
test()