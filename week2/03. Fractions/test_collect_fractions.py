import unittest

from collect_fractions import (lcm, lcm_multiple_numbers,
	convert_to_common_denominator, sum_of_fractions, collect_fractions)

class TestLCM(unittest.TestCase):
	def test_lcm_of_two_fractions(self):
		fractions = [(3, 8), (16, 12)]
		expected = 24

		self.assertEqual(lcm(fractions[0][1], fractions[1][1]), expected)

	def test_lcm_with_odd_number_of_fractions(self):
		fractions = [(3, 24), (16, 12), (7, 8)]
		
		result = lcm_multiple_numbers(fractions)
		expected = 24

		self.assertEqual(result, expected)

	def test_lcm_with_even_number_of_fractions(self):
		fractions = [(3, 8), (16, 40), (7, 24), (15, 12)]
		
		result = lcm_multiple_numbers(fractions)
		expected = 120

		self.assertEqual(result, expected)

	def test_lcm_of_negative_fractions(self):
		fractions = [(-3, 8), (16, 12), (-26, 5)]
		
		result = lcm_multiple_numbers(fractions)
		expected = 120

		self.assertEqual(result, expected)

class TestConvertToCommonDenominator(unittest.TestCase):
	def test_when_all_fractions_have_equal_denominator(self):
		fractions = [(3, 8), (7, 8), (15, 8), (5, 8)]
		expected = [(3, 8), (7, 8), (15, 8), (5, 8)]

		result = convert_to_common_denominator(fractions)

		self.assertEqual(result, expected)

	def test_when_some_fractions_have_different_denominator(self):
		fractions = [(5, 5), (7, 2), (13, 2), (15, 5)]
		expected = [(10, 10), (35, 10), (65, 10), (30, 10)]

		result = convert_to_common_denominator(fractions)

		self.assertEqual(result, expected)

	def test_when_all_fractions_have_different_denominator(self):
		fractions = [(3, 45), (7, 25), (15, 5), (5, 9)]
		expected = [(15, 225), (63, 225), (675, 225), (125, 225)] # 878 / 225

		result = convert_to_common_denominator(fractions)

		self.assertEqual(result, expected)

class TestSumOfFractions(unittest.TestCase):
	def test_sum_with_positive_numbers(self):
		fractions = [(15, 225), (63, 225), (675, 225), (125, 225)]
		expected = (878, 225)

		result = sum_of_fractions(fractions)

		self.assertEqual(result, expected)

	def test_sum_with_negative_numbers(self):
		fractions = [(15, 225), (-63, 225), (675, 225), (-125, 225)]
		expected = (502, 225)

		result = sum_of_fractions(fractions)

		self.assertEqual(result, expected)

class TestCollectFractions(unittest.TestCase):
	def test_when_no_fractions_then_return_0(self):
		fractions = []
		expected = 0

		result = collect_fractions(fractions)

		self.assertEqual(result, expected)

	def test_when_one_fraction_equals_0_then_return_sum_of_others(self):
		fractions = [(15, 5), (0, 1), (5, 5)]
		expected = (4, 1)

		result = collect_fractions(fractions)

		self.assertEqual(result, expected)

	def test_collect_fractions(self):
		fractions = [(5, 5), (-7, 12), (13, -2), (15, 10)]
		
		expected = (-55, 12)

		result = collect_fractions(fractions)

		self.assertEqual(result, expected)

if __name__ == '__main__':
	unittest.main()