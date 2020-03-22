from bill import Bill

class BatchBill:
	def __init__(self, bills): # list of Bills: bills
		self.__bills = bills

	def __len__(self):
		return len(self.__bills)

	def total(self):
		if self.__bills:
			return int(sum(self.__bills, Bill(0)))
		return 0	

	def __getitem__(self, index):
		return self.__bills[index]	