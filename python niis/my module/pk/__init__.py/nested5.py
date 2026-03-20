L=[]
print("enter how many list store")
s=int(input())
for i in range(0,s,1):
	X=[]
	print("enter list ",i+1,"how many data")
	s1=int(input())
	for j in range(0,s1,1):
		print("enter element",j+1)
		X.append(int(input()))
	L.append(X)
print("elements are")
for i in range(0,len(L),1):
	for j in range(0,len(L[i]),1):
		print(L[i][j],end="\t")
	print()