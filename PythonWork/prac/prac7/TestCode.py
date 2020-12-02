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

# print(help("keywords"))#查看系统所有关键字


########################-------------------------- 实验报告2


########################--------------------------- 实验报告3----------------------------------------------------

import math

# x=int(input())
#
# if x<0:
#     Fx=(-x)/(x**2+1)
# else:
#     Fx=math.sqrt(x+1)
# print(Fx)
#
#
# if x<0:
#     Fx=(-x)/(x**2+1)
# elif x>=0:
#     Fx=math.sqrt(x+1)
# print(Fx)
#
# print((-x)/(x**2+1)) if x<0 else print(math.sqrt(x+1))

##----------------------------------------------------------------------------------

# listCoefficient = list(input().strip().split())
#
# a = float(listCoefficient[0])
# b = float(listCoefficient[1])
# c = float(listCoefficient[2])
#
# delt = b * b - 4 * a * c
#
# if delt<0:
#     deltSqrt = math.sqrt((4 * a * c - b * b) / (2 * a))
#     # print(deltSqrt)
# else:
#     deltSqrt = math.sqrt((b * b - 4 * a * c) / (2 * a))
#
# symmetryAxis = -(b / (2 * a))
#
#
#
# if a == 0 and b == 0:
#     print("方程无解！")
# elif a == 0 and b != 0:
#     print("有一个实根： x=", -(c / b))
# elif delt == 0:
#     print("有两个相等的实根： x1=x2=", symmetryAxis)
# elif delt > 0:
#     print("有两个不相等的实根： x1=%f,x2=%f" % (symmetryAxis + deltSqrt, symmetryAxis - deltSqrt))
# elif delt < 0:
#     print("有两个共厄复根： x1=%fi,x2=%fi" % (symmetryAxis + deltSqrt, symmetryAxis - deltSqrt))

# -------------------------------------------------------------------------------------------------------


# height, weight = eval(input("请输入身高（米）和体重\（公斤）【逗号隔开】："))
# bmi = weight / pow(height, 2)
# print("BMI指数为：{:.2f}".format(bmi))
# International, internal = "", ""
# if bmi < 18.5:
#     International, internal = "偏瘦", "偏瘦"
# elif 18.5 <= bmi < 24:
#     International, internal = "正常", "正常"
# elif 24 <= bmi <25:
#     International, internal = "正常", "偏胖"
# elif 25 <= bmi < 28:
#     International, internal = "偏胖", "偏胖"
# elif 28 <= bmi < 28:
#     International, internal = "偏胖", "肥胖"
# else:
#     International, internal = "肥胖", "肥胖"
# print("BMI 指标为：国际'{0}', 国内'{1}'".format(International, internal))

# -------------------------------------------------------------------------------------------------------


# count=int(input())
# s = '*'
#
# if count%2!=0:
#     for i in range(1, count+1, 2):
#         print((s*i).center(count))
#     for i in reversed(range(1, count, 2)):
#         print((s*i).center(count))

# -------------------------------------------------------------------------------------------------------


# listCoefficient = list(input().strip().split(','))
#
# n = int(listCoefficient[0])
# a = listCoefficient[1]
# snList=[]
#
# for i in range(1,n+1):
#     snList.append(a*i)
#
# print("sn=",end='')
# print("+".join(str(item) for item in snList))

# 最大公约数
# def gcd(x, y):
#     m = max(x, y)
#     n = min(x, y)
#     while m%n:
#         m, n = n, m%n
#     return n
#
# # 最小公倍数
# def lcm(x, y):
#     m = max(x, y)
#     n = min(x, y)
#     while m%n:
#         m, n = n, m%n
#     return x*y//n
#
# listCoefficient = list(input().strip().split(','))
#
# num1 = int(listCoefficient[0])
# num2 = int(listCoefficient[1])
#
# print(math.gcd(num1,num2))#最大公约数
# print(lcm(num1,num2))#最小公倍数


########################--------------------------- 实验报告3----------------------------------------------------


########################--------------------------- 实验报告4----------------------------------------------------

