class Book:
    def __init__(self, id, name, is_available=True):
        self.id = id
        self.name = name
        self.is_available = is_available

class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []  # list of borrowed books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

class Library:
    def __init__(self, member_book_cap):
        self.library_books = []  # all books in library
        self.member_book_cap = member_book_cap

    def add_book(self, book):
        self.library_books.append(book)

    def can_borrow(self, member, book):
        return (len(member.books) < self.member_book_cap and 
                book not in member.books and 
                book.is_available)

    def borrow_book(self, member, book):
        if book not in self.library_books:
            print("Book not in library!")
            return
        if self.can_borrow(member, book):
            member.add_book(book)
            book.is_available = False
            print(f"{member.name} borrowed {book.name}")
        else:
            print("Cannot borrow book (cap reached, already borrowed, or unavailable).")

    def return_book(self, member, book):
        if book in member.books:
            member.remove_book(book)
            book.is_available = True
            print(f"{member.name} returned {book.name}")
        else:
            print("Cannot return book — member does not have it.")
