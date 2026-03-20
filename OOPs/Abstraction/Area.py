from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        print("Partially completed")
        pass
    
    def fun(self):
        print("Shape Demo Function ")


class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def fun(self):
        print("Circle demo function")

# s = Shape()      # cannot instantiate abstract class , do using child 
c = Circle(5)
print(c.area())
c.fun()
# print(s.fun())