import unittest
from song import Song
from playlist import Playlist

class TestPlaylist(unittest.TestCase):
	def test_init_playlist_with_no_songs(self):
		playlist = Playlist('my playlist')

		self.assertEqual(playlist.get_index_of_last_played_song(), -1)

	def test_add_new_song_to_playlist(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		playlist = Playlist('my playlist')
		expected_songs_in_playlist = [song1]
	
		playlist.add_song(song1)
	
		self.assertEqual(playlist.get_songs(), expected_songs_in_playlist)	

	def test_add_new_songs_consecutively_to_playlist(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		expected_songs_in_playlist = [song1, song2]

		playlist.add_song(song1)
		playlist.add_song(song2)
		
		self.assertEqual(playlist.get_songs(), expected_songs_in_playlist)	
		
	def test_add_new_songs_to_playlist(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		expected_songs_in_playlist = [song1, song2]

		playlist.add_songs([song1, song2])
		
		self.assertEqual(playlist.get_songs(), expected_songs_in_playlist)	

	def test_when_add_one_song_two_times_then_add_it_just_once(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		playlist = Playlist('my playlist')
		expected_songs_in_playlist = [song1]

		playlist.add_song(song1)
		playlist.add_song(song2)
		
		self.assertEqual(playlist.get_songs(), expected_songs_in_playlist)		

	def test_when_remove_song_in_playlist_then_return_message_and_remove_it(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		playlist = Playlist('my playlist')
		expected_songs_in_playlist = []
		playlist.add_song(song1)
		
		message = playlist.remove_song(song1)
		
		self.assertEqual(message, 'The song was removed')
		self.assertEqual(playlist.get_songs(), expected_songs_in_playlist)		

	def test_when_remove_song_not_in_playlist_then_return_message(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		playlist.add_song(song1)
	
		message = playlist.remove_song(song2)
		
		self.assertEqual(message, 'This song is not in the playlist')
		self.assertEqual(playlist.get_songs(), [song1])	

	def test_when_no_songs_then_return_total_length_0(self):
		playlist = Playlist('my playlist')

		result = playlist.find_total_length_songs()

		self.assertEqual(result, '0 seconds')	

	def test_find_total_length_of_songs(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		playlist.add_songs([song1, song2])

		result = playlist.find_total_length_songs()

		self.assertEqual(result, '9 minutes, 34 seconds')	

	def test_when_artists_appear_once_return_histogram(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Pesho", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		playlist.add_songs([song1, song2])
		expected_result = {'Manowar': 1, 'Pesho': 1}

		result = playlist.artists()

		self.assertEqual(result, expected_result)	

	def test_when_artists_appear_more_than_once_return_histogram(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		playlist.add_songs([song1, song2])
		expected_result = {'Manowar': 2}

		result = playlist.artists()

		self.assertEqual(result, expected_result)			

	def test_when_no_songs_then_return_empty_histogram(self):
		playlist = Playlist('my playlist')
		expected_result = {}

		result = playlist.artists()

		self.assertEqual(result, expected_result)			

class TestNextSongInPlaylist(unittest.TestCase):
	def test_when_no_songs_then_return_error_message(self):
		playlist = Playlist('my playlist')

		message = playlist.next_song()
		
		self.assertEqual(message, "No songs in playlist.")		

	def test_when_playlist_has_no_requirements_and_no_init(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		playlist.add_songs([song1, song2])

		song = playlist.next_song()
		
		self.assertEqual(playlist.get_index_of_last_played_song(), 0)
		self.assertEqual(song, song1)		

	def test_when_playlist_has_no_requirements_and_no_next_element_then_return_error(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist')
		playlist.add_songs([song1, song2])

		playlist.next_song()
		playlist.next_song()
		message = playlist.next_song()

		self.assertEqual(message, "No more songs to play. Refresh the playlist!")		
		self.assertEqual(playlist.get_index_of_last_played_song(), 1)
		
	def test_when_playlist_has_repeat_and_no_next_element(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		playlist = Playlist('my playlist', repeat=True)
		playlist.add_songs([song1, song2])

		playlist.next_song()
		playlist.next_song()
		song = playlist.next_song()
		
		self.assertEqual(playlist.get_index_of_last_played_song(), 0)
		self.assertEqual(song, song1)	

	def test_when_playlist_has_shuffle_and_no_next_element_than_return_error(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:50")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		song3 = Song(title="The Crown and the Ring", artist="Manowar", album="Kings of Metal", length="4:50")

		playlist = Playlist('my playlist', shuffle=True)
		playlist.add_songs([song1, song2, song3])

		a = playlist.next_song()
		b = playlist.next_song()
		c = playlist.next_song()

		# print(a,b,c) -> to test if played in random order? # Question 
	
		message = playlist.next_song()

		self.assertEqual(message, "No more songs to play. Refresh the playlist!")		
		self.assertEqual(playlist.get_index_of_last_played_song(), 2)

	def test_when_playlist_has_shuffle_and_repeat(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:50")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		song3 = Song(title="The Crown and the Ring", artist="Manowar", album="Kings of Metal", length="4:50")
		playlist = Playlist('my playlist', shuffle=True, repeat=True)
		playlist.add_songs([song1, song2, song3])

		playlist.next_song()
		playlist.next_song()
		playlist.next_song()
		song = playlist.next_song()	
		#print(a,b,c, song) #-> to test if played in random order? # Question 
		
		self.assertTrue(isinstance(song, Song))
		self.assertEqual(playlist.get_index_of_last_played_song(), 0)

	def test_when_playlist_has_no_requirements_and_gets_to_the_end_then_refresh(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:50")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		song3 = Song(title="The Crown and the Ring", artist="Manowar", album="Kings of Metal", length="4:50")
		playlist = Playlist('my playlist', shuffle=True, repeat=True)
		playlist.add_songs([song1, song2, song3])
		playlist.next_song()
		playlist.next_song()
		playlist.next_song()

		playlist.refresh()

		self.assertEqual(playlist.get_index_of_last_played_song(), -1)

	def test_when_playlist_has_no_requirements_and_gets_to_the_end_then_refresh_and_get_next_song(self):
		song1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:50")
		song2 = Song(title="Hail and Kill", artist="Manowar", album="Kings of Metal", length="5:50")
		song3 = Song(title="The Crown and the Ring", artist="Manowar", album="Kings of Metal", length="4:50")
		playlist = Playlist('my playlist', shuffle=True, repeat=True)
		playlist.add_songs([song1, song2, song3])
		playlist.next_song()
		playlist.next_song()
		playlist.next_song()

		playlist.refresh()
		song = playlist.next_song()

		self.assertEqual(song, song1)
		self.assertEqual(playlist.get_index_of_last_played_song(), 0)

if __name__ == '__main__':
	unittest.main()		