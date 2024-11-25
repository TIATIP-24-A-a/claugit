import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        # Testet, ob ein vorhandenes Element korrekt gefunden wird
        array = [1, 3, 5, 7, 9]
        target = 5
        self.assertEqual(binary_search(array, target), 2)

    def test_element_not_found(self):
        # Testet, ob ein nicht vorhandenes Element korrekt nicht gefunden wird
        array = [1, 3, 5, 7, 9]
        target = 4
        self.assertEqual(binary_search(array, target), -1)

if __name__ == "__main__":
    unittest.main()
