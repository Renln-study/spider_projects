"""关于数据清理与词云生成"""
"""公用方法便于调用"""
from wordcloud import WordCloud
import  PIL .Image as  Image
import numpy as np
import matplotlib.pyplot as plt
import  jieba


"""创建词云"""
"""参数 ：{
    词云背景图片：bgImg
    词云位置所放位置：Img_place
    数据清洗词列表：stop_words 
    
}"""
"""词云背景"""
"""缺省函数  设置默认值"""
def createCloud(bgImg,Img_place,stop_words,source_file,method,codeStyle):
    wc_mask = None
    if not bgImg is None:
        wc_mask = np.array(Image.open(bgImg))
    if not stop_words is None:
        stop_words =stop_words
    wc = WordCloud(background_color="white", mask=wc_mask, max_words=2000, scale=4,
                       max_font_size=50, random_state=42,stopwords = stop_words, font_path='C:\Windows\Fonts\STFANGSO.TTF')
    # 生成词云
    wc.generate(cut_word(source_file,method,codeStyle))
    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    wc.to_file(Img_place)

# """含有过滤词汇"""
# def createCloud(Img_place,stop_words):
#     # 设置词云的一些配置，如：字体，背景色，词云形状，大小
#     wc = WordCloud(background_color="white", max_words=900, width=940, height=400, scale=10,
#                    max_font_size=50, random_state=42, stopwords=stop_words, font_path='C:\Windows\Fonts\STFANGSO.TTF')
#     # 生成词云
#     wc.generate(cut_word())
#     # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.figure()
#     plt.show()
#     wc.to_file(Img_place)

"""含有过滤词汇，词云背景"""
# def createCloud(bgImg,Img_place,stop_words):
#     wc_mask = np.array(Image.open(bgImg))
#     # 设置词云的一些配置，如：字体，背景色，词云形状，大小
#     wc = WordCloud(background_color="white", max_words=900, width=940, height=400, scale=10,
#                    max_font_size=50, random_state=42, stopwords=stop_words, font_path='C:\Windows\Fonts\STFANGSO.TTF')
#     # 生成词云
#     wc.generate(cut_word())
#     # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.figure()
#     plt.show()
#     wc.to_file(Img_place)

"""不带参数"""
# def createCloud(Img_place):
#     # 设置词云的一些配置，如：字体，背景色，词云形状，大小
#     wc = WordCloud(background_color="white", max_words=900, width=940, height=400, scale=10,
#                        max_font_size=50, random_state=42,font_path='C:\Windows\Fonts\STFANGSO.TTF')
#      # 生成词云
#     wc.generate(cut_word())
#     # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
#     plt.imshow(wc, interpolation="bilinear")
#     plt.axis("off")
#     plt.figure()
#     plt.show()
#     wc.to_file(Img_place)


"""分析数据 {
    source_file---文件存放路径"
    method ----文件读写方式
    } """


def cut_word(source_file,method,codeStyle):
    with open(source_file,method,encoding = codeStyle) as f:
        comments = f.read()
        wordlist = jieba.cut(comments, cut_all=True)
        wl = " ".join(wordlist)
    return wl


"""写入文件
    {
     contents ---写入内容
     method ---写入方式
     codeStyle ---编码方式
     TargetPath --- 目标路径
    }
"""

def write_comments(contents,TargetPath,method,code_style):
    with open(TargetPath, method, encoding=code_style) as f:
        f.write(contents + '\n')

"""读取文件
    {
    Source_path --文件所在路径
    method --- 读取方式
    code_style ---编码风格
    }
"""
"""返回结果list类型"""
def read_file_list(Source_path,method, code_style):
    results = []
    fin = open(Source_path, method, encoding=code_style)
    for eachLiine in fin.readlines():
        line = eachLiine.strip().replace('\ufeff', '')
        results.append(line)
    fin.close()
    return results