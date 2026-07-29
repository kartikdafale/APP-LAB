# Library Management System using Object-Oriented Programming

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display_book(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Status  : {status}")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # Display all books
    def display_books(self):
        if len(self.books) == 0:
            print("Library is empty.")
        else:
            print("\n------ Library Books ------")
            for book in self.books:
                book.display_book()

    # Search book by ID
    def search_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    # Issue book
    def issue_book(self, book_id):
        book = self.search_book(book_id)

        if book:
            if not book.is_issued:
                book.is_issued = True
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
        else:
            print("Book not found.")

    # Return book
    def return_book(self, book_id):
        book = self.search_book(book_id)

        if book:
            if book.is_issued:
                book.is_issued = False
                print("Book returned successfully.")
            else:
                print("Book was not issued.")
        else:
            print("Book not found.")


# ---------------- Main Program ---------------- #

library = Library()

while True:
    print("\n====== Library Management System ======")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        book_id = int(input("Enter Book ID to search: "))
        book = library.search_book(book_id)

        if book:
            print("\nBook Found")
            book.display_book()
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = int(input("Enter Book ID to issue: "))
        library.issue_book(book_id)

    elif choice == "5":
        book_id = int(input("Enter Book ID to return: "))
        library.return_book(book_id)

    elif choice == "6":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice! Please try again.")
