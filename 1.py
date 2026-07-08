class User:
	age = 0

	def __init__(self, name):
		print("я создался")
		self.username = name

	def sayName(self):
		print("меня зовут ", self.username)

	def sayAge(self):
		print(self.age) 

	def setAge(self, newAge):
		self.age = newAge

alex = User("Alex")
mark = User("Mark")
marta = User("Marta")

alex.sayName()
alex.sayAge() #в скрипте уже был запрос на выведение возраста
alex.setAge(33) #создали запрос на изменение возраста
alex.sayAge() #создали запрос на проверку изменения возраст