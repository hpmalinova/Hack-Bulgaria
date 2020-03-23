from length import Length
class Song:
	def __init__(self, title, artist, album, length):
		self.__title = title
		self.__artist = artist
		self.__album = album
		self.__length = Length(length)
	
	def __str__(self):
		return f'{self.__artist} - {self.__title} from {self.__album} - {self.__length}'

	def __repr__(self):
		return f'{self.__artist} - {self.__title} from {self.__album} - {self.__length}'

	def __eq__(self, other):
		return self.__title == other.__title and self.__artist == other.__artist \
		and self.__album == other.__album and self.__length == other.__length

	def __hash__(self):
		return hash(self.__title, self.__artist, self.__album, self.__length)

	def length(self, seconds=True):
		return self.__length.length(seconds=True)

	def length(self, minutes=True):
		return self.__length.length(minutes=True)	

	def length(self, hours = True):
		return self.__length.length(hours=True)

	def length(self):
		return str(self.__length)

	def get_title(self):
		return self.__title	

	def get_artist(self):
		return self.__artist			

	def get_album(self):
		return self.__album			