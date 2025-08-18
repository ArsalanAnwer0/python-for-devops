# Class and Objects Practice
class Book:
    title = None
    author = None
    pages = 0
    price = 0

    def __init__(self,title,author,pages,price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    
    def displayInfo(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: {self.price}")

    def priceDiscount(self):
        self.price*=0.8


book_one = Book("Math","Arsalan",5,100)
book_two = Book("Physics","Ali",20,400)
print("Book 1")
book_one.displayInfo()
print("Book 2")
book_two.displayInfo()

print("After discount")

book_one.priceDiscount()
book_one.displayInfo()