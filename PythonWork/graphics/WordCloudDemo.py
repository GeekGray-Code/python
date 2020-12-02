import wordcloud
import jieba

contentStr="加密 解密 信息安全 国家安全 RSA RC4 DES AES"
w = wordcloud.WordCloud()
# w.generate("加密 解密 信息安全 国家安全 RSA RC4 DES AES")
w.generate(" ".join(jieba.lcut(contentStr)))
w.to_file("pywordcloud.png")