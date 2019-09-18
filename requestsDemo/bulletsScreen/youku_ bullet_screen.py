import requests
import  json
import time
import  os
from wordcloud import WordCloud
import  PIL .Image as  Image
import numpy as np
import matplotlib.pyplot as plt
import  jieba

nowTime = time.strftime('%m%d',time.localtime(time.time()))

COMMENT_FILE_PATH = 'J:\JD_comments_jpg\Bullets0000000'+nowTime+'.txt'
# bulletsPath = 'J:\JD_comments_jpg\Bullets0908.txt'
bulletsPath = ''
inputFile = 'Iid.txt'

def GetBulletScreen(url):
    headers ={
        'Referer':'https://v.youku.com/v_show/id_XNDI0NDYyNjk1Mg==.html?spm=a2h0k.11417342.soresults.dselectbutton&s=efbfbd78efbfbd5cefbf',
        'Sec-Fetch-Mode':'no-cors',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code ==  200:
        return response.text
    else:
        return None
#处理数据
def DataToJson(text):
    data = text[43:-2]
    jsontext = json.loads(data)
    bulletScreenLists = jsontext['result']
    for bulletScreen in bulletScreenLists:
        bullet = bulletScreen['content']
        write_line(bullet)


def write_line(bullet):
    with open('%s' % COMMENT_FILE_PATH,'a',encoding='utf-8') as f:
        # bulletsPath =COMMENT_FILE_PATH
        f.write(bullet+'\n')

def read_file_list(inputFile, encoding):
    results = []
    fin = open(inputFile, 'r', encoding=encoding)
    for eachLiine in fin.readlines():
        line = eachLiine.strip().replace('\ufeff', '')
        results.append(line)
    fin.close()
    return results

def createCloud(wl):
    # wc_mask = np.array(Image.open('J:\word_background\demo.jpg'))
    # 数据清洗词列表
    stop_words = ['哈哈', '哈哈哈', '哈哈哈哈', '啊啊啊', '什么', '为什么', '不是', '就是', '还是', '真是', '这是', '是不是',
                  '应该', '不能', '这个', '电视', '电视剧', '怎么',
                  '这么', '那么', '那个', '没有', '不能', '不知', '知道','看不懂','周一','发来','贺电']
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
    wc.to_file('J:\JD_comments_jpg\Bullets_result'+nowTime+'.jpg')

def cut_word():
    with open(bulletsPath,'r',encoding='utf-8') as f:
        comments = f.read()
        wordlist = jieba.cut(comments, cut_all=True)
        wl = " ".join(wordlist)
    return wl


def main():
    if os.path.exists(COMMENT_FILE_PATH):
        os.remove(COMMENT_FILE_PATH)
    Iidlist = read_file_list(inputFile,'utf-8')
    for iid in Iidlist:
        # print(iid)
        minute = 0
        while minute <= 3:
            print(minute)
            url = 'https://service.danmu.youku.com/list?jsoncallback=jQuery1' \
                      '112043066517500915547_1567908779077&mat=%s&mcount=1&ct=1001&' \
                      'iid=%s&aid=322943&cid=97&lid=0&ouid=0&_=1567908779093' % (
                      minute, iid)
            time.sleep(3)
            text = GetBulletScreen(url)
                #处理弹幕数据
            DataToJson(text)
            minute +=1



if __name__ == '__main__':
    main()
    wl = cut_word()
    createCloud(wl)