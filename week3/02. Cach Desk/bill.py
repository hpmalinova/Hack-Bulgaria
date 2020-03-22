class Bill:
	def __init__(self, amount): # int: amount
		if not isinstance(amount, int):
			raise TypeError('Wrong type')
		elif amount < 0:
			raise ValueError('The Amount should be >= 0') 
		else:
			self.__amount = amount

	def get_amount(self):
		return self.__amount		

	def __add__(self, other):
		return Bill(self.__amount + other.__amount)

	def __str__(self):
		return f'A {self.__amount}$ bill'

	def __repr__(self):
		return f'A {self.__amount}$ bill'
 	
	def __int__(self):
		return self.__amount

	def __eq__(self, other):
		if type(other) is type(self):
			return self.__amount == other.__amount
		return False

	def __hash__(self):
		return hash(self.__amount)	