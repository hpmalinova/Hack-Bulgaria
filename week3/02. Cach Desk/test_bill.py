import unittest
from bill import Bill

class TestBill(unittest.TestCase):
	def test_init_with_wrong_type(self):
		my_exc = None

		try:
			Bill('abv')
		except TypeError as err:
			my_exc = err
				
		self.assertTrue(my_exc)	

	def test_init_with_amount_less_than_0(self):
		my_exc = None

		try:
			Bill(-5)
		except ValueError as err:
			my_exc = err
				
		self.assertTrue(my_exc)			

	def test_int_repr(self):
		bill = Bill(10)

		expected = 10

		self.assertEqual(int(bill), expected)

	def test_str_repr(self):
		bill = Bill(10)

		expected = 'A 10$ bill'

		self.assertEqual(str(bill), expected)

	def test_when_bills_are_equal(self):
		bill1 = Bill(5)
		bill2 = Bill(5)

		result = bill1 == bill2

		self.assertTrue(result)

	def test_when_bills_are_not_equal(self):
		bill1 = Bill(5)
		bill2 = Bill(15)

		result = bill1 == bill2

		self.assertFalse(result)

if __name__ == '__main__':
	unittest.main()	