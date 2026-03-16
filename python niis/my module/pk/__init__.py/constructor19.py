class P:
	def __init__(self):
		print("PC")
class C(P):
	def __init__(self):
		super().__init__()
		print("CC")
ob=C()
	