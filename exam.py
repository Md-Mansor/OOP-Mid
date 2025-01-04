class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is currently not available.")

    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"The book '{self.title}' has been returned.")
        else:
            print(f"The book '{self.title}' was not borrowed.")

    def view_book_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {'Available' if self.availability else 'Not Available'}")


class Library:
    def __init__(self):
        self.__book_list = []

    def entry_book(self, book_id, title, author):
        book = Book(book_id, title, author, True)
        self.__book_list.append(book)

    def borrow_book(self, book_id):
        for book in self.__book_list:
            if book.book_id == book_id:
                book.borrow_book()
                return
        print(f"Book with ID {book_id} not found.")

    def return_book(self, book_id):
        for book in self.__book_list:
            if book.book_id == book_id:
                book.return_book()
                return
        print(f"Book with ID {book_id} not found.")

    def get_books(self):
        return self.__book_list


lib = Library()
lib.entry_book(1, "Book A", "Author A")
lib.entry_book(2, "Book B", "Author B")
lib.entry_book(3, "Book C", "Author C")

print("Viewing Book Info for Book ID 2:")
for book in lib.get_books():  # Accessing the private list via the get_books method
    if book.book_id == 2:
        book.view_book_info()

print("\nBorrowing Book with ID 2:")
lib.borrow_book(2)

print("\nViewing Book Info for Book ID 2 again:")
for book in lib.get_books():  # Accessing the private list via the get_books method
    if book.book_id == 2:
        book.view_book_info()
