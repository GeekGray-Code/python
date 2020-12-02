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
countStr=input("How  many numbers are there? ")
integerFlag=isInteger(countStr)

if integerFlag:
    count=int(countStr)
    for i in range(count):
        num=int(input("Enter  a  number  >> "))
        sequenceList.append(num)

    print("The  largest  value  is",max(sequenceList))


# sequenceList=list(input().strip().split())
# sequenceIntList=strListToIntList(sequenceList)
#
# print(max(sequenceIntList))