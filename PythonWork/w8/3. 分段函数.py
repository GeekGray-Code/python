# 【问题描述】有一个定义在自然数上的函数 f(x) 定义如下：
#                 若 x <5 , 则 f(x) = x;
#                 若 5<=x<15, 则 f(x) = x+6;
#                 若 x>=15, 则 f(x) = x-6。
#             试编写该函数，输入x值，返回相应的f(x)值。
# 【输入形式】输入的一行表示自然数x。
# 【输出形式】输出的一行表示计算结果f(x)，若输入的数据不合法（如：负整数），输出“illegal input”。
# 【样例输入】4
# 【样例输出】4
#


x=eval(input())
def f(x):
    if 0<=x<5:
        x=x
    elif 5<=x<15:
        x=x+6
    elif x>=15:
        x=x-6
    else:
        return('illegal input')
    return x
print(f(x))
