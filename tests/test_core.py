import unittest
from app.core import greet

class TestCore(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice! Welcome to the app.")

if __name__ == "__main__":
    unittest.main()
