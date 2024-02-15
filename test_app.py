# test_app.py
import unittest
from app import add

class TestAddFunction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(1,  2),  3)
        self.assertNotEqual(add(1,  2),  5)
        self.assertEqual(add(-1,  1),  0)
        self.assertEqual(add(0,  0),  0)

if __name__ == "__main__":
    unittest.main()
