


import sys
# import numpy #求均值中位数


# 判断是否为整数
def isInteger(strValue):
    try:
        num = int(strValue)
        if isinstance(num, int):
            return True

    except ValueError:
        return False


# 输入一个字符串列表，将它转换为数字列表
def strListToIntList(strList):
    return list(map(int, strList))

# sequenceList=list(input().strip().split())
sequenceList=[]
countStr=input()
amount=0

integerFlag=isInteger(countStr)

if integerFlag:
    count=int(countStr)
    if count<0:
        print("illegal input")
    else:
        for i in range(count):
            num=int(input())
            sequenceList.append(num)
        if count==0:
            print(0)
        else:
            # avg = numpy.mean(sequenceList)
            avg = sum(sequenceList)/count
            for item in sequenceList:
                if item >= avg:
                    amount += 1
            print(amount)
else:
    print("illegal input")



# sequenceIntList=strListToIntList(sequenceList)
# avg=numpy.mean(sequenceIntList)




