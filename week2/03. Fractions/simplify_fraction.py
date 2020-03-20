import math

# fraction is tuple where:
# fraction[0] = nominator; fraction[1] = denominator

def simplify_fraction(fraction):

	fraction = ensure_fraction(fraction)

	gcd = math.gcd(fraction[0], fraction[1])

	return (fraction[0] // gcd, fraction[1] // gcd)

def ensure_fraction(fraction):
	nominator, denominator = fraction

	if denominator == 0:
		raise ZeroDivisionError('Invalid fraction. You can`t divide by zero!')
	
	if nominator == 0:
		return (0, 1)
	
	if (nominator < 0 and denominator < 0) or denominator < 0:
		nominator *= -1
		denominator *= -1

	return (nominator, denominator)

def ensure_fractions(fractions):
	valid_fractions = []

	for fraction in fractions:
		try:
			valid_fractions.append(ensure_fraction(fraction))
		except ZeroDivisionError as e:
			print('Invalid fraction: will be ignored')

	return valid_fractions 