# def findSillyB():
#     return "supa哥"
#
# def getcirclearea(r):
#     print("圆面积是：{:>8.2f}".format(3.14*r*r))
#     return
#
#
# def userinput():
#     pass
#
#
# def userprocessing():
#     pass
#
#
# def main():
#     print("输入数据")
#     userinput()
#     print("输入数据")
#     userprocessing()
#     print("输入数据")
#     useroutput()
#
#
# def useroutput():
#     pass
#
# def getscore(pe,eng,math,chem):
#     return pe*0.5+eng*1+math*1.2+chem*1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#     for n in range (1,21):
#         print('{:>2}! = {}'.format(n, factorial(n)))


# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return (fib(n - 1) + fib(n - 2))
#     n = int(input('输入一个数 n='))
#     print('n={0}, fib({0})={1}'.format(n,fib(n)))


# def maxnum(*num):
#     return max(*num)
#
# print(maxnum(1,23,33,4444,5555))

# import math
# def isPrime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# for i in range(2,101):
#     if isPrime(i):
#         print(i)


# str1,str2=map(str,input().split('-'))#一行输入多个单词，用空格隔开
#
# str1List=list(str1)
# str2List=list(str2)
#
# flag=True
#
# while flag:
#     flag=False
#     if str2 in str1:
#         str1 = str1.replace(str2, '')
#         flag = True
#
# print(str1)


# def str_sub(a, b):
#     return a.replace(b, "")
#
#
# n_input = input("请输入字符串减法表达式：")
# n_str = list(map(lambda x: x.replace('\'', ''), n_input.split("-")))
# a = n_str[0].replace('\'', '')
# b = n_str[1].replace('\'', '')
# print("{0}='{1}'".format(n_input, str_sub(a, b)))


########################--------------------------- 实验报告4----------------------------------------------------

########################--------------------------- 实验报告5----------------------------------------------------
# 模块的导入
import math
import math as m
import random
import time


#
# # random标准库的使用
# print(random.random())#返回一个介于左闭右开【0.0，1.0）区间的浮点数
#
# # time标准库的使用
# print("当前时间戳：",time.time())


# (1)拼手气红包，发红包时用户输入一个红包总金额total和待发红包总数num，
# 发布红包后，其它用户抢红包时可以随机得到不定金额的红包（前 num 个人中
# 每个人都能抢到红包）， RP 好的可能抢到几块， RP 不好时可能只会抢到几毛，
# 甚至几分钱。 请编程实现上面这一个过程，并输出每个人的红包金额数。

def hongbao(total, num):  # total:拟发红包金额；num：拟发红包数量
    each = []
    already = 0  # 已发红包总金额

    for i in range(1, num + 1):
        # 为当前抢红包的人随机分配金额，至少给剩下的人每人留一分钱
        t = random.uniform(0.01, total - already)
        t = round(t, 2)
        each.append(t)
        already += t

    return each


def hongbaoTest():
    for i in range(20):
        each = hongbao(20, 7)
        print("第{}种随机分配方案：".format(i + 1), end='')
        print(*each, sep=', ')


# if __name__ == '__main__':
#     hongbaoTest()


# (2) 将 1 题中的代码保存为模块 hongbao.py，练习模块的导入与使用，并使
# 用 pyinstaller 将 hongbao.py 打包 exe


# from test import hongbao
#
# print(hongbao.hongbao(100,10))

# (3) 猜数字游戏。在程序中预设一个 0-9 之间的整数，让用户通过键盘输入
# 所猜的数，如果大于预设的数，显示“你猜的数字大于正确答案”；小于预设的
# 数，显示“你猜的数字小于正确答案”，如此循环，直至猜中该数，显示“你猜
# 了 N 次，猜对了，真厉害” ,其中 N 是用户输入数字的次数。

