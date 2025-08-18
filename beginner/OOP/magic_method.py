

class Book:
    """
    Explaining dunder methods
    """
    def __init__(self,title,author,num_page):
        self.title = title
        self.author = author
        self.num_page = num_page
    
    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self,other):
        return self.num_page < other.num_page
    
    def __gt__(self,other):
        return self.num_page > other.num_page
    
    def __add__(self,other):
        return self.num_page + other.num_page
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_page":
            return self.num_page
        else:
            return f"key {key} not found"
book1 = Book("The Hobbit","J.R.R Tokein",310)
book2 = Book("Harry Potter","J.K Rowling",223)
book3 = Book("The Lion King","Arsalan",820)
book4 = Book("The Lion King","Arsalan",820)


print(book3["author"])
    
    
