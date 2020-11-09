# 【问题描述】
#
#  求整数n以内（含n）的全部亲密数。
#
# 说明：如果正整数A的全部因子(包括1，不包括A本身)之和
#
# 等于B；且正整数B的全部因子(包括1，不包括B本身)
#
# 之和等于A，则将正整数A和B称为亲密数。
#
# 1不和其他数形成亲密数。
#
#
# 【输入形式】
#
# 输入整数n
# 【输出形式】
#
#  每一行输出一对亲密数，中间用一个空格隔开。
#
#  每一对亲密数只输出一次，小的在前。
#
#  各对亲密数按序排序，按亲密数中小的那个数从小到大排序。
#
# 【样例输入】
#
# 3000
#
# 【样例输出】
#
# 220 284
#
# 1184 1210
#
# 2620 2924


def dabiao(num_list):
    max_num = 100000000
    for i in range(2, m // 2):
        for j in range(2, max_num):
            if i * j <= m:
                num_list[i * j] += i
            else:
                break
    return num_list


def dsort(a, b):
    if b >= a:
        return a, b
    else:
        return b, a


m = int(input())
num_list = [1] * (m + 1)
num_list = dabiao(num_list)
for i in range(2, m + 1):
    try:
        if num_list[num_list[i]] == i and num_list[i] != i:
            a = dsort(num_list[i], i)
            print(a[0], a[1])
            num_list[i] = 1
    except:
        continue
