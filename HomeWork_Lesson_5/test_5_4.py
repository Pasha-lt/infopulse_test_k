from unittest import TestCase
from program_for_test import is_year_leap, triangle, hw_4_2_3
from hw_5_2 import ITEmployee


class TestHW4(TestCase):
    def test_is_year_leap(self):
        self.assertEqual(is_year_leap(2000), True)
        self.assertEqual(is_year_leap(1999), False)

    def test_triangle(self):
        self.assertEqual(triangle(3, 4, 5), True)
        self.assertEqual(triangle(0, 4, 0), False)

    def test_hw_4_2_3(self):
        self.assertEqual(hw_4_2_3(3, 4, 5), 'Versatile triangle')
        self.assertEqual(hw_4_2_3(0, 4, 0), 'Not a tringle')
        self.assertEqual(hw_4_2_3(2, 3, 2), 'Isosceles triangle')
        self.assertEqual(hw_4_2_3(3, 3, 3), 'Equilateral triangle')
        self.assertEqual(hw_4_2_3(6, 18, 21), 'Versatile triangle')



