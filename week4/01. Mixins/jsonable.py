import json

class Jsonable:
	def to_json(self, indent=4):
		return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4)

	def from_json(self, json_string): #returns object
		return self(json_string)