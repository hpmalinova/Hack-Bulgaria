from bill import Bill
from batchBill import BatchBill

class CashDesk:
	def __init__(self):
		self.__dict = {} # bill: how many times we have it

	def get_dict(self):
		return self.__dict

	def __add_to_dict(self, bill):
		if bill in self.__dict:
			self.__dict[bill] += 1
		else:
			self.__dict[bill] = 1

	def take_money(self, money):	
		if isinstance(money, Bill):
			self.__add_to_dict(money)
		elif isinstance(money, BatchBill):
			for bill in money:
				self.__add_to_dict(bill)

	def total(self):
		total_sum = 0	
	
		for bill in self.__dict:
			total_sum += int(bill) * self.__dict[bill]

		return total_sum	
		
	def __str__(self):
		return self.__get_dict_as_string_in_asc_order()

	def inspect(self):
		print(self.__inspect_helper())

	def __inspect_helper(self):
		result = f'We have a total of {self.total()}$ in the desk\n'
		result += 'We have the following count of bills, sorted in ascending order:'
		result += self.__get_dict_as_string_in_asc_order()

		return result	

	def __get_dict_as_string_in_asc_order(self):
		result = ''

		for bill in sorted(self.__dict):
			result += bill.get_str_value() + ' bills: ' + str(self.__dict[bill]) + '\n'
		
		return result