import unittest
from song import Song

class TestSong(unittest.TestCase):
	def test_create_song_with_seconds(self):
		song = Song(title='Kude sum?', artist='Pesho', album='Chao', length='55')

		self.assertEqual(song.length(), '55 seconds')	

	def test_create_song_with_minutes_and_seconds(self):
		song = Song(title='Kude sum?', artist='Pesho', album='Chao', length='3:55')

		self.assertEqual(song.length(), '3 minutes, 55 seconds')	

	def test_create_song_with_hours_minutes_and_seconds(self):
		song = Song(title='Kude sum?', artist='Pesho', album='Chao', length='4:20:55')

		self.assertEqual(song.length(), '4 hours, 20 minutes, 55 seconds')	

	def test_string_representation(self):
		song = Song(title='Kude sum?', artist='Pesho', album='Chao', length='3:55')
		
		expected_result = 'Pesho - Kude sum? from Chao - 3 minutes, 55 seconds'

		self.assertEqual(str(song), expected_result)	

if __name__ == '__main__':
	unittest.main()