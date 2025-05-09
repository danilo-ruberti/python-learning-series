import json
import os

def save_books_to_file(filename, book_list):
    """Save the list of books to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(book_list, f, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")

def load_books_from_file(filename):
    """Load the list of books from a JSON file if it exists."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading file: {e}")
        return []
