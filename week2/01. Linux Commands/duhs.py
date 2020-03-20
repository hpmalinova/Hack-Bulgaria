# duhs.py
import sys
import os
import math
# + 4k za directory

def round(size):
	res = 0
	while size > 0:
		res += 4096
		size -= 4096
	return res

def get_size(path, size):
	for subfile in os.scandir(path): # ['sub_dir_c', 'file1.py', 'sub_dir_b'...]
		if os.path.isfile(subfile):
			size += round(os.path.getsize(subfile))
		elif os.path.isdir(subfile):
			size += get_size(subfile, 4096)
	return size

def h_readable(num):
	if num >= int(math.pow(2, 10)) and int(num < math.pow(2, 20)):
		print(int(num // math.pow(2, 10)), "KB")
	elif num < int(math.pow(2, 30)):
		print(int(num // math.pow(2, 20)), "MB")
	else:
		print(int(num // math.pow(2, 30)), "GB")

def duhs(path):
	h_readable(get_size(path, 4096))
	
def main():
	duhs(sys.argv[1])


if __name__ == '__main__':
    main()