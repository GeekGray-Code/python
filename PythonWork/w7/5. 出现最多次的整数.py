# 【问题描述】
#
# 输入一组无序的整数，编程输出其中出现次数最多的整数及其出现次数。
#
# 【输入形式】
#
# 先从标准输入读入整数的个数（大于等于1，小于等于100），然后在下一行输入这些整数，各整数之间以一个空格分隔。
#
# 【输出形式】
#
# 在标准输出上输出出现次数最多的整数及其出现次数，两者以一个空格分隔；若出现次数最多的整数有多个，则按照整数升序分行输出。
#
# 【样例输入】
#
# 10
#
# 0 -50 0 632 5813 -50 9 -50 0 632
#
# 【样例输出】
#
# -50 3
#
# 0 3
#
# 【样例说明】
#
# 输入了10个整数，其中出现次数最多的是-50和0，都是出现3次

amount=int(input())
dictWord={}

if amount>=1 and amount<=100:
    numList = list(input().strip().split())


for item in numList:
    dictWord[item] = numList.count(item)  # 以数字为健，出现的次数为值构建键值对
# 值降序排列，健升序排列
    sortedDictWordList = sorted(dictWord.items(), key=lambda kv: (-kv[1], kv[0]))


# 输出出现次数最多的字符
for i in range(0,len(sortedDictWordList)):
    if sortedDictWordList[0][1]==sortedDictWordList[i][1]:
        print("%s %s" % (sortedDictWordList[i][0],sortedDictWordList[i][1]))
