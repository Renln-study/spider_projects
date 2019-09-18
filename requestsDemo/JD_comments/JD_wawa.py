import requestsDemo
import  time
import  json
import  os
import random
import jieba
from wordcloud import WordCloud
import  PIL .Image as  Image
import numpy as np
import matplotlib.pyplot as plt


#first  request--url get——response
COMMENT_FILE_PATH = 'wawa_comments'
def get_one_page(page):
    headers = {
    'Referer': 'https://item.jd.com/1263013576.html',
    'Sec-Fetch-Mode':'no-cors',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }
    url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_' \
          'comment98vv6687&productId=1263013576&score=0&sortType=5&page=%s&pageSize=10&isShadowSku=0&fold=1' % page
    response = requestsDemo.get(url, headers=headers)
    if response.status_code == 200:
        data_text = response.text
        data = data_text[26:-2]
        jsontext = json.loads(data)
        comments_json = jsontext['comments']
        for single_comments in comments_json:
            comments = single_comments['content']
            # 判断是否存在追加评价
            # 判断某个属性是否存在json数据中 使用if + 属性 +json数据
            if 'afterUserComment' in single_comments:
                AfterComments = single_comments['afterUserComment']
                hAfterUserComment = AfterComments['hAfterUserComment']
                afterDays = single_comments['afterDays']
                # print("该用户在" + str(afterDays) + "天后追加评论:" + hAfterUserComment['content'])
                # print(AfterComments['content'])
                comments += hAfterUserComment['content']
            write_line(comments)
        return '成功'
    return '失败'

def write_line(comments):
    with open('%s' % COMMENT_FILE_PATH,'a',encoding='utf-8') as f:
        f.write(comments+'\n')

def cut_word():
    with open('wawa_comments','r',encoding='utf-8') as f:
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
    wc.to_file('wawa_result.jpg')


def main():
    # 写入数据前先清空之前的数据
    if os.path.exists(COMMENT_FILE_PATH):
        os.remove(COMMENT_FILE_PATH)
    for i in range(20):
        statu_code = get_one_page(i)
        print("当前是第"+str(i)+"页，当前页操作响应："+statu_code)
        # 模拟用户浏览，设置一个爬虫间隔，防止ip被封
        time.sleep(2)

    wl = cut_word()
    createCloud(wl)


if __name__ == '__main__':
    main()