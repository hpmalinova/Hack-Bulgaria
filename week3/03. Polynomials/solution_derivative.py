import sys

from monomial import Monomial
from polynomial import Polynomial

def main():
	str_polynomial = sys.argv[1] #str
	mon = Monomial(-1, 1)
	print(mon)
	#polynomial = Polynomial(str_polynomial)
	#result = polynomial.find_derivative()
	#print(f'The derivative of f(x) = {str_polynomial} is: {result}')

if __name__ == '__main__':
	main()