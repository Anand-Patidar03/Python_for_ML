class Animal:
     
    def __init__(self,name,species):
         self.name = name
         self.species = species
         
    # def __init__(self,age,legs):
    #     self.age = age
    #     self.legs = legs
    
    # def __init__(self,name,species,age,legs):
    #     self.age = age
    #     self.legs = legs
    #     self.name = name
    #     self.species = species
        
    def sound(self,voice):
        print("This animal sounds as {}".format(voice))
        
dog1 = Animal("Dog","mammals")                  #second constructor override first constructor
# dog2 = Animal("Dog","mammals",15,4)              #perfectly fine

# print(dog1)
# cat = Animal(15,4)
# print (cat)



##  POSITIONAL ARGUMENT USE :- 
## Not a good practice but a approach

class Janvar:
    
    def __new__(Janvar):                    # this __new__ call __init__ internally but 
                                            # if we write __new__ explicitly then __init__
                                            # will not be called

        print("Constructor made using new ")
        
    
    def __init__(self,*args):
        if(len(args) == 1):
            self.name = args[0]
        elif(len(args)==2):
            self.name = args[0]
            self.species = args[1]
        elif(len(args)==3):
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]
            
    def sound(self,voice):
        return "This Janvar sounds like {}".format(voice)
    
    @staticmethod   #if you dont want to give self as argument
    def pet():
        return "This animal can be pet"
    
    
# dog1 = Janvar("Dog")
# dog2 = Janvar("Dog","mammals")
dog3 = Janvar("Dog","mammals",15)

# print(dog1.name)
# print(dog2.species)
# print(dog3.age)

# print(dog1.sound("Bark"))

print(dog3.pet())
    
          