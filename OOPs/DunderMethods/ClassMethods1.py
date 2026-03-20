class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school(cls):
        return cls.school
    
    @classmethod
    def get_printStmt1(cls):
        print("This is class method")
        
    
    def get_printStmt2(self):
        print("This is non class method")
        
        
    def get_printStmt3():
        print("This is also non class method number 2")

#to access class method
print(Student.get_school())
Student.get_printStmt1()

#to access non class method
obj = Student("anand")
obj.get_printStmt2()
Student.get_printStmt3()