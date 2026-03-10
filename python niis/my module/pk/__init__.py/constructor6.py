class Demo:
	def set(self,x,y): #method
		self.x=x
		self.y=y #instance variable

print("enter two values")
ob=Demo()
ob.set(10,20)
print("display first object values")
print(ob.x,ob.y)