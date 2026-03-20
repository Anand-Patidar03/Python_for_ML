class Account:
    def __init__(self, balance):
        self.__balance = balance   # private

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance")


acc = Account(10000)

print(acc.get_balance())   # getter

acc.set_balance(5000)      # setter
print(acc.get_balance())

acc.set_balance(-2000)     # invalid 