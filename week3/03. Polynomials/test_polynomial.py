import unittest
from monomial import Monomial
from polynomial import Polynomial
from utils import Utils

class TestCreatePolynomial(unittest.TestCase):
	def test_create_polynomial(self):
		polynomial = Polynomial('5x^2-x-7')

		expected_monomials = [Monomial(5, 2), Monomial(-1, 1), Monomial(-7, 0)]
		
		self.assertEqual(polynomial.get_polynomial(), expected_monomials)	

	def test_create_empty_polynomial(self):
		polynomial = Polynomial('0x')

		expected_monomials = []
		
		self.assertEqual(polynomial.get_polynomial(), expected_monomials)	

	def test_create_polynomial_with_empty_monomials(self):
		polynomial = Polynomial('5x+0x+9+0x')

		expected_monomials = [Monomial(5, 1), Monomial(9, 0)]
		
		self.assertEqual(polynomial.get_polynomial(), expected_monomials)	

class TestFindDerivative(unittest.TestCase):
	def test_find_derivative(self):
		polynomial = Polynomial('5x^2-7x+0')

		expected_derivative = '10x-7'

		self.assertEqual(polynomial.find_derivative(), expected_derivative)

	def test_when_polynomial_is_constant_0(self):
		polynomial = Polynomial('0')

		expected_derivative = '0'

		self.assertEqual(polynomial.find_derivative(), expected_derivative)

	def test_when_polynomial_is_constant(self):
		polynomial = Polynomial('8')

		expected_derivative = '0'

		self.assertEqual(polynomial.find_derivative(), expected_derivative)

	def test_when_polynomial_is_linear_function(self):
		polynomial = Polynomial('-5x-9')

		expected_derivative = '-5'

		self.assertEqual(polynomial.find_derivative(), expected_derivative)

	def test_when_polynomial_is_shuffled(self):
		polynomial = Polynomial('0-5x^2+2x-x^3')

		expected_derivative = '-3x^2-10x+2'

		self.assertEqual(polynomial.find_derivative(), expected_derivative)


if __name__ == '__main__':
	unittest.main()		