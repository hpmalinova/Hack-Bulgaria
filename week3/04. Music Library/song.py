class Song:
	def __init__(self, title, artist, album, length):
		self.__title = title
		self.__artist = artist
		self.__album = album
		self.__divide_time(length)

	def __divide_time(self, length):
		divided = length.split(':')

		self.__length = {'hours': 0, 'minutes': 0, 'seconds': 0}

		if len(divided) == 1:
			self.__length['seconds'] = int(divided[0])
		if len(divided)	== 2:
			self.__length['minutes'] = int(divided[0])
			self.__length['seconds'] = int(divided[1])
		if len(divided) == 3:
			self.__length['hours'] = int(divided[0])
			self.__length['minutes'] = int(divided[1])
			self.__length['seconds'] = int(divided[2])

	def __str__(self):
		return f'{self.__artist} - {self.__title} from {self.__album} - {self.length()}'

	def __repr__(self):
		return f'{self.__artist} - {self.__title} from {self.__album} - {self.length()}'

	def __eq__(self, other):
		return self.__title == other.__title and self.__artist == other.__artist \
		and self.__album == other.__album and self.__length == other.__length

	def __hash__(self, other):
		return hash(self.__title, self.__artist, self.__album, self.__length)

	def length(self, seconds = True):
		return self.__length['hours']*60*60 + self.__length['minutes']*60 + self.__length['seconds']

	def length(self, minutes = True):
		return self.__length['hours']*60 + self.__length['minutes']
	
	def length(self, hours = True):
		return self.__length['hours']

	def length(self):
		str_length = ''
		for time in ['hours', 'minutes', 'seconds']:
			str_length += self.__convert_time_to_string(self.__length[time], time)
			if str_length and time != 'seconds':
				str_length += ', '

		return str_length		

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

	def get_title(self):
		return self.__title	

	def get_artist(self):
		return self.__artist			

	def get_album(self):
		return self.__album			