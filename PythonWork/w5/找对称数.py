import operator


symmetryNumList=list(input().strip().split())
reverseSymmetryNumList=[]
symmetryNumCnt=0

for currentElem in symmetryNumList:
	tempList=list(str(currentElem))
	tempList.reverse()
	tempStr=''.join(tempList)#列表转字符串

	if currentElem==tempStr:
		symmetryNumCnt+=1
		reverseSymmetryNumList.append(currentElem)

reverseSymmetryNumList.append(symmetryNumCnt)	

for currentElem in reverseSymmetryNumList:
	print("%s" % (currentElem),end=" ")

