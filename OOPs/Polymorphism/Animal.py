class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")
        

def make_sound(animal):
    animal.sound()
    
dog = Dog()
cat = Cat()  
make_sound(dog)
make_sound(cat)


# animals = [Dog(), Cat()]


# for a in animals:
#     a.sound()


# dog.sound()
# cat.sound()
