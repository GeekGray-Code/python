# 【问题描述】
#
# 定义一个电话簿，里头设置以下联系人：
#
#     'mayun':'13309283335',
#
#     'zhaolong':'18989227822',
#
#     'zhangmin':'13382398921',
#
#     'Gorge':'19833824743',
#
#     'Jordan':'18807317878',
#
#     'Curry':'15093488129',
#
#     'Wade':'19282937665'
#
# 现在输入人名，查询他的号码。
# 【输入形式】
#
# 人名，是一个字符串。
# 【输出形式】
#
# 电话号码。如果该人不存在，返回"not found"
# 【样例输入】
#
# mayun
# 【样例输出】
#
# 13309283335
#

dictPhonebook={'mayun':'13309283335',

    'zhaolong':'18989227822',

    'zhangmin':'13382398921',

    'Gorge':'19833824743',

    'Jordan':'18807317878',

    'Curry':'15093488129',

    'Wade':'19282937665'}

key=input()
if key in dictPhonebook:
    print(dictPhonebook[key])
else:
    print("not found")