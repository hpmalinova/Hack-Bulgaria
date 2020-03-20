def closest_to (dist, gas_stations):
	closest_station = 0
	for station in gas_stations:
		if station < dist:
			closest_station = station
		else:
			return closest_station
	return closest_station

def gas_stations(distance, tank_size, stations):
	visited_stations = [] 
	current_distance = 0

	while current_distance <= distance:
		current_distance += tank_size 
		visited_stations.append(closest_to(current_distance, stations))

	return visited_stations
'''
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
# output: [80, 140, 220, 290]
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
# output: [70, 140, 210, 280, 350]
'''

def is_number_balanced(n):
	list_num = [int(x) for x in str(n)]
	length = len(list_num)

	left = list_num[: length // 2]
	right = [] 

	if length % 2 == 0:
		right = list_num[length // 2 : length]
	else:
		right = list_num[length // 2 + 1 : length]

	return sum(left) == sum(right)
'''
print(is_number_balanced(0))
# True
print(is_number_balanced(4518))
# True
print(is_number_balanced(28471))
# False
print(is_number_balanced(1238033))
# True
'''

def check_increasing(seq): # 1 2 3 4 5
	for i in range(len(seq) - 1):
		if seq[i] >= seq[i+1]:
			return False
	return True

def check_decreasing(seq): # 5 4 3 2 1 
	for i in range(len(seq) - 1):
		if seq[i] <= seq[i+1]:
			return False
	return True

def increasing_or_decreasing(seq):
	if check_increasing(seq):
		return "Up!"
	elif check_decreasing(seq):
		return "Down!"
	else:
		return False

'''
print(increasing_or_decreasing([1,2,3,4,5])) # Up!
print(increasing_or_decreasing([5,6,-10]))   # False
print(increasing_or_decreasing([1,1,1,1]))   # False
print(increasing_or_decreasing([9,8,7,6]))   # Down!
'''

def is_palindrome(object):
	return str(object) == str(object)[::-1]

def less(n):
	if n == 0:
		return 9
	else:
		return n - 1

def get_largest_palindrome(n):
	if n == 0:
		return 0

	if n < 0 :
		n *= -1

	if is_palindrome(n) or is_palindrome(n - 1): # change number of digits
		n -= 1

	largest_palindrome = [int(i) for i in str(n)]    
	
	for i in range(len(largest_palindrome) // 2):
		left = largest_palindrome[i]
		end = len(largest_palindrome) - i - 1
		right = largest_palindrome[end]  

		if left < right:
			largest_palindrome[end] = left
		elif left > right: 
			offset = 1
			
			while (largest_palindrome[end - offset] == 0):
				largest_palindrome[end - offset] = less(largest_palindrome[end - offset])
				offset += 1
			largest_palindrome[end - offset] = less(largest_palindrome[end - offset])

			if (i == end - offset): 
					left -= 1

			largest_palindrome[end] = left 

	return int(''.join(str(i) for i in largest_palindrome))

''' 
print(get_largest_palindrome(0)) # 0	
print(get_largest_palindrome(7)) # 6
print(get_largest_palindrome(10)) # 9	
print(get_largest_palindrome(21)) # 11
print(get_largest_palindrome(99)) # 88     
print(get_largest_palindrome(100)) # 99
print(get_largest_palindrome(200)) # 191
print(get_largest_palindrome(-252)) # 242  
print(get_largest_palindrome(203101)) # 202202  
print(get_largest_palindrome(754649)) # 754457
print(get_largest_palindrome(994687)) # 994499

'''

import re

def sum_of_numbers(input_string):
	input_string = input_string.lower()
	print(input_string)
	lst = re.split('[a-z]+', input_string)
	while("" in lst):
		lst.remove("")
	print(lst)	
	return sum([int(i) for i in lst])
'''
print(sum_of_numbers("ab125cd3")) #128
print(sum_of_numbers("ab12")) #12
print(sum_of_numbers("ab")) #0
print(sum_of_numbers("1101")) #1101
print(sum_of_numbers("1111O")) #1111
print(sum_of_numbers("1abc33xyz22")) #56
print(sum_of_numbers("0hfabnek")) #0    
'''

def birthday_ranges(birthdays, ranges):
	bdays = {} # day: number of people born on this day
	for bd in birthdays:
		if bd in bdays.keys():
			bdays[bd] += 1
		else:
			bdays[bd] = 1

	result = []
	for my_range in ranges:
		bdays_in_range = 0
		for i in range(my_range[0], my_range[1] + 1):
		  	if i in bdays.keys():
		  		bdays_in_range += bdays[i]
		result.append(bdays_in_range)
	return result	  
	
'''
print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])) #[2, 3, 4, 5, 2]
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])) #[5, 2, 0, 1]
'''

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

def cut_command(command):
	length = len(command)
	if length > 4 and (command[0] == 7 or command[0] == 9):
		length = length % 4
		command = command[:length]
	elif length > 3 and command[0] != 7 and command[0] != 9:
		length = length % 3
		command = command[:length]
	return command

letters = {1: True, 0: ' ' , 2: 'a', 22: 'b', 222: 'c', 3: 'd', 33: 'e', 333: 'f', 4: 'g',
44: 'h', 444: 'i', 5: 'j', 55: 'k', 555: 'l', 6: 'm', 66: 'n', 666: 'o', 7: 'p', 77: 'q', 777: 'r',
7777: 's', 8: 't', 88: 'u', 888: 'v', 9: 'w', 99: 'x', 999: 'y', 9999: 'z'}

def numbers_to_message(pressed_sequence):
    capitalize = False
    commands = group(pressed_sequence) #
    msg = []
    for command in commands:
    	if command == [1]:
    		capitalize = True	
    	elif command != [-1]:
    		command = cut_command(command)	
    		number = int(''.join(str(i) for i in command))	
    		letter = letters[number]
    		if capitalize: 	
    			letter = letter.upper()
    			capitalize = False
    		msg.append(letter)	

    return "".join(i for i in msg)
'''
print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])) # "abc"
print(numbers_to_message([2, 2, 2, 2])) # "a"
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
# "Ivo e Panda"
'''

def message_to_numbers(message):
	command = []	
	last_number = -1

	for letter in message:
		for key, value in letters.items():
			if value == letter.lower():
				if last_number == str(key)[0]: # add -1
					command.append(-1)
				if value != letter: # capitalize
					command.append(1)
				for i in str(key):
					command.append(int(i))
				last_number = str(key)[0]
			
	return command			

print(message_to_numbers("abc")) # [2, -1, 2, 2, -1, 2, 2, 2]
print(message_to_numbers("a"))   # [2]
print(message_to_numbers("Ivo e Panda")) # [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
print(message_to_numbers("aabbcc")) # [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
