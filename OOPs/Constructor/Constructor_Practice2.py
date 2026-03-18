class Train:
    
    def __init__(self,seats,price):
        self.seats = seats
        self.price = price
    
    def book_ticket(self):
        if self.seats > 0:
            self.seats -= 1
            return "Ticket booked successfully"
        else:
            return "Sorry, no seats available"
        
        
    def get_status(self):
        print("Number of seats available are {}".format(self.seats))
        
    def fare(self):
        print("Ticket of this train is of {} rupees".format(self.price))
        
        
tr = Train(100,200)

tr.get_status()
tr.book_ticket()
tr.fare()
tr.get_status()