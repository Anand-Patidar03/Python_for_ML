# class A:
#     def fun(self):
#         print("Inside Class A")
        
        
# class B:
#     def fun(self):
#         print("Inside Class B")
        
        
# class C(B,A):
#     def fun1(self):
#         super().fun()
        

# a = A()
# b = B()
# c = C()
# c.fun1()

class A:
    def fun(self):
        print("A")

class B(A):
    def fun(self):
        print("B")
        super().fun()

class C(A):
    def fun(self):
        print("C")
        super().fun()

class D(B, C):
    def fun(self):
        print("D")
        super().fun()
   
   
# a = A()
# b = B()
# c = C()     
d = D()
d.fun()