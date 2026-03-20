from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.emp_id = emp_id
        self.__salary = salary
        
    
    @abstractmethod
    def calculate_pay(self):
        pass
    
    @property
    def salary(self):
        return self.__salary
    
        
    

class Fulltime(Employee):
    def __init__(self,name,emp_id,salary):
        super().__init__(name,emp_id,salary)
        
        
    def calculate_pay(self):
        return self.salary
    
    
    @classmethod
    def from_dict(cls,data:dict):
            return cls(data['name'],data['emp_id'],data['salary'])
        
    
class Parttime(Employee):
    def __init__(self, name, emp_id, salary,hours,rateperhour):
        super().__init__(name, emp_id, salary)
        self.hours = hours
        self.rateperhour = rateperhour
        
        
    def calculate_pay(self):
        total_wage = self.salary+(self.hours*self.rateperhour)
        return total_wage
        
    
class Contractor(Employee):
    def __init__(self, name, emp_id,contract_amount):
        super().__init__(name, emp_id, salary=0)
        self.contract_amount = contract_amount
        
        
    def calculate_pay(self):
        total_wage = self.salary + self.contract_amount
        return total_wage
        

class Manager(Fulltime):
    def __init__(self, name, emp_id, salary,team_bonus):
        super().__init__(name, emp_id, salary)
        self.team_bonus = team_bonus
        
        
    def calculate_pay(self):
        total_wage = self.salary + self.team_bonus
        return total_wage
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            data["name"],
            data["emp_id"],
            data["salary"],
            data["team_bonus"]       # Manager needs extra field
        )
    
        
# e = Employee("Anand Patidar",125,10000000)
# print(e)                                  #cannot instantiate abstract class
# print(e.salary)

ft = Fulltime("Vijay Suman",45,2000000)
print(ft)
print(ft.calculate_pay())

pt = Parttime("Ajay Prajapati",18,500000,5,2000)
print(pt)
print(pt.calculate_pay())

ct = Contractor("Kavy Singhal",65,40000)
print(ct)
print(ct.calculate_pay())

mg = Manager("Anand Patidar",125,10000000,5000000)
print(mg)
print(mg.calculate_pay())

# Data coming from a database / JSON / API
employee_data = {"name": "Vijay Suman", "emp_id": 45, "salary": 200000}
manager_data  = {"name": "Anand Patidar", "emp_id": 125, "salary": 1000000, "team_bonus": 500000}

ft = Fulltime.from_dict(employee_data)
mg = Manager.from_dict(manager_data)

print(ft)    
print(mg)   

records = [
    {"name": "Ajay", "emp_id": 1, "salary": 50000},
    {"name": "Priya", "emp_id": 2, "salary": 60000},
]
employees = [Fulltime.from_dict(r) for r in records]