import unittest

from simplify_fraction import ensure_fraction, ensure_fractions, simplify_fraction

# numerator

class TestEnsureFraction(unittest.TestCase):
	def test_when_denominator_equals_zero_then_raise_exception(self):
		fraction = (5, 0)
		my_exc = None

		try:
			ensure_fraction(fraction)
		except Exception as e:
			my_exc = e

		self.assertIsNotNone(my_exc)
		self.assertEqual(str(my_exc), 'Invalid fraction. You can`t divide by zero!')

	def test_when_nominator_is_negative_and_denominator_is_non_negative_then_return_negative_fraction(self):
		fraction = (-27, 3)
		expected = (-27, 3)

		result = ensure_fraction(fraction)

		self.assertEqual(result, expected)

	def test_when_nominator_is_non_negative_and_denominator_is_negative_then_return_negative_fraction(self):
		fraction = (27, -3)
		expected = (-27, 3)

		result = ensure_fraction(fraction)

		self.assertEqual(result, expected)

	def test_when_both_nominator_and_denominator_are_negative_then_return_positive_fraction(self):
		fraction = (-27, -3)
		expected = (27, 3)

		result = ensure_fraction(fraction)

		self.assertEqual(result, expected)

class TestEnsureFractions(unittest.TestCase):
	def test_when_one_denominator_equals_zero_then_dont_include_it(self):
		fractions = [(5, 2), (7, 0), (3, 3)]
		expected = [(5, 2), (3, 3)]

		result = ensure_fractions(fractions)

		self.assertEqual(result, expected)

	def test_when_some_denominators_equal_zero_then_dont_include_them(self):
		fractions = [(5, 2), (7, 0), (3, 3), (5, 0)]
		expected = [(5, 2), (3, 3)]

		result = ensure_fractions(fractions)

		self.assertEqual(result, expected)

	def test_when_no_denominator_equals_zero_then_include_all(self):
		fractions = [(5, 2), (3, 3)]
		expected = [(5, 2), (3, 3)]

		result = ensure_fractions(fractions)

		self.assertEqual(result, expected)

class TestSimplifyFraction(unittest.TestCase):
	def test_when_nominator_is_bigger_than_denominator_and_unsimplifiable_then_return_the_same(self):
		fraction = (77, 8)
		expected = (77, 8)

		result = simplify_fraction(fraction)

		self.assertEqual(result, expected)

	def test_when_nominator_is_smaller_than_denominator_and_unsimplifiable_then_return_the_same(self):
		fraction = (9, 44)
		expected = (9, 44)
		
		result = simplify_fraction(fraction)

		self.assertEqual(result, expected)

	def test_when_nominator_is_bigger_than_denominator_and_simplifiable_then_simplify(self):
		fraction = (108, 12)
		expected = (9, 1)
		
		result = simplify_fraction(fraction)

		self.assertEqual(result, expected)

	def test_when_nominator_is_smaller_than_denominator_and_simplifiable_then_simplify(self):
		fraction = (20, 35)
		expected = (4, 7)
		
		result = simplify_fraction(fraction)

		self.assertEqual(result, expected)

	def test_when_nominator_equals_denominator_then_return_1(self):
		fraction = (19, 19)
		expected = (1, 1)

		result = simplify_fraction(fraction)

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()