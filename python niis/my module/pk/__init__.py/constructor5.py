class Demo:
	def __init__(self,x,y): #parameter constructor
		self.x=x
		self.y=y #instance variable

print("enter two values")
ob=Demo(int(input()),int(input()))
print("display first object values")
print(ob.x,ob.y)