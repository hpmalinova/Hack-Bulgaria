import unittest
from utils import Utils

class TestGetNormalFormOfMonomial(unittest.TestCase):
	def test_when_there_is_only_coeff(self):
		monomial = '5'

		expected = '5x^0'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_coeff_is_missing(self):
		monomial = 'x^3'

		expected = '1x^3'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_coeff_is_negative_one(self):
		monomial = '-x^3'

		expected = '-1x^3'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_coeff_is_negative_number(self):
		monomial = '-5x^3'

		expected = '-5x^3'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_coeff_is_positive_number(self):
		monomial = '5x^3'

		expected = '5x^3'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_power_is_missing(self):
		monomial = '2x'

		expected = '2x^1'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_power_is_negative_number(self):
		monomial = '5x^-3'

		expected = '5x^-3'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

	def test_when_power_is_positive_number(self):
		monomial = '5x^3'

		expected = '5x^3'

		self.assertEqual(Utils.get_normal_form_of_monomial(monomial), expected)

class TestConvertToNormalForm(unittest.TestCase):
	def test_when_first_monomial_is_negative(self):
		polynomial = '-3x^2+2x+5'

		expected = '-3x^2+2x^1+5x^0'

		self.assertEqual(Utils.convert_to_normal_form(polynomial), expected)

	def test_when_all_monomials_are_negative(self):
		polynomial = '-3x^2-2x-5'

		expected = '-3x^2-2x^1-5x^0'

		self.assertEqual(Utils.convert_to_normal_form(polynomial), expected)

	def test_when_monomials_are_shuffled(self):
		polynomial = '5+2x+3x^2'

		expected = '5x^0+2x^1+3x^2'

		self.assertEqual(Utils.convert_to_normal_form(polynomial), expected)

	def test_when_polynomial_is_empty(self):
		polynomial = ''

		expected = ''

		self.assertEqual(Utils.convert_to_normal_form(polynomial), expected)

	def test_when_polynomial_has_only_one_monomial(self):
		polynomial = '-2'

		expected = '-2x^0'

		self.assertEqual(Utils.convert_to_normal_form(polynomial), expected)

	def test_when_polynomial_has_empty_monomial(self):
		polynomial = '5x^2+0x-0'

		expected = '5x^2+0x^1-0x^0'

		self.assertEqual(Utils.convert_to_normal_form(polynomial), expected)

if __name__ == '__main__':
	unittest.main()		