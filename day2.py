class Book :
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("The title of the book is",self.title,"and the author is",self.author)
    

class IssuedBook(Book):
    def __init__(self, title, author,issued_to,issued_date):
        super().__init__(title, author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_book_details(self):
        super().display_book_details()
        print("The book is issued in",self.issued_date,"to",self.issued_to)
       
        


obj=IssuedBook("Harry Potter and the Philosopher’s Stone","J.K. Rowling","student","03-02-2026")
obj.display_book_details()