"""
Sample test
"""
from django.test import SimpleTestCase

from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc modul"""
    def test_add_numbers(self):
        """Test adding number"""
        res = calc.add(5,6)
        self.assertEqual(res,11)


    def test_subsctract_numbers(self):
        """Test substracting numbers"""
        res = calc.subtract(10,15)
        self.assertEqual(res,5)