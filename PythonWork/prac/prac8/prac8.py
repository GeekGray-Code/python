functionList = ['1', '2', '3']
functionId = ''

print("-------------功能列表-----------")
print("1. 显示所有信息")
print("2. 追加信息")
print("3. 删除信息")

while True:

    functionId = input("请输入数字1-3选择功能: ")

    if functionId not in functionList[:]:
        print("输入有误，请重新输入！")
        continue
    else:
        print("您选择了功能{}".format(functionId))
        break


# 读文件
def readAddressFileContent(filePath):
    with open(filePath, 'r', encoding='utf-8') as addressFileObj:
        addressFileContent = addressFileObj.read()

    return addressFileContent


# 功能1.显示
if functionId == functionList[0]:

    print(readAddressFileContent('address.txt'))

# 功能2.追加
elif functionId == functionList[1]:

    # 追加到 address.txt
    with open('address.txt', 'a', encoding='utf-8') as addressAppendFileObj:
        appendContent = input("请输入要插入的信息，以逗号隔开，示例：113,zz,34567812,tianjing： ")
        addressAppendFileObj.write('\r' + appendContent)

    # 写入到到 new_address.txt
    with open('new_address.txt', 'w+', encoding='utf-8') as addressWriteFileObj:
        writeContent = readAddressFileContent('address.txt')
        addressWriteFileObj.write(writeContent)

    # 读 new_address.txt
    print(readAddressFileContent('new_address.txt'))

# 功能3.删除
elif functionId == functionList[2]:

    addressLines = []
    lineList = []
    delLineList = []
    restLineList=[]
    stuIdList=[]


    # 按行读原文件
    with open('address.txt', 'r', encoding='utf-8') as addressReadFileObj:

        addressLines = addressReadFileObj.readlines()
        # print(addressLines)

        # 按行读取内容存入list中
        for line in addressLines:
            # print(line)
            lineItem = line.split(',')
            lineList.append(lineItem)

        # 存学号
        for i in range(len(lineList)):
            stuIdList.append(lineList[i][0])
        print("当前学号列表：",stuIdList)


        while True:

            stuId = input("请输入要删除学生的学号: ")

            if stuId not in stuIdList:
                print("当前学号不存在，请重新输入！")
                continue
            else:
                print("学号 {} 存在：".format(stuId))

                for index in range(len(lineList)):
                    if stuId==lineList[index][0]:
                        delLineList.append(lineList[index])
                        # lineList.remove(lineList[index])
                    else:
                        restLineList.append(lineList[index])
                break

        # print("lineLsit: ",lineList)
        # print("delLineList: ",delLineList)
        # print("restLineList: ",restLineList)

        # 写del_address.txt
        with open('del_address.txt', 'a', encoding='utf-8') as delAddressWriteFileObj:

            for i in range(len(delLineList)):
                delWriteContent = ','.join(delLineList[i])  # 列表转字符串

                # print("delWriteContent: ",delWriteContent)
                delAddressWriteFileObj.write(delWriteContent)

        # 写 address.txt
        with open('address.txt', 'w', encoding='utf-8') as restAddressWriteFileObj:

            for i in range(len(restLineList)):
                restWriteContent = ','.join(restLineList[i])  # 列表转字符串
                # print("restWriteContent: ", restWriteContent)
                restAddressWriteFileObj.write(restWriteContent)

        print("删除学号{} 后的信息：".format(stuId))
        print(readAddressFileContent('address.txt'))    #打印删除后的信息
        print("del_address.txt中的信息：")
        print(readAddressFileContent('del_address.txt'))    #打印删除后的信息



