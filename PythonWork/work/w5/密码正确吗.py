##############################Function##############################################

# 判断是否为整数
def isInteger(passwordStr):
    try:
        num = int(passwordStr)
        if isinstance(num, int):
            return True

    except ValueError:
        return False


# 输入一个合法字符串，将字符串转换成int型元素列表
def strToIntList(strValue):
    return list(map(int, str(strValue)))


# 输入一个合法的字符串，取它的个位数
def getDigits(strValue):
    tempList = list(map(int, str(strValue)))
    return tempList[(len(tempList) - 1)]


#############################Main###########################################


passwordStr = input()
count = 0
rightCount = 0

integerFlag = isInteger(passwordStr)

if integerFlag:
    passwordNum = int(passwordStr)
    pwdList = strToIntList(passwordStr)

    for currentElement in pwdList[1:6]:
        count += 1
        tempNumStr = str((pwdList[count - 1] + 1) ** 3)

        # print(currentElement)

        if currentElement == getDigits(tempNumStr):
            rightCount += 1

if rightCount == len(passwordStr) - 1:
    print("right")
else:
    print("wrong")
