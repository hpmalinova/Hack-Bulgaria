def get_letters(word):
	letters = {} #letter: number of times
	for letter in word:
		if letter.lower() in letters.keys():
			letters[letter.lower()] += 1
		else:
			letters[letter.lower()] = 1
	return letters		

def anagrams(word1, word2):
	if len(word1) != len(word2) or get_letters(word1) != get_letters(word2):
		return "NOT ANAGRAMS"
	else:
		return "ANAGRAMS"	
'''
print(anagrams("SILENT", "listen")) #True
print(anagrams("TOP_CODER", "COTO_PRODE")) #False
print(anagrams("TOP_CODER", "COTO_PRDE")) #True
'''

def is_credit_card_valid(number):
	digits = [int(i) for i in str(number)]
	for i in range(1, len(digits) - 1, 2):
		digits[i] = sum([int(i) for i in str(digits[i]*2)])
	return sum(digits) % 10 == 0
'''
print(is_credit_card_valid(79927398713)) # True
print(is_credit_card_valid(79927398715)) # False	
'''

def find_primes(n):
	primes = [True for i in range(n + 1)]

	p = 2
	while p * p <= n:
		if primes[p] == True:
			for i in range(p * p, n + 1, p):
				primes[i] = False
		p += 1
	return [i for i in range(2, n + 1) if primes[i] == True]

def goldbach(n):
	if n % 2 != 0:
		return False

	primes = find_primes(n)
	result = []

	i = 0
	while n - primes[i] >= n // 2:
		if n - primes[i] in primes:
			result.append((primes[i], n - primes[i]))
		i +=1 

	return result
'''
print(goldbach(4))   # [(2,2)]
print(goldbach(6))   # [(3,3)]
print(goldbach(8))   # [(3,5)]
print(goldbach(10))  # [(3,7), (5,5)]
print(goldbach(100)) # [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
'''

def is_valid(row, col, m):
	return row >= 0 and row < len(m) and col >= 0 and col < len(m[0]) 

def reduce_value(row, col, m, target):
	result = m[row][col] - target
	return result if result >= 0 else 0

def sum_after_bombing(row, col, m):
	target = m[row][col]
	
	if is_valid(row - 1, col, m):
		m[row - 1][col] = reduce_value(row - 1, col, m, target) # up
	if is_valid(row + 1, col, m):
		m[row + 1][col] = reduce_value(row + 1, col, m, target) # down
	if is_valid(row, col - 1, m):
		m[row][col - 1] = reduce_value(row, col - 1, m, target) # left
	if is_valid(row, col + 1, m):
		m[row][col + 1] = reduce_value(row, col + 1, m, target) # right
	if is_valid(row - 1, col - 1, m):
		m[row - 1][col - 1] = reduce_value(row - 1, col - 1, m, target) # upper left
	if is_valid(row - 1, col + 1, m):
		m[row - 1][col + 1] = reduce_value(row - 1, col + 1, m, target) # upper right
	if is_valid(row + 1, col - 1, m):
		m[row + 1][col - 1] = reduce_value(row + 1, col - 1, m, target) # lower left
	if is_valid(row + 1, col + 1, m):
		m[row + 1][col + 1] = reduce_value(row + 1, col + 1, m, target) # lower right

	sum_matrix = 0	
	for row in m:
		sum_matrix += sum(row)
	
	return sum_matrix


import copy

def matrix_bombing_plan(m):
	rows = len(m)
	columns = len(m[0])
	
	result = {}
	for row in range(rows):
		for col in range(columns):
			result[(row, col)] = sum_after_bombing(row, col, copy.deepcopy(m))

	return result

print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))