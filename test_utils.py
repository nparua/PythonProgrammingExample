import unittest
from utils import fizz_buzz

class TestUtils(unittest.TestCase):
	def test_fizz_buzz(self):
		self.assertEqual(fizz_buzz(3), "fizz")
		self.assertEqual(fizz_buzz(4), 4)
		self.assertEqual(fizz_buzz(7), "buzz")
		self.assertEqual(fizz_buzz(21), "fizzbuzz")
		self.assertRaises(ValueError, fizz_buzz, 'X')
		self.assertRaises(ValueError, fizz_buzz, 7.8)
