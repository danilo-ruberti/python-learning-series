

def add_book(book_list, title, author, status):
    """Add a book to the list if it's not already present."""
    book = {"title": title.strip(), "author": author.strip(), "status": status.strip().lower()}
    if book not in book_list:
        book_list.append(book)
        print(f"Added: {title} by {author}")
    else:
        print("This book already exists in your library.")

def update_status(book_list, title, new_status):
    """Update the reading status of a book by title."""
    found = False
    for book in book_list:
        if book["title"].lower() == title.strip().lower():
            book["status"] = new_status.strip().lower()
            print(f"Updated status of '{title}' to {new_status}")
            found = True
            break
    if not found:
        print("Book not found.")

def filter_books(book_list, status):
    """Return books matching the given status."""
    return [book for book in book_list if book["status"] == status.strip().lower()]

def print_books(book_list):
    """Prints out the list of books nicely formatted."""
    if not book_list:
        print("No books in your library.")
        return
    for i, book in enumerate(book_list, 1):
        print(f"{i}. {book['title']} by {book['author']} — Status: {book['status']}\n")