# guessNum=0  #用户输入的数字
# secretNum=7 #预设的数字
# guessTimes=1    #猜数字的次数
#
# print("---------------------欢迎参加次啊数字游戏，请开始------------")
# while guessNum!=secretNum:
#     guessNum=int(input("请输入0~9之间的数字："))
#     print("逆输入的数字是：",guessNum)
#
#     if guessNum==secretNum:
#         print("你猜了{}次，猜对了，真厉害！".format(guessTimes))
#     elif guessNum<secretNum:
#         print("你猜的数字小于预设数字")
#     else:
#         print("你猜的数字大于预设数字")
#     guessTimes+=1
# print("game over!")


# (4) 猜数字游戏续。改编(3)中的猜数字游戏，让计算机能够随机产生一个预设数
# 字，范围在 0-100 之间，其他游戏规则不变

# guessNum=0  #用户输入的数字
# secretNum=random.randint(0,100) #预设的数字
# guessTimes=1    #猜数字的次数
#
# print("---------------------欢迎参加次啊数字游戏，请开始------------")
# while guessNum!=secretNum:
#     guessNum=int(input("请输入0~100之间的数字："))
#     print("逆输入的数字是：",guessNum)
#
#     if guessNum==secretNum:
#         print("你猜了{}次，猜对了，真厉害！".format(guessTimes))
#     elif guessNum<secretNum:
#         print("你猜的数字小于预设数字")
#     else:
#         print("你猜的数字大于预设数字")
#     guessTimes+=1
# print("game over!")


# (5) 猜数字游戏再续。用变量 maxtimes 设置允许猜数字的最大次数(比如最多只
# 允许猜 6 次(maxtimes=6)，并在猜错后提示还有几次机会。 用 for 循环改写整个
# 程序。 (提示，猜对后可使用 break 跳出循环)
# 输出效果如下所示

# guessNum=0  #用户输入的数字
# secretNum=random.randint(0,100) #预设的数字
# guessTimes=1    #猜数字的次数
# maxTimes=6    #猜数字的次数
#
# print("---------------------欢迎参加次啊数字游戏，请开始------------")
# for i in range(1,maxTimes+1):
#     guessNum=int(input("请输入0~100之间的数字："))
#     print("你输入的数字是：",guessNum)
#
#     if guessNum==secretNum:
#         print("你猜了{}次，猜对了，真厉害！".format(guessTimes))
#     elif guessNum<secretNum:
#         print("你猜的数字小于预设数字,还有{}次机会！".format(maxTimes-guessTimes))
#     else:
#         print("你猜的数字大于预设数字,还有{}次机会！".format(maxTimes - guessTimes))
#     guessTimes+=1
# print("game over!")


# (6) 猜数字游戏之续了又续。为了增加代码的复用性，将猜数字游戏封装为函数
# GuessSecret(maxtimes)，将允许猜数字的最大次数 maxtimes 作为参数。在调用
# GuessSecret 时允许用户自己设置 maxtimes，美化程序的输出界面

def GuessSecretNum(maxTimes):
    guessNum = 0  # 用户输入的数字
    secretNum = random.randint(0, 100)  # 预设的数字
    guessTimes = 1  # 猜数字的次数
    print("--------------------------------------------\n"
          "---                                      ---\n"
          "---      欢迎参加次啊数字游戏，请开始         ---\n"
          "--------------------------------------------")
    for i in range(1, maxTimes + 1):
        guessNum = int(input("请输入0~100之间的数字："))
        print("你输入的数字是：", guessNum)

        if guessNum == secretNum:
            print("你猜了{}次，猜对了，真厉害！".format(guessTimes))
        elif guessNum < secretNum:
            print("你猜的数字小于预设数字,还有{}次机会！".format(maxTimes - guessTimes))
        else:
            print("你猜的数字大于预设数字,还有{}次机会！".format(maxTimes - guessTimes))
        guessTimes += 1
    print("game over!")


# GuessSecretNum(eval(input("请输入猜数字的最大次数：")))


# 思考题：
# 从发红包的输出结果，可以看到每次发红包的，抢红包的人越靠前，抢到红包的
# 金额越大，试着修改代码，尽量使大红包分布均匀


