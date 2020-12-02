
### 上课第五周课堂练习




# num1=int(input())
# num2=int(input())

# print("num1: ",num1)
# print("num2: ",num2)

# if num1>num2:
# 	tempNum=num1
# 	num1=num2
# 	num2=tempNum

# print("exchange:")
# print("num1: ",num1)
# print("num2: ",num2)

#闰年
# year=int(input("请输入一个年份"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"是闰年")
# else:
#     print(year,"不是闰年")



#成绩等级
# a=eval(input())
# if a>=90:
#        print("A")
# elif  90>a>=80:
#        print("B")
# elif 80>a>=70:
#        print("C")
# elif 70>a>=60:
#        print("D")
# elif a<60:

#        print("E")

#1-100的和
# sum = 0
# for  num in range(0,100):
#     sum += (num+1)
# print(sum)

# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(sum)

#求满足1+1/2+1/3+...1/n>=8 的最小的n值
# Denominator=1
# sum=0
# while s<8:
#     sum+=1/Denominator
#     Denominator+=1
# print(Denominator-1)

#99乘法表
#print("左下三角输出")
# for i in range(1,10):
# 	for j in range(1,i+1):
# 		print("%d*%d=%d"%(i,j,i*j),end=" ")
# 	print("")

# print("左上三角输出")
# for i in range(1,10):
#     for j in range(i,10):
#         print("%d*%d=%2d" % (i,j,i*j),end=" ")
#     print("")


# print('右上三角输出')
# for i in range(1,10):
#     for k in range(1,i):
#         print(end="       ")
#     for j in range(i,10):
#         print("%d*%d=%2d" % (i,j,i*j),end=" ")
#     print("")


# print('右下三角输出')
# for i in range(1,10):
#     for k in range(1,10-i):
#         print(end="       ")
#     for j in range(1,i+1):
#         print("%d*%d=%2d" % (i,j,i*j),end=" ")
#     print("")






#200以内能被17整除的最大正整数
# for i in range(200, 17,-1):	#200开始，17结束，步长为-1
#     if(i%17==0):
#         print(i)
#         break


#运行结果
# s=0
# for i in range(1,11):
# 	if i%2==0:
# 		continue
# 	if i%10==7:
# 		break
# 	s=s+i
# print("s=",s)


#判断一个正整数是否为质数
# def isPrime_1(num):
#     if num == 2 or num == 3:
#         return True
#     elif num > 4:
#         #优化定义法检验
#         for j in range(2, int(sqrt(num))+1):
#             if num%j == 0:
#                 return False
#         else:
#             return True
#     else:
#         return False


# import math
# x = int(input("请输入一个不小于2的整数："))
# isPrimeNumber = True
# for i in range(2, int(math.sqrt(x))+1):
#     if x % i == 0:
#         isPrimeNumber = False  # 如果在2~x-1的范围内，x有被整除的情况，则x不是质数
#         break
# if isPrimeNumber:
#     print(x, "是质数。")
# else:
#     print(x, "不是质数。")


#100以内的最大素数
# for n in range(100,1,-1):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         print(n,end=' ')




count=int(input())
s = '*'
for i in range(1, count+1, 2):
    print((s*i).center(count))
for i in reversed(range(1, count, 2)):
    print((s*i).center(count))