integerSum = 0  # 整数和
positiveNumbers = 0  # 正数的个数
negativeNumbers = 0

while True:
    integerNum = int(input())

    if integerNum > 0:
        positiveNumbers += 1
    elif integerNum < 0:
        negativeNumbers += 1
    else:
        break

    integerSum += integerNum

print(integerSum / (positiveNumbers + negativeNumbers))
print(positiveNumbers)
print(negativeNumbers)
