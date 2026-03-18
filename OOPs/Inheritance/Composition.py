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


# Usage
acc = Account(10000)
sav = SavingAccount(acc)

acc.deposit(5000)

sav.add_interest()

acc.show_balance()   # 15750 ✅