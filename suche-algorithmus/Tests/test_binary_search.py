import unittest

class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        array = [1, 3, 5, 7, 9]
        target = 5
        self.assertEqual((array, target), 2)

    def test_element_not_found(self):
        array = [1, 3, 5, 7, 9]
        target = 4
        self.assertEqual((array, target), -1)

if __name__ == "__main__":
    unittest.main()
