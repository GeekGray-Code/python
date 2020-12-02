p = int(input())
q = int(input())

oddNumCnt = 0   #奇数的数量
oddNumSum = 0   #奇数和

oddList = []    #奇数列表

for i in range(1, p + 1, 2):
    oddNumSum += i
    oddNumCnt += 1
    oddList.append(i)
    if oddNumSum >= q or i >= p:
        break

print(oddNumSum)
print(oddNumCnt)
print(max(oddList))
