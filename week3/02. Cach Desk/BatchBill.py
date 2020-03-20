class BatchBill:
	def __init__(self, bills):
		self.bills = bills

	def __len__(self):
		return len(self.bills)

	def total(self):
		total_sum = 0
		for bill in self.bills:
			total_sum += bill
		return total_sum

	def __getitem__(self, index):
		return self.bills[index]	

from Bill import Bill

if __name__ == '__main__':
	values = [10, 20, 50, 100]
	bills = [Bill(value) for value in values]
	batch = BatchBill(bills)
	for bill in batch:
		print(bill)
	