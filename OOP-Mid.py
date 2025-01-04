class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"The book '{self.__title}' has been borrowed.")
        else:
            print(f"The book '{self.__title}' is currently not available.")

    def return_book(self):
        if not self.__availability:
            self.__availability = True
            print(f"The book '{self.__title}' has been returned.")
        else:
            print(f"The book '{self.__title}' was not borrowed.")

    def view_book_info(self):
        print(f"Book ID: {self.__book_id}")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Availability: {'Available' if self.__availability else 'Not Available'}")


class Library:
    def __init__(self):
        self.__book_list = []

    def entry_book(self, book_id, title, author):
        book = Book(book_id, title, author, True)
        self.__book_list.append(book)

    def view_books(self):
        for book in self.__book_list:
            book.view_book_info()

    def borrow_book(self, book_id):
        for book in self.__book_list:
            if book.__book_id == book_id:
                book.borrow_book()

    def return_book(self, book_id):
        for book in self.__book_list:
            if book.__book_id() == book_id:
                book.return_book()
                return


library = Library()
library.entry_book(1, "1984", "George Orwell")
library.entry_book(2, "To Kill a Mockingbird", "Harper Lee")

while True:
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")
    choice = int(input("Inter Your Choice: "))
    if choice == 1:
        library.view_books()
    elif choice == 2:
        Id = int(input("Enter Book Id For Borrow: "))
        library.borrow_book(Id)
    elif choice == 3:
        Id = int(input("Enter Book Id For Return: "))
        library.return_book(Id)
    elif choice == 4:
        print("Exit From Library")
        break
    else:
        print("Invalid Choice. Please Try Again")
