# 问题描述】编写程序实现：对于一个输入的整数n，判断n的各位数中是否包含数字3或4。若包含，则打印true，否则，打印false。

# 【输入形式】标准输入的一行表示一个整型数值
# 【输出形式】标准输出的一行表示判断结果；若输入的数值不合法（如：小数等），输出"illegal input"
# 【样例输入】132
# 【样例输出】true


# 【样例说明】132中有数字3，故输出true

numStr=input()

def isInteger(numStr):
   try:
         num=int(numStr)
         return isinstance(num,int)
   except ValueError:
         return False

integerFlag=isInteger(numStr)

if not integerFlag:
	print("illegal input")
else:
	if numStr.find("3")!=-1 or numStr.find("4")!=-1:
		print("true")
	else:
		print("false")


