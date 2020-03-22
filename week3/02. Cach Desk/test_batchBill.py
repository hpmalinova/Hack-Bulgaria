import unittest
from bill import Bill
from batchBill import BatchBill

class TestBatchBill(unittest.TestCase):
	def test_len_of_batch(self):
		bills = [Bill(5), Bill(10), Bill(15)]

		batchBill = BatchBill(bills)

		expected_len = 3

		self.assertEqual(len(batchBill), expected_len)

	def test_total_sum_of_bills_when_no_bills(self):
		bills = []
		batchBill = BatchBill(bills)

		expected_sum = 0

		self.assertEqual(batchBill.total(), expected_sum)	

	def test_total_sum_of_bills(self):
		bills = [Bill(5), Bill(10), Bill(15)]
		batch = BatchBill(bills)

		expected_sum = 30

		self.assertEqual(batch.total(), expected_sum)	

	def test_iterable(self):
		values = [10, 20]
		bills = [Bill(value) for value in values]
		batch = BatchBill(bills)
		
		expected_result = 'A 10$ bill. A 20$ bill. '

		result = ''
		for bill in batch:
			result += str(bill) + '. '
		
		self.assertEqual(result, expected_result)

if __name__ == '__main__':
	unittest.main()	
