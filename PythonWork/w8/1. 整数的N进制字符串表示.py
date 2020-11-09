# 【问题描述】
#
# 编写函数itob(n,b),用于把整数n转换成以b为基底的字符串并返回.
#
# 编写程序,使用函数itob(n,b)将输入的整数n,转换成字符串s,将s输出。转换后的字符串从最高的非零位开始输出。如果n为负数，则输出的字符串的第一个字符为'-'。b为大于1小于37的任意自然数。当b=2时，输出字符只可能是'0'和'1'；当b=16时，输出字符串中可能含有字符为'0'-'9'，'a'-'f'(字母以小写输出)。b为18时，数码是'0'-'9'，'a'-'h'，其中'a'代表10，'g'代表16， 'h'代表17。又比如，输入n=33,b=17，则输出33的17进制值为"1g"。
#
# 【输入形式】输入整数n和b，其中n可以为负数。n和b以空格分隔.
# 【输出形式】输出转换后的字符串s.
# 【样例输入】5 2
# 【样例输出】101
# 【样例说明】5的二进制就是101

def itob(n, b):
    bList=[]
    flag= False
    if n<0:
        n = -n
        flag= True
    while (n/b):
        j = n%b
        n = n//b
        if j>9:
            j=chr(j+97-10)
        bList.append(j)
    return flag,bList

numStrList = input().split(" ")
numStrList[0] = int(numStrList[0])
numStrList[1] = int(numStrList[1])
bList = []

#将函数返回值a和s赋值给A和S
flag,bList = itob(numStrList[0],numStrList[1])

if flag:
    print("-",end="")
    for i in range(len(bList)-1,-1,-1):	#range的倒序输出
        print(bList[i],end="")
else:
    for i in range(len(bList)-1,-1,-1):
        print(bList[i],end="")

