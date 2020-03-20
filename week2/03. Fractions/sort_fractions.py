from simplify_fraction import ensure_fractions
from collect_fractions import convert_to_common_denominator

def sort_fractions(fractions):
	original_fractions = ensure_fractions(fractions)

	nominators = get_nominators(original_fractions) # return list of nominators

	new_positions = create_map_of_new_positions(nominators) # nominator: positions_in_original_list


	# TODO
	sorted_nominators = remove_duplicates(sorted(nominators))

	return order_fractions(original_fractions, new_positions, sorted_nominators)

def get_nominators(fractions):
	fractions_with_common_denominator = convert_to_common_denominator(fractions)

	nominators = []
	
	for fraction in fractions_with_common_denominator:
		nominators.append(fraction[0])

	return nominators

def create_map_of_new_positions(nominators):
	new_positions = {}

	for i in range(0, len(nominators)):
		if not nominators[i] in new_positions: # if not new_positions[nominators[i]]:
			new_positions[nominators[i]] = [i]
		else:
			new_positions[nominators[i]].append(i)

	return new_positions			

def remove_duplicates(sorted_nominators):
	result = []
	for nominator in sorted_nominators:
		if not nominator in result:
			result.append(nominator)

	return result	

def order_fractions(original_fractions, new_positions, sorted_nominators):
	sorted_original_fractions = [] # [(nom1, denom1), (nom2, denom2) .. ]

	for nominator in sorted_nominators:
		for position in new_positions[nominator]:
			sorted_original_fractions.append(original_fractions[position])

	return sorted_original_fractions