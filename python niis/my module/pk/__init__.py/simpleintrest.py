class Simple:
	def __init__(self,p,r,t):  #constructor
		self.p=p
		self.rate=r
		self.time=t
	def show(self):
		print("priniple=",self.p)
		print("rate=",self.rate)
		print("time=",self.time)
	def sical(self):
		return self.p*self.rate*self.time/100
i1=Simple(1000,10,2)
i1.show()
print("simple inteset=",i1.sical())