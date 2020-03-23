class Length:
	def __init__(self, str_length):
		self.__length = {'hours': 0, 'minutes': 0, 'seconds': 0}
		self.__divide_time(str_length)

	def __divide_time(self, str_length):
		divided = str_length.split(':')
		
		if len(divided) == 1:
			self.__length['seconds'] = int(divided[0])
		if len(divided)	== 2:
			self.__length['minutes'] = int(divided[0])
			self.__length['seconds'] = int(divided[1])
		if len(divided) == 3:
			self.__length['hours'] = int(divided[0])
			self.__length['minutes'] = int(divided[1])
			self.__length['seconds'] = int(divided[2])	

	def length(self, seconds=False, minutes=False, hours=False):
		if seconds==True:
			return self.__length['hours']*60*60 + self.__length['minutes']*60 + self.__length['seconds']
		elif minutes==True:
			return self.__length['hours']*60 + self.__length['minutes']
		elif hours==True:	
			return self.__length['hours']

	@staticmethod	
	def __convert_time_to_string(length, time):
		str_length = ''

		if length != 0:
			if time == 'hours':
				str_length += str(length) + ' hours'
			if time == 'minutes':
				str_length += str(length) + ' minutes'
			if time == 'seconds':
				str_length += str(length) + ' seconds'

		return str_length			

	def __str__(self):
		str_length = ''
		for time in ['hours', 'minutes', 'seconds']:
			str_length += self.__convert_time_to_string(self.__length[time], time)
			if str_length and time != 'seconds':
				str_length += ', '

		if not str_length:
			str_length = '0 seconds'		
				
		return str_length		

	def __repr__(self):
		str_length = ''
		for time in ['hours', 'minutes', 'seconds']:
			str_length += self.__convert_time_to_string(self.__length[time], time)
			if str_length and time != 'seconds':
				str_length += ', '

		return str_length			

	def __eq__(self, other):
		return self.__length == other.__length	

	def __hash__(self, other):
		return hash(self.__length)	