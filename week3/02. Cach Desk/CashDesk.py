from Bill import Bill
from BatchBill import BatchBill

class CashDesk:
	def __init__(self):
		self.dict = {} # bill: how many times we have it

	def add(self, item):
		if item in self.dict:
			self.dict[item] += 1
			print(self.dict)
		else:
			self.dict[item] = 1
			print(self.dict)

	def take_money(self, money):	
		if isinstance(money, Bill):
			print('a')
			add(self, money)
			print(self.dict)
		elif isinstance(money, BatchBill):
			print('b')
			for bill in BatchBill:
				add(self, bill)
			print(self.dict)


	def __str__(self):
		result = ''
		print(self.dict)
		for key in self.dict.keys():
			result.append(key)			
		return result	

if __name__ == '__main__':
	values = [10, 20, 50, 100, 100, 100]
	bills = [Bill(value) for value in values]

	batch = BatchBill(bills)

	desk = CashDesk()

	desk.take_money(Bill(10))
	#desk.take_money(batch)
	print(desk)