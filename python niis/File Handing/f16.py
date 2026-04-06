#write three student project in the file
import pickle
#create class
class Student:
	def __init__(self,roll,name,mark):
		self.roll = roll
		self.name = name
		self.mark = mark
	def show(self):
		print(self.roll,self.name,self.mark)
#write object to binary file
f = open("Student.dat","wb")
s1 = Student(101, "Arun",85)
s2 = Student(102, "Ravi",90)
s3 = Student(103, "sita",88)
pickle.dump(s1, f)
pickle.dump(s2, f)
pickle.dump(s3, f)
f.close()

