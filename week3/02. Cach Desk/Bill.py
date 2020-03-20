class Bill:
	def __init__(self, amount):
		if not isinstance(amount, int):
			raise TypeError('Wrong type')
		elif amount < 0:
			raise ValueError('The Amount should be >= 0') 
		else:
			self.amount = amount

	def __str__(self):
		return f'A {self.amount}$ bill'

	def __repr__(self):
		return f'A {self.amount}$ bill'
 	
	def __int__(self):
		return self.amount

	def __eq__(self, other):
		return self.amount == other.amount
	

if __name__ == '__main__':
	b = Bill(5)
	print(b)