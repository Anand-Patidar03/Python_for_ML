class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)


class SavingAccount:
    def __init__(self, account):
        self.account = account   # composition

    def add_interest(self):
        self.account.balance += self.account.balance * 0.05


# # Usage
# acc = Account(10000)
# sav = SavingAccount(acc)

# acc.deposit(5000)

# sav.add_interest()

# acc.show_balance()   

class RocketFlyBehavior:
    def fly(self):
        print("Flying with rocket")

class FlyBehavior:
    def fly(self):
        print("Flying")

class NoFlyBehavior:
    def fly(self):
        print("Cannot fly")

class Bird:
    def __init__(self, fly_behavior):
        self.fly_behavior = fly_behavior
    
    def perform_fly(self):
        self.fly_behavior.fly()
        

f = FlyBehavior() 
b = Bird(f)
b.fly_behavior = RocketFlyBehavior() 
# rf = RocketFlyBehavior()
b.fly_behavior.fly()

# b.perform_fly()