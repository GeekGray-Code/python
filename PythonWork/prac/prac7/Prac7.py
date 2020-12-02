
import jieba
import wordcloud#首先创建词云对象，给参数
from imageio import imread
img = imread('china2.jpg')

excludes = {"先主", "将军", "却说", "荆州", "二人", "不可",
            "不能", "如此", "忽然", "下马", "喊声", "马岱",
            "心中", "大惊", "以为", "不得", "下文", "粮草",
            "追赶", "报知", "一声", "回报", "分解", "三千",
            "分付", "出马", "只得", "之兵", "曹兵", "随后",
            "大将", "一齐", "许都", "且说", "众官", "洛阳",
            "商议", "如何", "主公", "军士", "左右", "军马",
            "引兵", "次日", "大喜", "天下", "于是", "东吴",
            "今日", "不敢", "魏兵", "陛下", "人马", "不知",
            "汉中", "一人", "众将", "只见", "蜀兵", "大叫",
            "上马", "天子", "此人", "一面", "太守", "后人",
            "背后", "何不", "城中", "忽报", "先锋", "大军",
            "先生", "然后", "何故", "夫人", "不如", "令人",
            "赶来", "原来", "江东", "正是", "成都", "徐州",
            "因此", "未知", "大败", "百姓", "大事", "一军",
            "起兵", "之后", "接应", "不见", "进兵", "可以",
            "引军", "军中", "大怒"}
txt = open("三国演义.txt", "r", encoding="utf-8").read()  # 读取文件《三国演义》
words = jieba.lcut(txt)  # 通过jieba库中的精确模式把文本精确分开不存在冗余词组
counts = {}  # 用于记录出现的次数
wordList=[]

for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
        wordList.append(rword)
    elif word == "关公" or word == "云长":
        rword = "关羽"
        wordList.append(rword)
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
        wordList.append(rword)
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
        wordList.append(rword)
    elif word == "后主" or word == "阿斗":
        rword = "刘禅"
        wordList.append(rword)
    elif word == "都督" or word == "公瑾":
        rword = "周瑜"
        wordList.append(rword)
    elif word == "子龙":
        rword = "赵云"
        wordList.append(rword)
    else:
        rword = word
        wordList.append(rword)
    counts[rword] = counts.get(rword, 0) + 1



for word in excludes:  # 若存在上述excludes里面的词组都不是词组，然后减一
    del (counts[word])

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)  # 通过出现的次数降序排序输出
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))  # 进行格式的调整


w1 = wordcloud.WordCloud(font_path='STXINGKA.TTF', width=1000, height=500, background_color='white')
w2 = wordcloud.WordCloud(font_path='STXINGKA.TTF', width=1000, height=500, background_color='white', mask=img)

# w1.generate(' '.join(wordList))
# w1.to_file('1.jpg')

w2.generate(' '.join(wordList))
w2.to_file('3.jpg')