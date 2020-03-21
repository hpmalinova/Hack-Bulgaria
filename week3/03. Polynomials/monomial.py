class Monomial:
	def __init__(self, coeff, power): # int: coeff, power
		self.__coeff = coeff
		self.__power = power

	def find_derivative(self):
		# [0.x^n]' = [n.x^0]' = 0'
		if self.__coeff == 0 or self.__power == 0: 
			return Monomial(0, 0)

		# [n.x^1]' = n
		if self.__power == 1:
			return Monomial(self.__coeff, 0)

		#f(x) = c * x^n --> [c, n]
		#f'(x) = n * c * x^(n - 1) --> [n*c, n-1]	
		return Monomial(self.__power * self.__coeff, self.__power - 1)

	def __str__(self):
		return self.__convert_to_string()

	def __repr__(self):
		return self.__convert_to_string()

	def __convert_to_string(self):
		if self.__coeff == 0:
			return ''

		monomial = self.__add_coeff()
		monomial += self.__add_power()

		return monomial			

	def __add_coeff(self):
		monomial = '' 

		if self.__coeff == -1:
			monomial += '-'
		elif self.__coeff != 1: 
			monomial += str(self.__coeff)

		return monomial

	def __add_power(self):
		monomial = ''

		if self.__power != 0:
			monomial += 'x'
			if self.__power != 1:
				monomial += '^' + str(self.__power)

		return monomial		

	def get_coeff(self):
		return self.__coeff

	def get_power(self):
		return self.__power

	def __eq__(self, other):
		if self.__coeff == 0 and other.__coeff == 0:
			return True 
		return self.__coeff == other.__coeff and self.__power == other.__power	

	def __lt__(self, other):
		return self.__power < other.__power	