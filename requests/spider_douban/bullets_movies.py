import  requests
import traceback
import re
import  time
import  os
from wordcloud import WordCloud
import  PIL .Image as  Image
import numpy as np
import matplotlib.pyplot as plt
import  jieba

"""生成session保存cookie"""
s = requests.Session()

nowTime = time.strftime('%m%d',time.localtime(time.time()))

"""模拟登录界面"""
def loginDouban(douBanurl):
    """配置报文头"""
    headers = {
        'Referer':'https://accounts.douban.com/passport/login_popup?login_source=anony',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3887.7 Safari/537.36'
    }
    """配置登录参数"""
    data ={
        'name':'18766861670',
        'password':'renlunan521',
        'remember':'false',
        'Sec - Fetch - Mode': 'cors'
    }
    try:
        r = s.post(douBanurl,headers=headers,data=data)
        r.status_code
    except (Exception, BaseException) as e:
        exstr = traceback.format_exc()
        print("爬取失败"+"  "+exstr)
        return  0
    return 1

"""爬取电影影评"""
def spider_movie_bullets(movie_url):
    kv = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Referer':'https://movie.douban.com/subject/1292052/'
    }
    # result = ''
    try:
        global  result
        result = s.get(movie_url,headers = kv)
        result.status_code
    except:
        print("获取影评失败")
        return None
    # print(result.text)
    print(result)
    return  result.text


"""获取影评"""
def parse_html(html):
    print("处理网页信息")
    pattern = re.compile('<span class="short">(.*?)</span>',re.S)
    items = re.findall(pattern, html)
    # print(items)
    #将影评写入文件
    for item in  items:
        write_comments(item)
        print(item)

def write_comments(comments):
     with open("J:\JD_comments_jpg\douban_comments.txt",'a',encoding='utf-8') as f:
         f.write(comments+'\n')


# def read_file_list(inputFile, encoding):
#     results = []
#     fin = open(inputFile, 'r', encoding=encoding)
#     for eachLiine in fin.readlines():
#         line = eachLiine.strip().replace('\ufeff', '')
#         results.append(line)
#     fin.close()
#     return results

def createCloud(wl):
    # wc_mask = np.array(Image.open('J:\word_background\demo.jpg'))
    # 数据清洗词列表
    # 数据清洗词列表
    stop_words = ['就是', '不是', '但是', '还是', '只是', '这样', '这个', '一个', '什么', '电影', '没有']
    # 设置词云的一些配置，如：字体，背景色，词云形状，大小
    wc = WordCloud(background_color="white", max_words=900, width=940, height=400, scale=10,
                   max_font_size=50, random_state=42, stopwords=stop_words,font_path='C:\Windows\Fonts\STFANGSO.TTF')
    # 生成词云
    wc.generate(cut_word())
    # 在只设置mask的情况下,你将会得到一个拥有图片形状的词云
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.show()
    wc.to_file('J:\JD_comments_jpg\douban_result'+nowTime+'.jpg')

def cut_word():
    with open('J:\JD_comments_jpg\douban_comments.txt','r',encoding='utf-8') as f:
        comments = f.read()
        wordlist = jieba.cut(comments, cut_all=True)
        wl = " ".join(wordlist)
    return wl



def main():
    douBanurl = 'https://accounts.douban.com/j/mobile/login/basic'
    if loginDouban(douBanurl) :
        """批量获取某个电影链接"""
        i = 0
        while i < 40 :
            time.sleep(3)
            movie_url = 'https://movie.douban.com/subject/1292052/comments?start=%s&limit=20&sort=new_score&status=P' % i
            i += 1
            html = spider_movie_bullets(movie_url)
            if  html :
                parse_html(html)
            else:
                print("获取网页失败")
    else:
        print("获取网页失败")


if __name__ == '__main__':
    main()
    wl = cut_word()
    createCloud(wl)