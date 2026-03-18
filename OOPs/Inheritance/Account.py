class Account:
    def __init__(self,balance):
        self.balance = balance
        
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        self.balance -= amount
        return self.balance
        
    
class SavingAccount(Account):
    def __init__(self,balance,interest):
        super().__init__(balance)
        self.interest = interest
        
    def add_interest(self):
        interest_amt = acc.balance*self.interest
        acc.balance += interest_amt
        return acc.balance
  
          
        

class CurrentAccount(Account):
    def __init__(self,balance,overdraft):
        super().__init__(balance)
        self.overdraft = overdraft
        
    def withdraw(self, amount):
        if(acc.balance+self.overdraft >= amount):
            super().withdraw(amount)
            return acc.balance
        
        else:
            return "Amount cannot be withdrawn "
        
        
acc = Account(10000)
savacc = SavingAccount(acc.balance,0.05)
curracc = CurrentAccount(acc.balance,5000)

print(acc.deposit(20000))
print(acc.withdraw(5000))
print(savacc.add_interest())
print(curracc.withdraw(60000))