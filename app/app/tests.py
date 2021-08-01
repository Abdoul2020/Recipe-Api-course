from django.test import TestCase

from app.calc import add,subtract

class calcTest(TestCase):

    def test_add_numbers(self):
        """Test that add two numbers together"""
        self.assertEqual(add(3,8),11)

    def test_substract_numbers(self):
        """Substract two numbers"""
        self.assertEqual(subtract(2,7),5)

