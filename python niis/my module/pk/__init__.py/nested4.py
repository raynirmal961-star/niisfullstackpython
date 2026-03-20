L=[]
print("enter how many list store")
s=int(input())
for i in range(0,s,1):
	print("enter list1 data")
	X=eval(input())
	L.append(X)
print("elements are")
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()