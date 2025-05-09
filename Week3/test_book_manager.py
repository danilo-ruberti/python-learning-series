import unittest
from book_manager import add_book, update_status, filter_books

class TestBookManager(unittest.TestCase):
    def setUp(self):
        # Runs before each test
        self.books = []

    def test_add_book(self):
        add_book(self.books, "1984", "George Orwell", "want to read")
        self.assertEqual(len(self.books), 1)
        self.assertEqual(self.books[0]["title"], "1984")

        # Test duplicate
        add_book(self.books, "1984", "George Orwell", "want to read")
        self.assertEqual(len(self.books), 1)  # should not add again

    def test_update_status(self):
        add_book(self.books, "Dune", "Frank Herbert", "reading")
        update_status(self.books, "Dune", "read")
        self.assertEqual(self.books[0]["status"], "read")

    def test_filter_books(self):
        add_book(self.books, "Book A", "Author X", "read")
        add_book(self.books, "Book B", "Author Y", "want to read")
        read_books = filter_books(self.books, "read")
        self.assertEqual(len(read_books), 1)
        self.assertEqual(read_books[0]["title"], "Book A")

if __name__ == "__main__":
    unittest.main()