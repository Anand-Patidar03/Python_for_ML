class Person:
    def __init__(self,name,age):
        self.__name = name   # __name  it is private variable
        self.__age = age    # only use inside class
        
    def display_info(self):
        print(f"This person's name is {self.__name} and age is {self.__age}")
        
person = Person("Anand Patidar",21)

#print(person._Person__name) #not a good practice to access private variable

person.display_info()
