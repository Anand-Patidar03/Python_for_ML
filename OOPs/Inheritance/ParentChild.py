class Parent:
    def __init__(self,surname):
        self.surname = surname
        
    def fullName(self,name):
        print("Parent full name is",name,self.surname)
        
class Child(Parent):
    def __init__(self,surname,age):
        super().__init__(surname)
        self.age = age
        
    def fullName(self,name):
        print("Child full name is",name,self.surname)
        pass
        
        
p = Parent("Patidar")
c = Child(p.surname,14)
p.fullName("Pushpendra")
c.fullName("Anand")