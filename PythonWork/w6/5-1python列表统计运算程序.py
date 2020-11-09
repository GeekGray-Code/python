# 输入一个合法字符串，将字符串转换成int型元素列表
def strToIntList(strValue):
    return list(map(int, str(strValue)))

# 输入一个字符串列表，将它转换为数字列表
def strListToIntList(strList):
    return list(map(int, strList))




# import numpy #求均值中位数

# sequenceList=list(input("Enter a number (<Enter> to quit):").strip().split())
sequenceList=[]
sum=0


while(True):
    numStr=input("Enter a number (<Enter> to quit):")
    if numStr:
        sequenceList.append(numStr)
    if not numStr:
        break



# sequenceIntStr=''.join(sequenceList)#列表转字符串
sequenceIntList=strListToIntList(sequenceList)
sequenceIntList.sort()

for item in sequenceIntList:
    sum+=item

print("The mean is %.6f" % (sum/len(sequenceIntList)))

listLen=len(sequenceIntList)

if listLen%2 == 0: #如果有偶数个整数
    median = (sequenceIntList[int(listLen/2) - 1] + sequenceIntList[int(listLen/2)]) / 2 #计算中间两个的平均值，存到m里
    # print("%.1f" % m) #按一位小数打印m
    print("The median is %.6f" % median)
else: #如果有奇数个整数
    median = sequenceIntList[int((listLen-1)/2)] #将中间那个整数的值存到m里
    # print(m) #直接打印m
    print("The median is %.6f" % median)




# print(sequenceIntList)
# print("The mean is ",numpy.mean(sequenceIntList))
# print("The median is ",numpy.median(sequenceIntList))
# print("The median is ",numpy.median(sequenceIntList))