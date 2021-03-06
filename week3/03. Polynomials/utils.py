class Utils:
	@classmethod	
	def convert_to_normal_form(cls, polynomial): # gets and returns string
		if polynomial == '':
			return ''

		polynomial = cls.add_plus_before_minus(polynomial)

		monomials = polynomial.split('+')

		return cls.__get_normal_form_of_polynomial(monomials)

	@classmethod
	def __get_normal_form_of_polynomial(cls, monomials):
		normal_form_of_polynomial = ''
		
		for monomial in monomials:
			normal_form_of_monomial = cls.get_normal_form_of_monomial(monomial)

			if normal_form_of_polynomial and cls.__check_if_negative_monomial(normal_form_of_monomial):
				normal_form_of_polynomial = cls.__remove_last_element(normal_form_of_polynomial)

			normal_form_of_polynomial += normal_form_of_monomial
			normal_form_of_polynomial += '+'

		# if last element is '+'	
		if normal_form_of_polynomial and normal_form_of_polynomial[-1] == '+':
			normal_form_of_polynomial = cls.__remove_last_element(normal_form_of_polynomial)

		return normal_form_of_polynomial	

	@classmethod
	def get_normal_form_of_monomial(cls, monomial):
		normal_form = '' 

		if 'x' not in monomial:
			normal_form = monomial + 'x^0'
		else:
			monomial = monomial.split('x')

			normal_form = cls.__add_coeff(monomial[0])
			normal_form += 'x'
			normal_form += cls.__add_power(monomial[1])

		return normal_form	

	@staticmethod		
	def __remove_last_element(string):
		return string[:-1]	

	@staticmethod	
	def __check_if_negative_monomial(monomial):
		return monomial[0] == '-'

	@staticmethod	
	def add_plus_before_minus(string):
		result = ''
		
		for symbol in string:
			if symbol == '-':
				result += '+'
			result += symbol	

		# if first symbol of string was '-'
		if result[0] == '+':
			result = result[1:]	

		return result
	
	@staticmethod
	def __add_coeff(monomial_coeff):
		coeff = ''

		if monomial_coeff == '-':
			coeff += '-1'
		elif monomial_coeff == '':
			coeff += '1'
		else:
			coeff += monomial_coeff

		return coeff	
	
	@staticmethod
	def __add_power(monomial_power):
		power = ''
		
		if '^' in monomial_power:
			power += monomial_power
		else:
			power += '^1'

		return power	