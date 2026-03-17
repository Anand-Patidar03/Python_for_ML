class Order:
    
    def __init__(self,user,product,price):
        self.user = user
        self.product = product
        self.price = price
        
    def to_dict(self):
        return {
        "user": self.user,
        "product": self.product,
        "price": self.price
    }
        
    def display_order(self):
        # print("The user {} ordered product {} of price {}".format(self.user,self.product,self.price))
        print(self.to_dict())
        
class Store:
    
    def __init__(self):
        self.orders = []
        
        
    def add_orders(self,order1):
        
        self.orders.append(order1)
        
    
order1 = Order("Anand","Moblie",21000)
order2 = Order("Vijay","Laptop",70000)
order3 = Order("Ajay","Cricket bat",5000)
order4 = Order("Ram","Bow",1001)
store1 = Store()

store1.add_orders(order1)
store1.add_orders(order2)
store1.add_orders(order3)
store1.add_orders(order4)


# print(store1.orders)
order1.display_order()
order2.display_order()
order3.display_order()
order4.display_order()


        