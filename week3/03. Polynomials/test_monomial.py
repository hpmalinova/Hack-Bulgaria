import unittest
from monomial import Monomial

class TestPrintCoeffMonomial(unittest.TestCase):
	def test_when_coeff_equals_1_then_dont_print_it(self):
		monomial = Monomial(1, 5)

		expected = 'x^5'

		self.assertEqual(str(monomial), expected)

	def test_when_coeff_equals_negative_1_then_print_only_minus(self):
		monomial = Monomial(-1, 5)

		expected = '-x^5'

		self.assertEqual(str(monomial), expected)

	def test_when_coeff_equals_0_then_return_empty_string(self):
		monomial = Monomial(0, 5)

		expected = ''

		self.assertEqual(str(monomial), expected)

	def test_when_coeff_is_greater_than_one_then_print_it(self):
		monomial = Monomial(5, 10)

		expected = '5x^10'

		self.assertEqual(str(monomial), expected)

	def test_when_coeff_is_less_than_negative_one_then_print_it(self):
		monomial = Monomial(-5, 10)

		expected = '-5x^10'

		self.assertEqual(str(monomial), expected)

class TestPrintPowerMonomial(unittest.TestCase):
	def test_when_power_is_zero_then_print_only_coeff(self):
		monomial = Monomial(5, 0)

		expected = '5'

		self.assertEqual(str(monomial), expected)

	def test_when_power_is_one_then_print_only_x(self):
		monomial = Monomial(5, 1)

		expected = '5x'

		self.assertEqual(str(monomial), expected)

	def test_when_power_is_greater_than_one_then_print_it(self):
		monomial = Monomial(5, 5)

		expected = '5x^5'

		self.assertEqual(str(monomial), expected)

	def test_when_power_is_less_than_zero_then_print_it(self):
		monomial = Monomial(5, -5)

		expected = '5x^-5'

		self.assertEqual(str(monomial), expected)

class TestFindDerivative(unittest.TestCase):
	def test_when_coeff_equals_zero_then_return_empty_monomial(self):
		monomial = Monomial(0, 3)

		expected = Monomial(0, 0)

		self.assertEqual(monomial.find_derivative(), expected)		

	def test_when_power_equals_zero_then_return_empty_monomial(self):
		monomial = Monomial(5, 0)

		expected = Monomial(0, 0)

		self.assertEqual(monomial.find_derivative(), expected)	

	def test_when_power_equals_one_then_return_the_same_coeff_and_power_0(self):
		monomial = Monomial(5, 1)

		expected = Monomial(5, 0)

		self.assertEqual(monomial.find_derivative(), expected)			

	def test_when_positive_coeff_and_power_then_return_derivative(self):
		monomial = Monomial(3, 2)

		expected = Monomial(6, 1)

		self.assertEqual(monomial.find_derivative(), expected)	

	def test_when_negative_coeff_and_power_then_return_derivative(self):
		monomial = Monomial(-3, -2)

		expected = Monomial(6, -3)

		self.assertEqual(monomial.find_derivative(), expected)						

if __name__ == '__main__':
	unittest.main()	