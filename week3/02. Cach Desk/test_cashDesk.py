import unittest
from bill import Bill
from batchBill import BatchBill
from cashDesk import CashDesk

class TestTakeMoney(unittest.TestCase):
	def test_take_no_bill(self):
		bill = None
		desk = CashDesk()
		expected_dict = {}

		desk.take_money(bill)

		self.assertEqual(desk.get_dict(), expected_dict)

	def test_take_one_bill(self):
		bill = Bill(10)
		desk = CashDesk()
		expected_dict = {Bill(10): 1}

		desk.take_money(bill)

		self.assertEqual(desk.get_dict(), expected_dict)

	def test_take_more_equal_bills_consecutively(self):
		bill1 = Bill(10)
		bill2 = Bill(10)
		desk = CashDesk()
		expected_dict = {Bill(10): 2}

		desk.take_money(bill1)
		desk.take_money(bill2)

		self.assertEqual(desk.get_dict(), expected_dict)

	def test_take_more_different_bills_consecutively(self):
		bill1 = Bill(10)
		bill2 = Bill(15)
		desk = CashDesk()
		expected_dict = {Bill(10): 1, Bill(15): 1}

		desk.take_money(bill1)
		desk.take_money(bill2)

		self.assertEqual(desk.get_dict(), expected_dict)

	def test_take_batch(self):
		batch = BatchBill([Bill(5), Bill(10), Bill(15)])
		desk = CashDesk()
		expected_dict = {Bill(5): 1, Bill(10): 1, Bill(15): 1}

		desk.take_money(batch)

		self.assertEqual(desk.get_dict(), expected_dict)

	def test_take_bill_and_batch(self):
		bill = Bill(5)
		batch = BatchBill([Bill(5), Bill(10), Bill(15)])
		desk = CashDesk()
		expected_dict = {Bill(5): 2, Bill(10): 1, Bill(15): 1}

		desk.take_money(bill)
		desk.take_money(batch)

		self.assertEqual(desk.get_dict(), expected_dict)

class TestTotalMoney(unittest.TestCase):
	def test_total_money_when_desk_is_empty(self):
		desk = CashDesk()
		expected = 0

		result = desk.total()

		self.assertEqual(result, expected)

	def test_total_money(self):
		batch = BatchBill([Bill(5), Bill(10), Bill(15), Bill(10)])
		desk = CashDesk()	
		desk.take_money(batch)
		expected = 40

		result = desk.total()

		self.assertEqual(result, expected)

class TestPrintMethods(unittest.TestCase):
	def test_when_bills_are_unordered(self):
		batch = BatchBill([Bill(25), Bill(10), Bill(15), Bill(10)])
		desk = CashDesk()	
		desk.take_money(batch)
		expected = '10$ bills: 2\n15$ bills: 1\n25$ bills: 1\n'
		
		self.assertEqual(str(desk), expected)

if __name__ == '__main__':
	unittest.main()	