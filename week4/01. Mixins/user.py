from jsonable import Jsonable
from xmlable import Xmlable

import json

class Name(Jsonable):
	def __init__(self, name, last_name):
		self.name = name
		self.last_name = last_name

	def __str__(self):
		return self.to_json()
			
	def __repr__(self):
		return self.to_json()	


class User(Jsonable, Xmlable): 
	def __init__(self, name, last_name, age):
		self.age = age
		self.name = Name(name, last_name)
	
	def __str__(self):
		return self.to_json()

	def __repr__(self):
		return self.to_json()



if __name__ == '__main__':
	u = User('Pesho', 'Peshev', 29)
	print(u)