from monomial import Monomial

class Polynomial:
	def __init__(self, str_polynomial):
		self.__str_polynomial = str_polynomial

		normal_form_of_monomials = self.convert_to_normal_form(str_polynomial)		

		self.__polynomial = []
		for monomial in normal_form_of_monomials:
			monomial = monomial.split('x^')
			self.__polynomial.append(Monomial(int(monomial[0]), int(monomial[1])))

	def __str__(self):
		return self.__str_polynomial

	def __repr__(self):
		return self.__str_polynomial

	def __getitem__(self, index):
		return self.__polynomial[index]	

	def find_derivative(self):
		result = ''

		for monomial in self.__polynomial:
			to_add == str(monomial.find_derivative())
			if to_add != '':
				if to_add[0] == '-' and result != '':
					result = result[:len(result) - 1]
				result += to_add
				result += '+'

		if result[-1] == '+':
			result = result[:len(result) - 1]

		if result == '':
			result = '0'	
				
		return result

	def convert_to_normal_form(self, str_polynomial):
		str_polynomial = self.add_plus_before_minus(str_polynomial)
		list_of_monomials = str_polynomial.split('+')
		
		normal_form_of_monomials = []
		
		for monomial in list_of_monomials:
			normal_form_of_monomial = ''

			if 'x' not in monomial:
				normal_form_of_monomial = self.add_x(monomial)
			else:
				monomial = monomial.split('x')

				normal_form_of_monomial = self.add_coeff(monomial[0])
				
				normal_form_of_monomial += 'x'
				
				normal_form_of_monomial += self.add_power(monomial[1])

			normal_form_of_monomials.append(normal_form_of_monomial)		

		return normal_form_of_monomials		

	def add_plus_before_minus(self, str_polynomial):
		result = ''
		
		for i in range(len(str_polynomial)):
			if str_polynomial[i] == '-':
				result += '+'
			result += str_polynomial[i]

		return result

	def add_x(self, str_monomial):
		return str_monomial + 'x^0'

	def add_coeff(self, monomial_coeff):
		normal_form_of_monomial = ''

		if monomial_coeff == '-':
			normal_form_of_monomial += '-1'
		elif monomial_coeff == '':
			normal_form_of_monomial += '1'
		else:
			normal_form_of_monomial += monomial_coeff

		return normal_form_of_monomial	

	def add_power(self, monomial_power):
		normal_form_of_monomial = ''
		if '^' in monomial_power:
			normal_form_of_monomial += monomial_power
		else:
			normal_form_of_monomial += '^1'

		return normal_form_of_monomial	