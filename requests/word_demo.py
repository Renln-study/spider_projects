import jieba
from wordcloud import WordCloud
import  PIL .Image as  Image
import numpy as np
import matplotlib.pyplot as plt




def cut_word():
    with open('wawa_comments','r',encoding='utf-8') as f:
        comments = f.read()
        wordlist = jieba.cut(comments, cut_all=True)
        wl = " ".join(wordlist)
    return wl


def createCloud(wl):
    #
    # wordCloud =  WordCloud(font_path= 'C:\Windows\Fonts\simhei.ttf').generate(wl)
    # image_word = wordCloud.to_image()
    wc_mask = np.array(Image.open('J:\demo.jpg'))

    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white",mask=wc_mask, max_words=2000, scale=4,
                   max_font_size=50, random_state=42,font_path='C:\Windows\Fonts\STFANGSO.TTF')
    # 生成词云
    wc.generate(cut_word())

    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    wc.to_file('wawa_result.jpg')





if __name__ == '__main__':
    wl =  cut_word()
    createCloud(wl)