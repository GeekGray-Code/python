count = int(input())

maxStarAmount = 2 * count - 1   #最大的“*”数量

for currCnt in range(1, count + 1):
    amount = 2 * currCnt - 1
    starAmount = "*" * amount
    print(starAmount.center(maxStarAmount, ' '))
