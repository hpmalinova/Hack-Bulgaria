import math
from simplify_fraction import ensure_fractions, simplify_fraction

# fraction is tuple where:
# fraction[0] = nominator; fraction[1] = denominator
# fractions is list of tuples: (nominator, denominator)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple_numbers(fractions): # return lcm
	cur_lcm = fractions[0][1]

	for fraction in fractions:
		cur_lcm = lcm(cur_lcm, fraction[1])

	return cur_lcm

def convert_to_common_denominator(fractions):
	lcm = lcm_multiple_numbers(fractions)
	new_fractions = []

	for fraction in fractions:
		new_fractions.append((fraction[0] * lcm // fraction[1], lcm))
			
	return new_fractions

def sum_of_fractions(fractions): # returns fraction
	fractions_with_common_denominator = convert_to_common_denominator(fractions)

	sum_of_nominators = 0

	for fraction in fractions_with_common_denominator:
		sum_of_nominators += fraction[0]

	return (sum_of_nominators, fractions_with_common_denominator[0][1])

def collect_fractions(fractions):
	if not fractions:
		return 0 
	
	valid_fractions = ensure_fractions(fractions)
	
	sum_of_fractions = sum_of_fractions(valid_fractions)

	return simplify_fraction(sum_of_fractions)