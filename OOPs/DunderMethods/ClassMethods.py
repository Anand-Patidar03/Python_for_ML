class Student:
    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    

student = Student()

print(student.get_count())
print(student.get_count())
print(student.get_count())