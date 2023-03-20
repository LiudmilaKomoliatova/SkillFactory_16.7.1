class Cat:
	def __init__(self, name='', gender='', age=0):
		self.name = name
		self.gender = gender
		self.age = age

	def __str__(self):
		return f'name: {self.name} gender: {self.gender} age: {self.age}'


new_cat = Cat("Зевс", "Male", 12)

print(new_cat)
