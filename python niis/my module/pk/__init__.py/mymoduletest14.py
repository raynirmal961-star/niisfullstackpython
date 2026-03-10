class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("my name=",self.name)
		print("my rollno=",self.roll)
		print("my mark=",self.mark)
s1=student("Soumitra",1,70.50)
s2=student("Satish",2,80.50)
s3=student("Suman",3,70.50)
s1.show()
s2.show()
s3.show()