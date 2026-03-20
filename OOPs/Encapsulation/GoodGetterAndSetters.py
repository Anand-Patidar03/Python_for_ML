class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):        # getter
        return self.__balance

    @balance.setter
    def balance(self, amount):   # setter
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")


acc = Account(10000)

print(acc.balance)     # getter

acc.balance = 5000     # setter
print(acc.balance)

acc.balance = -2000    # invalid 