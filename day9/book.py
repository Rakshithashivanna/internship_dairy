class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
    def __str__(self):
        return f"The title of the book is {self.title} and author is {self.author} and the price of the book is {self.price}"

    def __repr__(self):
        return f"Title:{self.title}\nAuthor:{self.author}\nPrice:{self.price} "
    
obj=Book("Harry Potter and the Philosopher’s Stone","J.K. Rowling",500)
print(obj)
obj
print(repr(obj))
