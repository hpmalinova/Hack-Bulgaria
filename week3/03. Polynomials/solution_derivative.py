import sys

from polynomial import Polynomial

def main():
	str_polynomial = sys.argv[1]
	polynomial = Polynomial(str_polynomial)
	print(polynomial.find_derivative())

if __name__ == '__main__':
	main()