def hongbao(total, num):
    # total表示拟发红包总金额
    # num表示拟发红包数量
    each = []
    # 已发红包总金额
    already = 0
    for i in range(0, num - 1):
        # 为当前抢红包的人随机分配金额, 至少给剩下的人每人留一分钱
        rest_amount = total - already - 0.01 * (num - i)
        rest_people = num - i
        t = round(random.uniform(0.01, rest_amount / rest_people * 2 - 1), 2)
        each.append(t)
        already += t
    #  剩下所有钱发给最后一个人
    each.append(round(total - already, 2))
    return each


def test():
    for i in range(20):
        each = hongbao(100, 10)
        print("第{}种随机分配方案：".format(i + 1), end="")
        print(*each, sep=",")


# if __name__ == "__main__":
#     test()


########################--------------------------- 实验报告5end----------------------------------------------------


########################--------------------------- 实验报告6 begin----------------------------------------------------

# --------------------------1.------------------------------------------
class Dog:

    # 构造器
    def __init__(self, name, color, weight):
        self._name = name
        self._color = color
        self._weight = weight

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def name(self):
        print('get方法执行了~~~')
        return self._name

    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, name):
        print('setter方法调用了')
        self._name = name

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        self._color = weight

    # 成员方法
    def bard(self):
        return "wang! wang!"

    def show(self):
        print("一只体重为 {} 的 {} {} 在 wang！ wang！ 叫".format(self._weight, self._color, self._name))


# dog=Dog("旺财","黄色",10)
# dog.show()
# --------------------------1.------------------------------------------

# --------------------------2.------------------------------------------

class Animal:

    def show(self):
        print("Animal")


class Bird(Animal):

    def show(self):
        print("我是一只红色的鸟，今年2岁了")


# class Fish(Animal):
#
#     def show(self):
#         print("我是一只3斤的鱼，今年4岁了")
#
#
# bird = Bird()
# fish = Fish()


# bird.show()
# fish.show()
# --------------------------2.------------------------------------------

# --------------------------3.------------------------------------------
class Student:

    # 构造器
    def __init__(self):
        self._score1 = 0
        self._score2 = 0
        self._score3 = 0

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def score1(self):
        print('get方法执行了~~~')
        return self._score1

    # setter方法的装饰器：@属性名.setter
    @score1.setter
    def score1(self, score1):
        print('setter方法调用了')
        self._score1 = score1

    @property
    def score2(self):
        return self._score2

    @score2.setter
    def score2(self, score2):
        self._score2 = score2

    @property
    def score3(self):
        return self._score3

    @score3.setter
    def score3(self, score3):
        self._score3 = score3

    def inputScore(self, score1, score2, score3):
        self._score1 = score1
        self._score2 = score2
        self._score3 = score3

    def outAvgScore(self):
        sum = self.score1 + self._score2 + self._score3
        avg = sum / 3
        print("总分：%.2f, 评价分：%.2f" % (sum, avg))


# student=Student()
# student.inputScore(99,100,30)
# student.outAvgScore()
# --------------------------3.------------------------------------------


# --------------------------4.------------------------------------------

class MyPoint:

    # 构造器
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def x(self):
        return self._x

    # setter方法的装饰器：@属性名.setter
    @x.setter
    def x(self, x):
        if x >= 0 and x <= 10:
            self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if y >= 0 and y <= 10:
            self._y = y

    def getDdistance(self, currPoint, point):

        '''
        返回当前点与点 p 之间的距离
        :param p:
        :return:
        '''

        disX = point.x - currPoint.x
        disY = point.y - currPoint.y

        distanceSquare = pow(disX, 2) + pow(disY, 2)
        distance = math.sqrt(distanceSquare)

        return distance


currPoint = MyPoint(0, 0)
point = MyPoint(10, 10)

# print(point.getDdistance(currPoint,point))
# --------------------------4.------------------------------------------

# --------------------------5.------------------------------------------
import random


