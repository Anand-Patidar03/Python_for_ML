import random

class BankAccount:
    def __init__(self, owner_name, account_no, balance):
        self.owner_name = owner_name
        self.__balance = balance      # private
        self.account_no = account_no
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        if amount >= 0:
            self.__balance = amount
            
        else:
            print("Invalid amount")
            
            
    def deposit(self,amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount try again !")
            
    def withdraw(self, amount):
        if not BankAccount.validate_amount(amount):
            raise ValueError("Withdraw amount must be positive")
        if amount > self.__balance:
            raise Withdraw_Excetion(f"Cannot withdraw {amount}, balance is {self.__balance}")
        self.__balance -= amount
            
            
            
    @classmethod
    def open_account(cls,owner_name,initial_deposit):
        
        account_no = "".join(str(random.randint(0, 9)) for _ in range(12))
        return cls(owner_name, account_no, initial_deposit)
    
    
    @staticmethod
    def validate_amount(amount):
        if(amount >= 0):
            return 1    
        
     
class Withdraw_Excetion(Exception):
    def __init__(self,message):
        super().__init__(message)
        
    def __str__(self):
        return f"{self.message}"  
    
    
    
class SavingAccount(BankAccount):
    def __init__(self, owner_name, account_no, balance,interest_rate):
        self.interest_rate = interest_rate
        super().__init__(owner_name, account_no, balance)    
   
 
    def monthly_interest(self):
        monthly = (self.interest_rate / 12) / 100
        return self.balance*monthly  
    
    @classmethod
    def open_account(cls, owner_name, initial_deposit, interest_rate):
        account_no = "".join(str(random.randint(0, 9)) for _ in range(12))
        return cls(owner_name, account_no, initial_deposit, interest_rate)
 
    
# bank = BankAccount.open_account("Anand Patidar",10000)

# print(bank)
# print(bank.account_no)
# print(bank.owner_name)
# print(bank.balance)

# bank.deposit(30000)

# print(bank.balance)

# bank.withdraw(15000)

# print(bank.balance)

sacc = SavingAccount.open_account("Anand Patidar",20000,5)

print(sacc)
print(sacc.monthly_interest())
print(sacc.balance)

