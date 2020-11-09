### isdigit() 无法判断整数
# a="123"
# b="11.09"
# c='eee'
#
# print(a.isdigit())  #True
# print(b.isdigit())  #False
# print(c.isdigit())  #False


########################--------------------------- 实验报告一
# 计算圆周长和面积

# r=3.2
# area=3.14*r*r
# perimeter=2*3.14*r
# print("圆形的面积：{:.2f},周长:{:.2f}".format(area,perimeter))


# 计算三角形的面积

# import math
#
# try:
#     a=eval(input())
#     b=eval(input())
#     c=eval(input())
#
#     p=(a+b+c)/2
#     s=math.sqrt(p*(p-a)*(p-b)*(p-c))
#     print("三角形的面积是：{:.2f}".format(s))
# except NameError:
#     print("请输入正数数值")

# num=int(input())
#
# print("{:}的二进制：{:}".format(num,bin(num)))
# print("{:}的八进制：{:}".format(num,oct(num)))
# print("{:}的十六进制：{:}".format(num,hex(num)))

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# print(a+b-c*d)

# c=float(input("请输入摄氏温度:"))
#
# f=9*c/5+32
#
# print("摄氏温度{}对应的华氏度为:{:}".format(c,f))

# import math
# r=eval(input("请输入圆锥体的底面半径："))
# h=eval(input("请输入圆锥体的高："))
#
# print("圆锥体的体积：",math.pi*r*r*h/3)
########################--------------------------- 实验报告一


########################--------------------------- 作业7填空

# print('abc' in 'abdcefg')
# print((1,2,3)+(4,5))

# x={1:2}
# x[2]=2
# print(len(x))

# print({1,2,3,4}-{3,4,5,6})

# x=[1,2,3]
# y=x[:]
# print(y is x)


# print({1,2,3}&{3,4,5})


# x=[1,2,3,4,5]
# del x[:3]
# print(x)


# print(list(str([1,2,3]))==[1,2,3])

# print(list(set([3,2,1]))==[3,2,1])


# x=[[]]*3
# x[0].append(1)
# print(x)

# print(True*3)

# x='1'
# y='1'
# print(x+y)

# x=[1,2]
# x[0:1]=[0,1,2]
# print(x)

# print(3 not in {(1),(2),(3)})

# print({1,2,3}=={3,2,1})
########################--------------------------- 作业7填空


########################--------------------------- 实验报告2

# tul1=(123,1222,1998,10)   #元组创建
# sorted(tul1)    #元组排序
# del tul1    #删除元组


# testList = [124, 456, 789, 908,124]  # 创建列表
# testList.append(100)  # 增加
# testList.remove(124)  # 删除
# testList.count(124)  # 计数
# testList.sort()  # 排序


# testDict={"name":"Geek","age":23}#创建字典
# del testDict['name']#删除键值对
# testDict["age"]=18#修改
# print(testDict)#读取

# testSet=[1,2,3,4,5,6]#创建
# testSet.remove(1)#删除
# testSet.clear()#清空


# 2、根据输入字符串 s，输出一个宽度为 15 字符，字符串 s 居中显示，以
# “=”填充的格式。如果输入字符串超过 15 个字符，则输出字符串前 15 个字
# 符，最终输出其全小写形式。

# testStr=input()
#
# if len(testStr)<=15:
#     print(testStr.center(15,'='))
# else:
#     print(testStr[:15].lower())


# 3、给定一个数字 123456，请采用宽度为 25、右对齐方式打印输出，使用
# 加号“+”填充。

# print("123456".rjust(25,'+'))


# 4、s="123"是一个整数形式字符串，编写程序判断 s 是否是整数形式字符串。
# 如果是则输出 True，否则输出 False。要求代码不超过 2 行。

# print("123".isdigit())


# （1）建立字典 dict，包含内容是："数学":81, "语文":95, "英语":78, "物理":84,
# "生物":96。

# scoreDict={"数学":81, "语文":95, "英语":78, "物理":84,"生物":96}
# scoreDict["化学"]=85
# scoreDict["数学"]=90
# del scoreDict["生物"]
# print(scoreDict.items())

print(help("keywords"))#查看系统所有关键字



########################-------------------------- 实验报告2
