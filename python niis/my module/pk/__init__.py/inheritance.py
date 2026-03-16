#Parent Class
class Person:
	def __init__(self,name,age):
		self,name=name
		self,age=age
	def show_person(self):
		print("Name :",self.name)
		print("age :",self.age)
#child class
class Student(Person):
	def __init__(self, name, age, roll):
		super().__init__(name,age)
		self.roll = roll
	def show_student(self):
		print("Roll No :", self.roll)

#Grand child class
class EnggStudent(Student):
	def __init__(self,name,age,roll,branch):
		super().__init__(name,age,roll)
		self.branch = branch
	def show_engg(self):
		print("Branch :",self.branch)
#Object creation
e = EnggStudent("Soumitra",20,101,"Computer Science")
# calling methods
e.show_person()
e.show_student()
e.show_engg()