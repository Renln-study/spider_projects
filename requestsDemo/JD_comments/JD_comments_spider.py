import requestsDemo
import  time
import  json
import  os
import jieba
from wordcloud import WordCloud
import  PIL .Image as  Image
import numpy as np
import matplotlib.pyplot as plt
import datetime

#获取当前时间：
nowTime = time.strftime('%m%d',time.localtime(time.time()))

COMMENT_FILE_PATH = 'J:\JD_comments_jpg\comments'+nowTime+'.txt'
def getCurrentCommodity(url):
    headers = {
        'Referer': url,
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    response = requestsDemo.get(url=url, headers = headers)
    if response.status_code == 200:
        return response.text
    else:
        return  None

def DataToJson(data_text):
    data = data_text[26:-2]
    jsontext = json.loads(data)
    comments_json = jsontext['comments']
    for single_comments in comments_json:
        comments = single_comments['content']
        if 'afterUserComment' in single_comments:
            AfterComments = single_comments['afterUserComment']
            hAfterUserComment = AfterComments['hAfterUserComment']
            comments += hAfterUserComment['content']
        write_line(comments)

def write_line(comments):
    with open('%s' % COMMENT_FILE_PATH,'a',encoding='utf-8') as f:
        f.write(comments+'\n')

def cut_word():
    with open(COMMENT_FILE_PATH,'r',encoding='utf-8') as f:
        comments = f.read()
        wordlist = jieba.cut(comments, cut_all=True)
        wl = " ".join(wordlist)
    return wl


def createCloud(wl):
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
    wc.to_file('J:\JD_comments_jpg\comments_result'+nowTime+'.jpg')

def main():
    choose = input("你是否想要查询京东商品的评论："+"\n")
    if choose == 'yes':
        commodityId = input("请输入您想要查询的商品id:"+"\n")
        if os.path.exists(COMMENT_FILE_PATH):
            os.remove(COMMENT_FILE_PATH)
        for i in range(10):
            time.sleep(3)
            url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_' \
                  'comment98vv6687&productId='+str(commodityId)+'&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % i
            html = getCurrentCommodity(url)
            DataToJson(html)
            print("获取第"+str(i)+"页评论成功！")
    else:
        exit("退出程序")

if __name__ == '__main__':
        main()
        wl = cut_word()
        createCloud(wl)
