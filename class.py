my_pet = {"name": "Bear", "colors": ["brown"], "weight": 10}

class Dog(object):
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight

my_dog = Dog("Bear", "Brown", 10)
my_dog2 = Dog("Rascal", "White", 6)

print my_dog.name
print my_dog2.name

class Food(object):
	def __init__(self, appetizer, entrees, desserts):
			self.appetizer = appetizer
			self.entrees = entrees
			self.desserts = desserts

starter = Food("gyoza", "ramen", "mochi")

print starter.appetizer

class Animals(object):
	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight

mammals = Animals("Lion", "Brown", 550)

print mammals.name