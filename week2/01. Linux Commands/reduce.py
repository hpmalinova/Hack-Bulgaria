# reduce.py
import sys

def reduce_file_path(path):
	path = [x for x in path.split('/') if x != '' and x != '.']
	print('path:', path)
	if not path:
		return '/'
	result = []
	for i in range(0, len(path)):
		result.append('/')
		if path[i] == '..':
			result = result[:i*2 - 2] # - 1 ...-Python/week01
		else:
			result.append(path[i])
	print('result', result)
	print("".join(result))

def main():
#	reduce_file_path(argv[1])
#	print(reduce_file_path("/")) # "/"
	print(reduce_file_path("/srv/../")) # "/"
#	print(reduce_file_path("/srv/www/htdocs/wtf/")) # "/srv/www/htdocs/wtf"
#	print(reduce_file_path("/srv/www/htdocs/wtf")) # "/srv/www/htdocs/wtf"
#	print(reduce_file_path("/srv/./././././")) # "/srv"
#	print(reduce_file_path("/etc//wtf/")) # "/etc/wtf"
#	print(reduce_file_path("/etc/../etc/../etc/../")) # "/"
#	print(reduce_file_path("//////////////")) # "/"
#	print(reduce_file_path("/../")) # "/"


if __name__ == '__main__':
    main()