# Import functions from your modules
from book_manager import add_book, update_status, filter_books, print_books
from file_utils import save_books_to_file, load_books_from_file


# Initialize the book list
books = []

# Load existing books from file (if any)
books = load_books_from_file("books.json")

while True:
    print("Welcome to Your Library Tracker!")
    print("1. Add a new book")
    print("2. Update book status")
    print("3. Show all books")
    print("4. Filter books by status")
    print("5. Save and exit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        status = input("Enter status (want to read / reading / read): ")
        add_book(books, title, author, status)

    elif choice == "2":
        title = input("Enter book title to update: ")
        new_status = input("Enter new status (want to read / reading / read): ")
        update_status(books, title, new_status)

    elif choice == "3":
        print_books(books)

    elif choice == "4":
        status = input("Enter status to filter by (want to read / reading / read): ")
        filtered = filter_books(books, status)
        print_books(filtered)

    elif choice == "5":
        save_books_to_file("books.json", books)
        print("Library saved. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")