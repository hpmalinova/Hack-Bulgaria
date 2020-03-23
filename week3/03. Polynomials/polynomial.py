from monomial import Monomial
from utils import Utils

class Polynomial:
	def __init__(self, polynomial): # gets string
		self.__str_polynomial = polynomial

		self.__polynomial = []
		self.__add_monomials(self.__get_monomials(polynomial))

	def __get_monomials(self, polynomial):
		normal_form_of_polynomial = Utils.convert_to_normal_form(polynomial)
		normal_form_of_polynomial = Utils.add_plus_before_minus(normal_form_of_polynomial)

		monomials = normal_form_of_polynomial.split('+')

		return monomials

	def __add_monomials(self, monomials):
		for monomial in monomials:
			monomial = monomial.split('x^')

			if monomial[0] != '0':
				self.__polynomial.append(Monomial(int(monomial[0]), int(monomial[1])))
		self.__polynomial.sort(reverse = True)		

	def get_polynomial(self):
		return self.__polynomial		

	def __str__(self):
		return self.__str_polynomial

	def __repr__(self):
		return self.__str_polynomial

	def __getitem__(self, index):
		return self.__polynomial[index]	

	def find_derivative(self):
		result = ''

		for monomial in self.__polynomial:
			to_add = str(monomial.find_derivative())
			result = self.add_to_result(to_add, result)

		if result and result[-1] == '+':
			result = result[:len(result) - 1]

		if not result:
			result = '0'	
				
		return result

	@staticmethod	
	def add_to_result(to_add, result): #TODO TEST
		if to_add != '':
			if to_add[0] == '-' and result:
				result = result[:len(result) - 1]
			result += to_add
			result += '+'

		return result	