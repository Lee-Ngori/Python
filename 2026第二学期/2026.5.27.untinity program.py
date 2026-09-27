class Logger:
    _instance = None
    def __new__(jee):
        if jee._instance is None:
            jee._instance = super().__new__(jee)
            jee._instance.logs = []
        return jee._instance
    def add_log(self,value):
        self.logs.append(value)
    def show_log(self):
        for log in self.logs:
            print(log)
Danking = Logger()
Tyloo = Logger()
print(Danking is Tyloo)
Danking.add_log('Start System')
Tyloo.add_log('Load Config')
print('Logs:')
Danking.show_log()
print('let me check')
Tyloo.show_log()           