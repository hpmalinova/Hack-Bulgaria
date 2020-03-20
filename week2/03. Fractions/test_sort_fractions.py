import unittest

from sort_fractions import (sort_fractions, get_nominators,
	create_map_of_new_positions, remove_duplicates, order_fractions)

class TestGetNominators(unittest.TestCase): #get invalid TODO
	def test_get_nominator(self):
		fractions = [(1, 5), (-7, 12), (5, 2), (-3, 10)]
		expected = [12, -35, 150, -18]

		result = get_nominators(fractions)

		self.assertEqual(result, expected)

class TestCreateMap(unittest.TestCase):
	def test_creating_map_of_nominators_with_no_repeating_elements(self):
		nominators = [1, 7, 3, 5]
		expected = {1: [0], 7: [1], 3: [2], 5: [3]}

		result = create_map_of_new_positions(nominators)

		self.assertEqual(result, expected)

	def test_creating_map_of_nominators_with_repeating_elements(self):
		nominators = [1, 7, 3, 5, 7, 1, 0, 7]
		expected = {1: [0, 5], 7: [1, 4, 7], 3: [2], 5: [3], 0: [6]}

		result = create_map_of_new_positions(nominators)

		self.assertEqual(result, expected)

class TestOrderFractions(unittest.TestCase):
	def test_order_fractions(self):
		original_fractions = [(3, 5), (4, 4), (2, 1), (6, 20), (6, 10)]
		new_positions = {12: [0, 4], 20: [1], 40: [2], 6: [3]}
		sorted_nominators_with_no_repeating_elements = [6, 12, 20, 40]
		expected = [(6, 20), (3, 5), (6, 10), (4, 4), (2, 1)]

		result = order_fractions(original_fractions, new_positions, 
			sorted_nominators_with_no_repeating_elements)

		self.assertEqual(result, expected)

class TestRemoveDuplicates(unittest.TestCase):
	def test_when_no_duplicates(self):
		nominators = [6, 12, 4, 5]
		expected = [6, 12, 4, 5]

		result = remove_duplicates(nominators)

		self.assertEqual(result, expected)

	def test_when_duplicates(self):
		nominators = [6, 12, 4, 6, 4, 5, 12, 12]
		expected = [6, 12, 4, 5]
		
		result = remove_duplicates(nominators)

		self.assertEqual(result, expected)	

class TestSortFractions(unittest.TestCase):
	def test_when_some_fractions_are_invalid(self):
		fractions = [(3, 5), (7, 0), (4, 4), (5, 0), (2, 1), (6, 20), (6, 10)]
		
		expected = [(6, 20), (3, 5), (6, 10), (4, 4), (2, 1)]

		result = sort_fractions(fractions)

		self.assertEqual(result, expected)

	def test_when_some_fractions_are_negative(self):
		fractions = [(3, -5), (-6, 20), (-6, -10)]
		
		expected = [(-3, 5), (-6, 20), (6, 10)]

		result = sort_fractions(fractions)

		self.assertEqual(result, expected)	

if __name__ == '__main__':
	unittest.main()