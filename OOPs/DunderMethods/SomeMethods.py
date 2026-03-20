class A:
    def __str__(self):
        return "This is object A"


class B:
    def __repr__(self):
        return "B() object"
    
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = MyList([1,2,3])
print(len(obj)) 

obj1 = A()
print(obj1)

obj2 = B()
print(obj2)