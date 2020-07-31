import unittest

from jsonable import Jsonable

class Panda(JS):
	def __init__(self):
		pass

class JS:
	def to_json(self, indent =4):
		name = self

class TestJsonable(unittest.TestCase):
	def test_to_json_returns_empty_json_for_objects_with_no_arguments(self):
		panda = Panda()

		expected = {
			'type': Panda.__name__,
			'dict': {}
		}

		self.assertEqual(panda.to_json(), expected)

if __name__ == '__main__':
	unittest.main())	