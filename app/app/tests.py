from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc app"""
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        res = calc.subtract(11, 5)
        self.assertEqual(res, 6)
