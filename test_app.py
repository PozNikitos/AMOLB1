import unittest
from app import add

class TestAddition(unittest.TestCase):
    def test_addition_1(self):
        self.assertEqual(add(1, 2), 3)

    def test_addition_2(self):
        self.assertNotEqual(add(1, 2), 5)

    def test_addition_3(self):
        self.assertEqual(add(-1, 1), 0)

    def test_addition_4(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
