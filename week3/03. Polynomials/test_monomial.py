import unittest
from monomial import Monomial

class TestMonomial(unittest.TestCase):
	def test_convert_monomial_of_power_greater_than_1_to_tuple(self):
		monomial = Monomial('7x^5') # 7x^5

		expected_coeff = 7
		expected_power = 5

		self.assertEqual(monomial.get_coeff(), expected_coeff)	
		self.assertEqual(monomial.get_power(), expected_power)

	def test_convert_monomial_of_power_1_to_tuple(self):
		monomial = Monomial('7x') # 7x^1

		expected_coeff = 7
		expected_power = 1

		self.assertEqual(monomial.get_coeff(), expected_coeff)	
		self.assertEqual(monomial.get_power(), expected_power)

	def test_convert_monomial_of_power_0_to_tuple(self):
		monomial = Monomial('7') # 7x^0

		expected_coeff = 7
		expected_power = 0

		self.assertEqual(monomial.get_coeff(), expected_coeff)	
		self.assertEqual(monomial.get_power(), expected_power)	

	def test_convert_monomial_of_power_greater_than_1_to_tuple_with_negative_power(self):
		monomial = Monomial('7x^-5') # 7x^5

		expected_coeff = 7
		expected_power = -5

		self.assertEqual(monomial.get_coeff(), expected_coeff)	
		self.assertEqual(monomial.get_power(), expected_power)

	def test_convert_monomial_of_power_1_to_tuple_with_negative_coeff(self):
		monomial = Monomial('-7x') # 7x^1

		expected_coeff = -7
		expected_power = 1

		self.assertEqual(monomial.get_coeff(), expected_coeff)	
		self.assertEqual(monomial.get_power(), expected_power)

	def test_convert_monomial_of_power_0_to_tuple_with_negative_coeff(self):
		monomial = Monomial('-7') # 7x^0

		expected_coeff = -7
		expected_power = 0

		self.assertEqual(monomial.get_coeff(), expected_coeff)	
		self.assertEqual(monomial.get_power(), expected_power)	

if __name__ == '__main__':
	unittest.main()	