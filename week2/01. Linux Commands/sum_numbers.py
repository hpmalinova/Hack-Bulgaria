import sys

# filename = "5 2 13123 1234 123"
def sum_numbers(filename):
	with open(filename, 'r') as f:
		numbers = [x for x in f.read().split(" ") if x != ''] # ["12", "23"...]
		my_sum = 0
		for number in numbers:
			my_sum += int(number)
		print(my_sum)	


def main():
    sum_numbers(sys.argv[1])

if __name__ == '__main__':
    main()	