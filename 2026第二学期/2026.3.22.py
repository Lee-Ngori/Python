class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print(f'存款成功，当前余额为{self.balance:.2f}')
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'取款成功，当前余额为{self.balance:.2f}')
        else:
            print('没钱了警告一次')
    def show_balance(self):
        print(f'当前余额为{self.balance:.2f}')

def test():
    account = BankAccount('张三',1000)
    account.show_balance()
    account.deposit(500)
    account.withdraw(200)
test()