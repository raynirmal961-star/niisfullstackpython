"""wap take emp salary from keyboard if sal>=5000 da=30% hra=20% then disply basic salary da hra and totalsal"""
print("enter basic salary")
sal=float(input())
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)