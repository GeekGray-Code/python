import math

listCoefficient=[]
listCoefficient=list(input().strip().split())

a=float(listCoefficient[0])
b=float(listCoefficient[1])
c=float(listCoefficient[2])


if a!=0 and (b*b-4*a*c)>=0:
	temp=b*b-4*a*c
	delt=math.sqrt(temp)
	if delt>=0:
		x1=(-b+delt)/(2*a)
		x2=(-b-delt)/(2*a)

		print("%.2f %.2f" % (max(x1,x2),min(x1,x2)),end=" ")

else :
	print("No")


 