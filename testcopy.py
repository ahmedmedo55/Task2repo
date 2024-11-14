# test_calculator.py

import unittest
from areaFunction import AreaCircle

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.area_of_circle = AreaCircle()

    def test_area(self):
        # Test area of circle rule functionality
        result = self.area_of_circle(10)
        self.assertEqual(result, 314)


if __name__ == '__main__':
    unittest.main()
