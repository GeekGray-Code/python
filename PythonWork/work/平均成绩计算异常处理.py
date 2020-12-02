# 1. 平均成绩计算异常处理
# 【问题描述】
#
# 用户输入若干个成绩（百分制），求所有成绩的平均分。
# 每输入一个分数后询问是否继续输入下一个分数，回答“y”或“Y”就继续输入下一个分数，
# 回答“n”或“N”就停止输入分数。如果成绩输入有误，要求输出“不是合法成绩”（要求有异常处理）

# 判断是否为整数
import operator


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


scoreList=[]
sum=0

while True:

    score=input("请输入一个百分制分数：")

    flagInput=input("是否继续输入下一个分数，回答“y”或“Y”继续输入下一个分数，回答“n”或“N”就停止输入分数: ")


    if flagInput == 'y' or flagInput == 'Y':
        intFlag = isInteger(score)

        if intFlag:
            scoreList.append(score)

    elif flagInput == 'n' or flagInput == 'N':
        intFlag = isInteger(score)

        if intFlag:
            scoreList.append(score)
        else:
            print("{} is illegal score.".format(score))
        break






scoreIntList=strListToIntList(scoreList)
print(scoreList)
print(scoreIntList)

for item in scoreIntList:
    sum+=item

try:

    avg=sum/len(scoreIntList)
    print("The average score is {}.".format(avg))

except ZeroDivisionError:
    print("异常信息：除数不能为0")




