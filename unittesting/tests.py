import unittest
from unittesting.models import Book

def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(5, 0), 5)
    
    def test_book(self):
        book = Book(book_name="Django123", book_author="akansha 123", book_description="test description 123", book_status=True)
        self.assertEqual(book.book_name, "Django123")
        self.assertEqual(book.book_author, "akansha 123")
        self.assertEqual(book.book_description, "test description 123")
        self.assertTrue(book.book_status)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)