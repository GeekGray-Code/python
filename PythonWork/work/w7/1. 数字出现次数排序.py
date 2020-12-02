# 【问题描述】
#
# 给定n个整数，请统计出每个整数出现的次数，按出现次数从多到少的顺序输出。
#
#
# 【输入形式】
#
# 第一行包含一个整数n，表示给定数字的个数; 第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。
#
# 【输出形式】
#
# 输出有多行，每行包含两个整数，分别表示一个给定的整数和它出现的次数。按出现次数递减的顺序输出。如果两个整数出现的次数一样多，则先输出值较小的，然后输出值较大的。
#
# 【样例输入】
#
# 12
#
# 5 2 3 3 1 3 4 2 5 2 3 5
#
# 【样例输出】
#
# 3 4
#
# 2 3
#
# 5 3
#
# 1 1
#
# 4 1
#
#
# 【样例说明】
#
# n不超过1000，给出的数为2,000,000,000以内的非负整数。




import operator

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

amount=int(input())
sequenceList=[]
dictNum={}

if amount<=1000:
    sequenceList = list(input().strip().split())
    sequenceIntList=strListToIntList(sequenceList)

    # sequenceIntList.sort()
    for item in sequenceIntList:
        dictNum[item]=sequenceIntList.count(item)#以数字为健，出现的次数为值构建键值对

    # 使用sorted高阶函数对dict进行值排序，得到结果为一个由元素为元组构成的list
    # sortedDictList = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)#对单个条件进行排序

    # 值降序排列，健升序排列
    sortedDictList = sorted(dictNum.items(), key=lambda kv: (-kv[1], kv[0]))#多个限制条件排序

    # 遍历list，每个item为元组
    for item in sortedDictList:
        print("%s %s" % (item[0], item[1]))

    # for i in range(0, len(sortedDictList)):
    #     print("%s %s" % (sortedDictList[i][0], sortedDictList[i][1]))


