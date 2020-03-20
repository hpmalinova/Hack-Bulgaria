import math

class Fraction:
	def __init__(self, numerator, denominator):
		assert denominator != 0, 'Zero denominator'
		
		if numerator == 0:
			denominator = 1
	
		if (numerator < 0 and denominator < 0) or denominator < 0:
			numerator *= -1
			denominator *= -1
		
		self.numerator = numerator
		self.denominator = denominator	

	def __str__(self):
		return f'{self.numerator}/{self.denominator}'

	def __eq__(self, other):
		return self.numerator / self.denominator == other.numerator / other.denominator	

	def simplify(self):
		my_gcd = math.gcd(self.numerator, self.denominator)
		
		return Fraction(self.numerator // my_gcd, self.denominator // my_gcd)	

	def __add__(self, other):
		numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
		denominator = self.denominator * other.denominator

		return Fraction(numerator, denominator).simplify()
	