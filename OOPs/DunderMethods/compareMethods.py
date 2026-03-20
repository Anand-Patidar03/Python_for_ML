class Demo:
    
    class_var = "I am class variable"
    
    def instance_method(self):
        print("Instance method")
    
    @classmethod
    def class_method(cls):
        print("Class method:", cls.class_var)
    
    @staticmethod
    def static_method():
        print("Static method")
        
        
d = Demo()

d.instance_method()
d.class_method()
d.static_method()

Demo.class_method()