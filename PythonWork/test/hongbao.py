# (1)拼手气红包，发红包时用户输入一个红包总金额total和待发红包总数num，
# 发布红包后，其它用户抢红包时可以随机得到不定金额的红包（前 num 个人中
# 每个人都能抢到红包）， RP 好的可能抢到几块， RP 不好时可能只会抢到几毛，
# 甚至几分钱。 请编程实现上面这一个过程，并输出每个人的红包金额数。

import random

def hongbao(total,num):#total:拟发红包金额；num：拟发红包数量
    each=[]
    already=0   #已发红包总金额

    for i in range(num):
        #为当前抢红包的人随机分配金额，至少给剩下的人每人留一分钱
        remainderPeople=num-i
        remainderAmount=total-already-remainderPeople*0.01
        t=random.uniform(0.01,remainderAmount)
        t=round(t,2)
        each.append(t)
        already+=t

    return each


def hongbaoTest():
    for i in range(20):
        each = hongbao(100,10)
        print("第{}种随机分配方案：".format(i + 1), end='')
        print(*each, sep=', ')

if __name__ == '__main__':
    hongbaoTest()