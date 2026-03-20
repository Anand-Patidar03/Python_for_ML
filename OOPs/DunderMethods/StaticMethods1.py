class MyClass:
    
    @staticmethod
    def my_method():
        print("Hello from static method")
        
        
# c = MyClass()
# c.my_method()



class MathUtils:
    
    @staticmethod
    def add(a, b):
        return a + b

# print(MathUtils.add(2, 3))


class User:
    
    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

print(User.is_valid_email("test@gmail.com"))