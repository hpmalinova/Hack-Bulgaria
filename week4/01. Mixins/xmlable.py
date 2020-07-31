
import xml.etree.ElementTree as ET

class Xmlable:
	def to_xml():
		pass
	def from_xml(self, xml_string):
		return ET.fromstring(xml_string)

class Food:
	def __init__(self):
		self.f = 'Yummy'

class Panda(Xmlable):
	def __init__(self, name='Pesho'):
		self.name = name
		#self.food = Food()

if __name__ == '__main__':
	panda = Panda(name='Marto')
	ret = panda.from_xml('<Panda><name>Marto</name></Panda>')
	print(ret)