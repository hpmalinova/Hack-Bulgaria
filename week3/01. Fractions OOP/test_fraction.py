import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
	def test_when_denominator_equals_zero_then_raise_exception(self):
		my_exc = None

		try:
			Fraction(1,0)
		except AssertionError as e:
			my_exc = e

		self.assertIsNotNone(my_exc)
		self.assertEqual(str(my_exc), 'Zero denominator')

	def test_when_nominator_is_negative_and_denominator_is_non_negative_then_return_negative_fraction(self):
		fraction = Fraction(-27, 3)

		self.assertEqual(fraction.numerator, -27)
		self.assertEqual(fraction.denominator, 3)

	def test_when_nominator_is_non_negative_and_denominator_is_negative_then_return_negative_fraction(self):
		fraction = Fraction(27, -3)

		self.assertEqual(fraction.numerator, -27)
		self.assertEqual(fraction.denominator, 3)

	def test_when_both_nominator_and_denominator_are_negative_then_return_positive_fraction(self):
		fraction = Fraction(-27, -3)
	
		self.assertEqual(fraction.numerator, 27)
		self.assertEqual(fraction.denominator, 3)

	def test_fraction_string_representation(self):
		fraction1 = Fraction(1, 3)
		fraction2 = Fraction(1, -3)

		self.assertEqual(str(fraction1), '1/3')
		self.assertEqual(str(fraction2), '-1/3')
		
	def test_fraction_equalization_with_equal_numerators_and_denominators(self):
		fraction1 = Fraction(1, 5)
		fraction2 = Fraction(1, 5)

		self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')

	def test_fraction_equalization_with_different_numerators_and_denominators_but_equal_fractions(self):
		fraction1 = Fraction(-2, -5)
		fraction2 = Fraction(10, 25)

		self.assertTrue(fraction1 == fraction2, 'Fractions are not equal')

	def test_fraction_equalization_with_non_equal_fractions(self):
		fraction1 = Fraction(1, 5)
		fraction2 = Fraction(2, 5)

		self.assertFalse(fraction1 == fraction2, 'Fractions are equal')

class TestSimplifyFraction(unittest.TestCase):
	def test_when_numerator_is_different_from_denominator_and_unsimplifiable_then_return_the_same(self):
		fraction = Fraction(77, 8)
		
		simplified_fraction = fraction.simplify()

		self.assertEqual(simplified_fraction.numerator, 77)
		self.assertEqual(simplified_fraction.denominator, 8)

	def test_when_numerator_is_different_from_denominator_and_simplifiable_then_simplify(self):
		fraction = Fraction(20, 35)
		
		simplified_fraction = fraction.simplify()

		self.assertEqual(simplified_fraction.numerator, 4)
		self.assertEqual(simplified_fraction.denominator, 7)

	def test_when_numerator_equals_denominator_then_return_1(self):
		fraction = Fraction(19, 19)
		
		simplified_fraction = fraction.simplify()

		self.assertEqual(simplified_fraction.numerator, 1)
		self.assertEqual(simplified_fraction.denominator, 1)

class TestSumFractions(unittest.TestCase):
	def	test_when_fractions_have_equal_denominator(self):
		fraction1 = Fraction(3, 10)
		fraction2 = Fraction(5, 10)

		result = fraction1 + fraction2 # 4/5

		self.assertEqual(result.numerator, 4)
		self.assertEqual(result.denominator, 5)


	def	test_when_fractions_have_gcd_denominators_equal_to_1(self):
		fraction1 = Fraction(3, 4)
		fraction2 = Fraction(5, 5)

		result = fraction1 + fraction2 # 7/4

		self.assertEqual(result.numerator, 7)
		self.assertEqual(result.denominator, 4)

	def	test_when_fractions_have_gcd_denominators_non_equal_to_1(self):
		fraction1 = Fraction(3, 2)
		fraction2 = Fraction(5, 10)
		result = fraction1 + fraction2 # 2/1

		self.assertEqual(result.numerator, 2)
		self.assertEqual(result.denominator, 1)
	
	def	test_when_sum_more_fractions(self):
		fraction1 = Fraction(3, 2)
		fraction2 = Fraction(5, 10)
		fraction3 = Fraction(9, 3)
		#result = fraction1 + fraction2 + fraction3 # 2/1

		self.assertEqual(result.numerator, 5)
		self.assertEqual(result.denominator, 1)


if __name__ == '__main__':
	unittest.main()	