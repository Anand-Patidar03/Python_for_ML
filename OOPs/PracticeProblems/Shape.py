from abc import ABC,abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    def describe(self):
        print("This is of type {} and has area {}".format(type(self).__name__,self.area()))
        
    @staticmethod
    def larger(s1,s2):
        if s1.area() > s2.area():
            print("the Shape s1 has larger area than s2")
            
        elif s1.area() < s2.area():
            print("the Shape s2 has larger area than s1")
            
        else:
            print("the Shape s1 has equal area than s2")
            
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return math.pi*(self.radius*self.radius)
    
    def perimeter(self):
        return 2*math.pi*self.radius
    
    
    
    
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height = height
        self.width = width
        
    def area(self):
        return self.height*self.width
    
    def perimeter(self):
        return 2*(self.height+self.width)
        
   
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2        # Heron's formula
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c     
    
# s1 = Shape()
# s2 = Shape()
c = Circle(4)
r = Rectangle(3,5)
t = Triangle(3,4,5)
print(c)
print(r)
print(t)
print("The area of Circle is {}".format(c.area()))
print("The perimeter of Circle is {}".format(c.perimeter()))
print("The area of Ractangle is {}".format(r.area()))
print("The perimeter of Rectangle is {}".format(r.perimeter()))
print("The area of Triangle is {}".format(t.area()))
print("The perimeter of Triangle is {}".format(t.perimeter()))

Shape.larger(c,r)

c.describe()
r.describe()
t.describe()