from que_via_stack import Que

class AnimalShelter():
	def __init__(self):
		self.cats = Que()
		self.dogs = Que()
		self.history = Que()

	def enque(self, animal, species):
		if species == 'dog':
			self.dogs.add(animal)
		elif species == 'cat':
			self.cats.add(animal)
		self.history.add(species)

	def deque_any(self):
		if self.history.is_empty():
			return None
		species = self.history.remove()
		if species == 'dog':
			return self.dogs.remove()
		elif species == 'cat':
			return self.cats.remove()
	
	def remove_history(self, species):
		temp = 0
		while self.history.remove() != species:
			temp += 1
		for i in range(0, temp):
			self.history.add('cat' if species == 'dog' else 'dog')
	
	def deque_cat(self):
		if self.cats.is_empty():
			return None
		self.remove_history('cat')
		return self.cats.remove()

	def deque_dog(self):
		if self.dogs.is_empty():
			return None
		self.remove_history('dog')
		return self.dogs.remove()

shelter = AnimalShelter()
shelter.enque('dog1', 'dog')
shelter.enque('dog2', 'dog')
shelter.enque('cat1', 'cat')
shelter.enque('dog3', 'dog')
shelter.enque('cat2', 'cat')
shelter.history.display()
print(shelter.deque_any() == 'dog1')
print(shelter.deque_cat() == 'cat1')
print(shelter.deque_dog() == 'dog2')
