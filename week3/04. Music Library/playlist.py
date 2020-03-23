import datetime
import random
from song import Song
from length import Length

class Playlist:
	def __init__(self, name, repeat=False, shuffle=False):
		self.__name = name
		self.__repeat = repeat
		self.__shuffle = shuffle
		self.__songs = []
		self.__iterator = iter(self)

	def get_songs(self):
		return self.__songs	

	# TODO
	# add print	method -> only name; all_songs (one by one); all_songs (by artist); all_songs (by album)

	def add_song(self, song):
		if isinstance(song, Song) and not song in self.__songs:
			self.__songs.append(song)
	
	def add_songs(self, songs):
		for song in songs:
			self.add_song(song)	

	def remove_song(self, song): # Question: Да връща string/ print/ exception? 
		if song in self.__songs:
			self.__songs.remove(song)
			return 'The song was removed'
		else:
			return 'This song is not in the playlist'

	def find_total_length_songs(self): 
		time_in_seconds = 0

		for song in self.__songs:
			time_in_seconds += song.length(seconds=True)

		total_len = Length(str(datetime.timedelta(seconds=time_in_seconds)))	

		return str(total_len)

	def artists(self):
		histogram = {} # artist: times in the playlist		
		for song in self.__songs:
			if song.get_artist() in histogram:
				histogram[song.get_artist()] += 1
			else:
				histogram[song.get_artist()] = 1	
		return histogram

	def refresh(self, repeat=False, shuffle=False):
		self.__repeat = repeat
		self.__shuffle = shuffle
		self.__iterator = iter(self)
			
	def next_song(self): # returns a Song
		try:
			return next(self.__iterator)
		except ValueError:
			return "No songs in playlist."
		except StopIteration:
			return "No more songs to play. Refresh the playlist!"

	def __iter__(self):
		self.__last_played = -1 # index in order_of_songs
		return self

	def get_index_of_last_played_song(self):
		return self.__last_played

	def __next__(self): # returns a Song
		if not self.__songs:
			raise ValueError

		next_song = None
			
		if self.__last_played == -1:
			self.__init_order_of_songs()
		
		next_song = self.__get_next_song() 	

		if next_song:
			return next_song 	
		else:
			raise StopIteration	

	def __init_order_of_songs(self):
		self.__order_of_songs = list(range(0, len(self.__songs)))
		if self.__shuffle:
			random.shuffle(self.__order_of_songs)
				
	def __get_next_song(self):
		if self.__last_played == len(self.__songs) - 1:
			if self.__repeat:
				if self.__shuffle:
					self.__init_order_of_songs()
				self.__last_played = 0
				return self.__songs[self.__order_of_songs[self.__last_played]]

			else:
				return None
		else:
			self.__last_played += 1
			return self.__songs[self.__order_of_songs[self.__last_played]]		