class Counter:
    def __init__(self):
        self.value = 0
    def increase(self):
        self.value += 1
    def decrease(self):
        self.value -= 1
    def reset(self):
        self.value = 0
    def display(self):
        print(f"Value: {self.value}")

def main():
    c = Counter()
    while True:
        choice = input().strip()  
        if choice == "1":
            c.increase()
        elif choice == "2":
            c.decrease()
        elif choice == "3":
            c.reset()
        elif choice == "4":
            break
        else:
            continue  
        c.display()

main()