#判断合法数字
def isInteger(passwordStr):
   try:
         num=int(passwordStr)
         if isinstance(num,int):
         	return True

   except ValueError:
   	return False

import sys

index=0
sum=0
scoreList=[]
stuCountStr=input()

if isInteger(stuCountStr):
	stuCount=int(stuCountStr)
	if stuCount>0:
		while index<stuCount:
			scoreElemStr=input()
			if isInteger(scoreElemStr):
				scoreElem=int(scoreElemStr)
				if scoreElem>=0 and scoreElem<=100:
					scoreList.append(scoreElem)
					sum+=scoreList[index]
					index+=1
				else:
					print("illegal input")
					sys.exit(0)
			else:
					print("illegal input")
					sys.exit(0)

		print("%.2f" % (sum/len(scoreList)))

	else:
		print("illegal input")
		sys.exit(0)
else:
	print("illegal input")







