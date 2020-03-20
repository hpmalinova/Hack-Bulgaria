def sum_of_digits(n):
	if n < 0:
		n = -1 * n
	sum = 0
	while n > 0:
		sum += n % 10
		n = n // 10
	return sum

# print(sum_of_digits(55))

def count_digits(n):
	digits = 0;
	if n == 0:
		return 1
	while n >= 1:
		digits += 1
		n = n // 10
	return digits

# print(count_digits(5555))

def to_digits(n):
	x = count_digits(n)
	my_list = [0 for i in range(x)]
	size = 0
	while x > 0:
		x -= 1
		my_list[size] = n // pow(10, x)
		size += 1
		n = n % pow(10,x)
	return my_list

# print (to_digits(1971273))	

def to_number(digits):
	length = len(digits)
	number = 0;
	for i in range(0, length):
		number = 10*number + digits[i]
	return number

# print(to_number([5,6,1,2]))

def fact(n):
	if n <= 1:
		return 1
	res = n * fact(n-1)
	return res

def fact_digits(n):
	res = 0
	while n > 0:
		last_digit = n % 10 	
		res += fact(last_digit)
		n = n // 10
	return res

# print(fact_digits(999))

def palindrome(object):
	string = str(object)
	for i in range(0, len(string) // 2):
		if string[i] != string[len(string) - 1 - i]:
			return False
	return True

# print(palindrome(121))
# print(palindrome(456))
# print(palindrome('kapak'))
# print(palindrome('baba'))

def count_vowels(str):
	#vowels = {'a', 'A', 'E', 'e', 'O', 'o', 'I', 'i', 'U', 'u', 'Y', 'y'}
	vowels = {'a', 'e', 'o', 'i', 'u', 'y'}
	vowels_number = 0;
	for i in range(0, len(str)):
		if str[i] in vowels or str[i].lower() in vowels:
			vowels_number += 1
	return vowels_number

# print(count_vowels('A nice day to code!'))

def count_consonants(str):
	consonants = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'}
	consonants_number = 0;
	for i in range(0, len(str)):
		if str[i] in consonants or str[i].lower() in consonants:
			consonants_number += 1
	return consonants_number

# print(count_consonants('A nice day to Code!'))

def count_letters(str, v_or_c):
	letters = {}
	letters_number = 0;
	if v_or_c == 'v':
		letters = {'a', 'e', 'o', 'i', 'u', 'y'}
	else: 
		letters = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'}
	for i in range(0, len(str)):
		if str[i] in letters or str[i].lower() in letters:
			letters_number += 1
	return letters_number

# print(count_letters('A nice day to code!', 'v'))
# print(count_letters('A nice day to code!', 'c'))

def char_histogram(str):
	dictionary = {}
	for i in range(0, len(str)):
		if not str[i] in dictionary:
			dictionary[str[i]] = 1
		else:
			dictionary[str[i]] += 1
	return dictionary

# print(char_histogram('Python!'))

def sum_matrix(matrix):
	sumM = 0
	for i in range(0,len(matrix)):
		for j in range(0, len(matrix[i])):
			sumM += matrix[i][j]
	return sumM

# print(sum_matrix([[1,2,3],[5,4]]))
# print(sum_matrix([[1,2,3],[0,0]]))

def nan_expand(times):
	if times < 1:
		return ''
	result = 'Not a NaN'
	while times > 1:
		result = 'Not a ' + result
		times -=1 
	return result

# print(nan_expand(3))

import math

def prime_factorization(n):
	dictionary = {}
	i = 2
	max_i = n // 2 + 1
	while i < max_i:
		if n % i == 0:
			if not i in dictionary:
				dictionary[i] = 1
			else:
				dictionary[i] += 1
			n = n / i
		else:
			i +=1	
	if not dictionary:
		dictionary[n] = 1		 
	result = [(p,a) for p, a in dictionary.items()]
	return result

# print(prime_factorization(10))
# print(prime_factorization(1000))
# print(prime_factorization(89))

def group(lst):
	if not lst:
		return []

	result = []	
	curN = lst[0]
	toAdd = []
	for i in range(len(lst)):
		if curN == lst[i]:
			toAdd.append(curN)
		else:
			curN = lst[i]
			result.append(toAdd)
			toAdd = [curN]	
	if toAdd:
		result.append(toAdd)

	return result

# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3, 5]))
# print(group([]))

def max_consecutive(items):
	groupOfEqualElements = group(items)
	if not groupOfEqualElements:
		return 0
	maxSub = len(groupOfEqualElements[0])
	for i in range(1, len(groupOfEqualElements)):
		curSub = len(groupOfEqualElements[i])
		if curSub > maxSub:
			maxSub = curSub	

	return maxSub

# print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
# print(max_consecutive([]))
# print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))

def contains_word(word, text):
	return text.count(word) + text[::-1].count(word)


def word_counter(matrix, word):	
	word = input('Enter word:')
	size = input('Enter matrix size (format NxM): ')
	n = int(size.split(' ')[0])
	m = int(size.split(' ')[1])
	if len(word) > min([n,m]):
		return 'Invalid number of rows or columns'

	matrix = []
	rows_input = 0
	print('Enter matrix: ')
	while rows_input < n:
		row_input = input()
		row = row_input.strip().split(' ')
		if len(row) != m
			return 'Wrong input'
		
		matrix.append(row.split(' '))
		rows_input += 1

		word_occurances = 0

		#rows
		for row in matrix:
			#if contains_word(word, row):
			#	word_occurances += 1
			word_occurances += contains_word(word,''.join(row)

		#columns
		for i in range(m):
			column = []
			for row in matrix:
				column.append(row[i])
			word_occurances += contains_word(word, ''.join(column))

		#diagonals
		for c in range(n+m-1):
			diagonal = []
			for i in range(n):
				for j in range(m):
					if i + j == c:
						diagonal.append(matrix[i][j])
			word_occurances += contains_word(word, ''.join(diagonal))

		for c in range(1 - m, n):
			diagonal = []
			for i in range(n):
				for j in reversed(range(m)):
					if j - i == c
					diagonal.append(matrix[i][j])

print(word_counter([['i','v','a','n'], ['e','v','n','h']], 'ivan'))	
print(word_counter([['i','v','a','n'], ['e','v','n','h'], ['n','a','v','i']], 'ivan'))	