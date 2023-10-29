from validations import Validations
from abc import ABC, abstractmethod

class LibraryOperation(ABC):
    @abstractmethod
    def search_books(self, title):
        pass

    @abstractmethod
    def borrow_book(self, book, borrower):
        pass

    @abstractmethod
    def return_book(self, book, borrower):
        pass

class BookType(ABC):
    @abstractmethod
    def get_book_type(self):
        pass

class Fiction(BookType):
    def get_book_type(self):
        return "Fiction"

class NonFiction(BookType):
    def get_book_type(self):
        return "Non-Fiction"

class Book:
    def __init__(self, title, author, publication_date, book_type):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.book_type = book_type

    def __str__(self):
        return f"{self.title} by {self.author}"

class Borrower:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.borrowing_history = []

    def borrow_book(self, book, librarian):
        librarian.borrow_book(book, self)
        self.borrowing_history.append(book)

    def return_book(self, book, librarian):
        librarian.return_book(book, self)
        self.borrowing_history.remove(book)

    def view_borrowing_history(self):
        return [str(book) for book in self.borrowing_history]

class Librarian(LibraryOperation):
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

    def search_books(self, title):
        # Implement book search logic here, for now returning a sample book
        return [Book("Sample Book", "Sample Author", "2023-01-01", Fiction())]

    def borrow_book(self, book, borrower):
        # Implement book borrowing logic here
        pass

    def return_book(self, book, borrower):
        # Implement book return logic here
        pass

# Create instances

librarian = Librarian("Librarian Name", "librarian@example.com")
borrower = Borrower("Borrower Name", "borrower@example.com")

# Search for books
books = librarian.search_books("Sample Book")
if books:
    book_to_borrow = books[0]
    borrower.borrow_book(book_to_borrow, librarian)

# View borrowing history
history = borrower.view_borrowing_history()
for book in history:
    print(book)


librarian = Librarian("Librarian Name", "librarian@example.com")
borrower = Borrower("Borrower Name", "borrower@example.com")

books = librarian.search_books("Sample Book")
if books:
    book_to_borrow = books[0]
    borrower.borrow_book(book_to_borrow, librarian)

history = borrower.view_borrowing_history()
for book in history:
    print(book)
