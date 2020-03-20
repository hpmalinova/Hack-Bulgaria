import unittest
from cancellation import validate_conditions, ensure_conditions, group_conditions, 
	get_cancellation_policy, sort_conditions
from datetime import datetime, timedelta

class TestValidateConditions(unittest.TestCase):
	def test_validation_passes_with_valid_conditions(self):
		conditions = [
			{'hours': 10, 'percent': 10},
			{'percent': 100}
		]		

		validate_conditions(conditions)

	def test_raises_exception_if_all_conditions_have_hours(self):
		conditions = [
			{'hours': 10, 'percent': 10}
		]
		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid conditions')

	def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
		conditions = [
			{'hours': 10, 'percent': 10},
			{'percent': 100},
			{'percent' : 100}
		]
		
		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err
		
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Invalid conditions')	
	

	def test_raises_exception_if_hours_bigger_than_24(self):
		conditions = [
			{'hours': 72, 'percent': 10},
			{'percent': 100}
		]

		exc = None

		try:
			validate_conditions(conditions)
		except Exception as err:
			exc = err
		
		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Hours cannot be > 24')	


class TestEnsureConditions(unittest.TestCase):
	def test_ensure_all_conditions_have_hours(self):
		conditions = [
			{'hours': 10, 'percent': 10},
			{'percent': 100}
		]
		ensure_conditions(conditions)
		#self.assertTrue(all(['hours' in condition.keys() for condition in conditions]))
		self.assertEqual(conditions[0]['hours'] == 10)
		self.assertEqual(conditions[1]['hours'] == 0)
		# add samo poslednoto hours da e 0

class TestGroupConditions(unittest.TestCase):
	def test_group_conditions_with_two_elements(self):
		conditions = [
			{ 'hours': 10, 'percent': 20 }, # 24 - 11 
			{ 'hours': 0, 'percent': 50 } # 10 - 0
		]

		expected = [(24, 12), (12, 6), (6, 0)]

		self.assertEqual(group_conditions(conditions), expected)

	def test_group_conditions(self):
		conditions = [
			{ 'hours': 24, 'percent': 10 }, 
			{ 'hours': 12, 'percent': 50 }, 
			{ 'hours': 6, 'percent': 80 }, 
			{ 'hours': 0, 'percent': 100 }
		]

		expected = [(24, 12), (12, 6), (6, 0)]

		self.assertEqual(group_conditions(conditions), expected)

class TestGetCancellationPolicy(unittest.TestCase):
	def test_cancellation_fee_with_only_one_condition(self):
		conditions = [{ 'hours': 0, 'percent': 50 }]
		price = 100
		now = datetime.now()
		start = now + timedelta(hours = 100)

		result = get_cancellation_policy(conditions, price, start, now)
		self.assertEqual(result, 50) #nz

class TestSortConditions(unittest.TestCase):
	def test_conditions_are_sorted_in_descendiong_order(self):
		conditions = [{ 'hours': 12, 'percent': 50 }, { 'hours': 0, 'percent': 100 }, 
		{ 'hours': 6, 'percent': 80 }, { 'hours': 24, 'percent': 10 }]
		
		result = sort_conditions(conditions)

		#expected
		#self.assertEqual(result, 50) #nz
#class TestPairConditions(unittest.TestCase):
#	booking_start = datetime.now()
#	now = booking_start - timedelta(hours=10)
#	res = get_current_condiiton(conditions, booking_start, now)


if __name__ == '__main__':
	unittest.main()