# 【问题描述】
#
# 输入字符串，输出字符串中出现次数最多的字母及其出现次数。如果有多个字母出现次数一样，则按字符从小到大顺序输出字母及其出现次数。
# 【输入形式】
#
# 一个字符串。
# 【输出形式】
#
# 出现次数最多的字母及其出现次数
#
# 【样例输入】
#
# abcccd
# 【样例输出】
#
# c 3


#定义一个函数str_maxsum（字符串中最多的字符及数量）参数str_input（字符串输入）
def str_maxsum(str_input):
   #创建一个空的临时列表
   tmp=[]
   #将输入的字符串列表化，list_input（输入列表）
   list_input=list(str_input)
   #循环i小于输入列表长度
   for i in range(len(list_input)):
       #按索引统计输入列表里每个元素出现的次数，并依次添加到临时列表
       tmp.append(list_input.count(list_input[i]))
   #找到临时列表最大值赋给变量list_max（临时列表最大值）
   list_max=max(tmp)
   #循环i小于列表长度（再次循环，目的是找到临时列表最大值对应的输入列表索引值）
   for i in range(len(list_input)):
       #如果临时列表最大值与该索引对应的临时列表值不相等，程序继续但不打印
       if list_max != tmp[i]:
           continue
       #如果相等，将该索引对应的输入列表值传递给变量str_max（最多字符）
       str_max = list_input[i]
   #打印最多字符和临时列表最大值
   print(str_max,list_max)

#调用函数，str_maxsum（字符串中最多的字符及数量），传入参数str_input（‘AABBCCCD’）
# str_maxsum('AABBBCCCD')


def calculate_element(sequence):
    res = {}
    for e in set(sequence):
        res[e] = sequence.count(e)
    return res

dictWord={}
wordStr=input()
wordList=list(wordStr)

for item in wordList:
    dictWord[item] = wordList.count(item)  # 以数字为健，出现的次数为值构建键值对
# 值降序排列，健升序排列
    sortedDictWordList = sorted(dictWord.items(), key=lambda kv: (-kv[1], kv[0]))

    # 遍历list，每个item为元组

# print(sortedDictWordList[0])
# for item in sortedDictWordList:

# 输出出现次数最多的字符
for i in range(0,len(sortedDictWordList)):
    if sortedDictWordList[0][1]==sortedDictWordList[i][1]:
        print("%s %s" % (sortedDictWordList[i][0],sortedDictWordList[i][1]))

