# wc.py
import sys

def wc_chars(filename):
	with open(filename, 'r') as f:
		print(len(f.read()))

def wc_words(filename):
	with open(filename, 'r') as f:
		all_lines = [x for x in f.read().replace('\n', ' ').split(' ') if x != '']
		print(len(all_lines))
		
def wc_lines(filename):
	with open(filename, 'r') as f:
		print(len(f.readlines()))	

def wc(command, filename):
	if command == 'chars':
		wc_chars(filename)
	elif command == 'words':
		wc_words(filename)
	elif command == 'lines':
		wc_lines(filename)
	else:
		"Invalid input, try again"

def main():
	wc(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()