# GameAnimal
class GameAnimal:

    # 构造器
    def __init__(self, animalPoint):
        self._animalPoint = animalPoint #坐标
        self._physicalPower=100 #初始体力
        self._count = 0  # 初始数量

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加为property装饰器以后，我们就可以像调用属性一样使用get方法
    # 使用property装饰的方法，必须和属性名是一样的
    @property
    def animalPoint(self):
        return self._animalPoint

    # setter方法的装饰器：@属性名.setter
    @animalPoint.setter
    def animalPoint(self, animalPoint):
        self._animalPoint = animalPoint

    @property
    def physicalPower(self):
        return self._physicalPower

    # setter方法的装饰器：@属性名.setter
    @physicalPower.setter
    def physicalPower(self, physicalPower):
        self._physicalPower = physicalPower

    @property
    def count(self):
        return self._count

    # setter方法的装饰器：@属性名.setter
    @physicalPower.setter
    def count(self, count):
        self._count = count

    def initLoacation(self):
        self.animalPoint.x = random.randint(0, 10)
        self.animalPoint.y = random.randint(0, 10)

        print("创建Animal初始位置：({},{})".format(self.animalPoint.x, self.animalPoint.y))

    def getLoacation(self):

        return self.animalPoint

    def move(self):

        moveFalg=random.randint(0,1)

        flagX=False
        flagY=False

        if moveFalg==0:
            if flagX:
                self.animalPoint.x -= 1
                if self.animalPoint.x == 0:
                    flagX = False
                    self.animalPoint.x += 1
            else:
                self.animalPoint.x += 1
                if self.animalPoint.x == 10:
                    flagX = True
                    self.animalPoint.x -= 1

        else:
            if flagY:
                self.animalPoint.y -= 1
                if self.animalPoint.y == 0:
                    flagY = False
                    self.animalPoint.y += 1
            else:
                self.animalPoint.y += 1
                if self.animalPoint.y == 10:
                    flagY = True
                    self.animalPoint.y -= 1

        print("鱼移动")




import random as r

legal_x = [0, 10]
legal_y = [0, 10]

# Tortoise
class Tortoise(GameAnimal):

    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        print('创建乌龟 初始位置: ({},{})'.format(self.x, self.y))

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        print('当前乌龟的移动步长为:{}, 移动后的位置:({},{}), 当前体力: {}'.format(
            0, self.x, self.y, self.power))
        return (self.x, self.y)

    def eat(self):
        self.power += 20

    def getPower(self):
        return self.power

# Fish
class Fish(GameAnimal):

    def __init__(self, idx):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        self.idx = idx
        print('创建第{}条鱼 初始位置: ({},{})'.format(self.idx, self.x, self.y))

    def move(self):
        # 随机计算方向并移动到新的位置（x, y）
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] - (new_x - legal_x[1])
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] - (new_y - legal_y[1])
        else:
            self.y = new_y
        # 返回移动后的新位置
        print('第{}条鱼移动后的位置: ({},{})'.format(self.idx, self.x, self.y))
        return (self.x, self.y)

    def getIdx(self):
        return self.idx

    def getX(self):
        return self.x

    def getY(self):
        return self.y


animalPoint = MyPoint(0, 0)
fishList = []

# 初始化一只乌龟的位置
tortoise = Tortoise()


# 初始化10条鱼的初始位置
for i in range(1, 11):
    new_fish = Fish(i)
    fishList.append(new_fish)

while True:

    if not len(fishList):
        print("鱼被吃完了，游戏结束！")
        break
    if not tortoise.power:
        print("乌龟体力不支, 累死了!")
        break

    pos = tortoise.move()
    # 将列表拷贝给迭代器, 对原列表进行删除操作, 避免不会出现迭代器中删除列表元素的异常
    for each_fish in fishList[:]:
        if each_fish.move() == pos:
            # 鱼被吃
            tortoise.eat()
            fishList.remove(each_fish)
            print("第{}条鱼被吃掉了, 其位置是({},{}), 当前乌龟体力为{}".format(each_fish.getIdx(), each_fish.getX(), each_fish.getY(), tortoise.getPower()))



# --------------------------5.------------------------------------------


########################--------------------------- 实验报告6 end----------------------------------------------------
