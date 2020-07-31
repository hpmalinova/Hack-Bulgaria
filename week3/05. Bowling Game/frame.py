class Frame:
	def __init__(self, first, second=None,third=None): # string
		self.__first = first
		self.__second = second
		self.__third = third

	def get_points(self):
		if self.__first 