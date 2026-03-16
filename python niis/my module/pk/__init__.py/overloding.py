class A:
	def f1(self):
		print("Person")
class B(A):
	def f2(self):
		print("Student")
class C(B):
	def f3(self):
		print("Engineer")
ob=C()
ob.f1()
ob.f2()
ob.f3()