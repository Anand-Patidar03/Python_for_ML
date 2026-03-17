# class Car:
#     pass

# car1 = Car()
# car2 = Car()

# # print(car1)

# print(dir(car1))

#### Classes are real-world entities or objects
#### Atributes are the properties of the classes
#### Methods are the actions of the classes

class Car:
    
    ## Constructor in Python
    def __init__(self,windows,tyres,engine,seats):
        self.windows = windows
        self.tyres = tyres
        self.engine = engine
        self.seats = seats
        
    def self_driving(self,engine):        # this function's own parameter
        print("The type of self driving car is {} ".format(engine))
        
car1 = Car(4,4,"Petrol",5)
# print(car1)
print("The number of windows in car1 is {}".format(car1.windows))
print("The number of tyres in car1 is {}".format(car1.tyres))
print("The engine in car1 is {} engine".format(car1.engine))
print("The number of seats in car1 is {}".format(car1.seats))

car1.self_driving("Electric")
        