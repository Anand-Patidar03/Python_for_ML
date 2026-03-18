import math

class Calculator:
    
    def __init__(self,n):
        self.n = n
        
    def sqr(self,n):
        return n*n
    
    def cube(self,n):
        return n*n*n 
    
    def sqrrt(self,n):
        return math.sqrt(n)
    
    
n = int(input("Enter a number : "))
obj = Calculator(n)
print("Square if {} is {}".format(n,obj.sqr(n)))
print("Cube if {} is {}".format(n,obj.cube(n)))
print("Square root if {} is {}".format(n,obj.sqrrt(n)))
        