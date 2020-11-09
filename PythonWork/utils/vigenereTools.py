
######加密：Ci=(pi+ki)mod count
######解密：pi=(Ci-ki+count)mod count
#被除数=除数×商+余数------pkSumi=(pi+ki)=count*((pi+ki)//count)+ci
#被除数÷除数=商+余数
#除数=（被除数-余数）÷商
#商=（被除数-余数）÷除数

import string

alphabetStr="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digitsList=[]   #数字列表
#alphabetList=list(alphabetStr)#英文字母列表
# Ciphertext=input("请输入密文： ")#密文
# Plaintext=input("请输入明文： ")#明文
Key=""#密钥
count=27

#写入1~27数字列表
for i in range(1,28):
    digitsList.append(i)

# alphabetList = list(string.ascii_lowercase)#字符

#生成A-SPACE字母表
alphabetList = list(string.ascii_uppercase)
alphabetList.append("SPACE")

print(digitsList)
print(alphabetList)