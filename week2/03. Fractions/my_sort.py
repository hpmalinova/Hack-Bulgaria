'''
Implement a function, called my_sort that takes 3 arguments. The arguments are:

iterable - list or tuple that has to be sorted. Preserve the type in the return value. 
Must have default value

ascending - boolean that controls the sorting order. Must have default value

key - string that serves as a lookup key if the iterable argument is a list of dictionaries. 
Must have default value

The function should return the given iterable sorted in order that is controlled by the ascending value.
'''

def partition(array, start, end):
	pivot = array[start]
	low = start + 1
	high = end

	while True:
		while low <= high and array[high] >= pivot:
			high = high - 1
		
		while low <= high and array[low] <= pivot:
			low = low + 1

		if low <= high:
			array[low], array[high] = array[high], array[low]
		else:
			break

	array[start], array[high] = array[high], array[start]

	return high

def quick_sort(array, start, end):
	if start < end:
		p = partition(array, start, end)
		quick_sort(array, start, p - 1)
		quick_sort(array, p + 1, end)

def my_sort(iterable = None, ascending = True, key = ''):
	pass

if __name__ == '__main__':
	arr = (4,1,7,0)
	quick_sort(arr, 0, 3)
	print(arr)



	'''
	sorted_iterable = []
	if iterable == None or :
		sorted_iterable = []
	'''	