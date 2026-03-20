class Person:
    def __init__(self,name,age):
        self._name = name   #protected variable (can be used inside derived class)
        self._age = age
        
    
class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)
        
    def display_info(self):
        print(f"The person's name is {self._name} and age is {self._age}")
        
        
student = Student("Anand Patidar",21)

student.display_info()