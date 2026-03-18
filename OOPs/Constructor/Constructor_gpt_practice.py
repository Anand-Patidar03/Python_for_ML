## PROBLEM 1

# class Employee:
    
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
        
#     def bonus(self):
#         if(self.salary > 50000):
#             self.salary *= 1.1
#         else:
#             self.salary *= 1.05
            
#         return self.salary
            
# emp = Employee("Anand",10000000)
# print("Salary of this employee after bonus is :",emp.bonus())


## PROBLEM 2

# class Book:
    
#     def __init__(self,title,price):
#         self.title = title
#         self.price = price
        
#     def apply_discount(self):
#         discount = 0
#         if(self.price >= 700):
#             discount = 20
#         elif(self.price >= 500 and self.price < 700):
#             discount = 10
#         elif(self.price >= 300 and self.price < 500):
#             discount = 5
#         else:
#             discount = 0
            
#         self.price *= (100-discount)/100.0
#         return self.price
        

# book1 = Book("TPOM",600)
# book2 = Book("HTWFAIP",750)
# book3 = Book("Bramhcharya",400)
# book4 = Book("Handbook",100)

# print("Price is ",book1.apply_discount())
# print("Price is ",book2.apply_discount())
# print("Price is ",book3.apply_discount())
# print("Price is ",book4.apply_discount())


# PROBLEM 3

# class Cart:
    
#     def __init__(self):
#         self.items = []
        
#     def add_items(self,name,price):
#         item = {}
#         item["name"] = name
#         item["price"] = price
#         self.items.append(item)
        
#     def remove_item(self,name):
#         for item in self.items:
#             if(item["name"] == name):
#                 self.items.remove(item)
        
#     def total_price(self):
#         summ = sum(map(lambda x : x['price'] , self.items))
#         return summ
    
# dic = {}      
# cart1 = Cart()

# cart1.add_items("Pen",10)
# cart1.add_items("Notebook",100)
# cart1.add_items("Keyboard",1000)
# cart1.add_items("Bottle",150)
# cart1.add_items("Ear-Phone",1800)

# cart1.remove_item("Bottle")

# print("Total price of cart is : ",cart1.total_price())

# print(cart1.items)
  
   
# PROBLEM 4

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self,book_name):
        
        for book in self.books:
            if book['name'] == book_name:
                book['stock'] += 1
                return 
        else:
                new_book = {
                    "name": book_name,
                    "stock": 1
                }
                self.books.append(new_book)
                return
                
            
        
    def issue_book(self,book_name):
        for book in self.books:
            if book['name'] == book_name and book['stock'] > 0:
                print("Book issued to you !")
                book['stock'] -= 1
                return 
        else :
                print("Book is out of stock Sorry!")
                
                
book1 = Library()

book1.add_book("TPOM")
book1.add_book("Brahm")
book1.add_book("BG")
book1.add_book("TPOM")
book1.add_book("Brahm")

print(book1.books)

book1.issue_book("BG")
book1.issue_book("BG")
book1.issue_book("Brahm")