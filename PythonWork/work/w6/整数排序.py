# 输入一个字符串列表，将它转换为数字列表
def strListToIntList(strList):
    return list(map(int, strList))

# 判断是否为整数
def isInteger(strValue):
    try:
        num = int(strValue)
        if isinstance(num, int):
            return True

    except ValueError:
        return False

sequenceList=[]
countStr=input()
integerFlag=isInteger(countStr)

if integerFlag:
    count=int(countStr)
    sequenceList=list(input().strip().split())
    sequenceIntList=strListToIntList(sequenceList)

    sequenceIntList.sort()

    for item in sequenceIntList:
        print(item, end=" ")

# sequenceList=list(input().strip().split())
# sequenceIntList=strListToIntList(sequenceList)
#
# sequenceIntList.pop(0)





