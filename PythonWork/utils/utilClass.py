tempList=[]

# 判断是否为整数
import operator


def isInteger(strValue):
    try:
        num = int(strValue)
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


# 输入一个字符串列表，将它转换为数字列表
def strListToIntList(strList):
    return list(map(int, strList))



tempStr=''.join(tempList)#列表转字符串
str1='abc'
list(str1)#字符串转列表
# print("%s" % (currentElem),end=" ") #空格隔开输出,最后一个元素后面有空格
# print("+".join(str(item) for item in snList))#+号隔开输出,最后一个元素后面五+号

# 使用sorted高阶函数对dict进行值排序，得到结果为一个由元素为元组构成的list
    # sortedDictList = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

    # lamba表达式对字典值降序排列，健升序排列
    # sortedDictList = sorted(dict.items(), key=lambda kv: (-kv[1], kv[0]))