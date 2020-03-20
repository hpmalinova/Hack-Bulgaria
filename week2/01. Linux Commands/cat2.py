# cat2.py
import sys

def cat2(arguments):
	for arg in arguments:
		with open(arg, 'r') as f:
			print(f.read())
		print()

def main():
	cat2(sys.argv[1::])

if __name__ == '__main__':
    main()