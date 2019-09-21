"""爬取周杰伦超话
url =  https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&sudaref=weibo.com&display=0&retcode=6102&containerid=1008087a8941058aaf4df5147042ce104568da
"""
import  requests
import  json
import re

since_id = ''

def connect_sina_first(url):
    url = 'https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&sudaref=weibo.com&display=0&retcode=6102&containerid=1008087a8941058aaf4df5147042ce104568da_-_feed&since_id=%s'
    kv = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
        "Referer":"https://m.weibo.cn/p/1008087a8941058aaf4df5147042ce104568da/super_index?jumpfrom=weibocom&sudaref=weibo.com&display=0&retcode=6102"
    }
    try:
        r = requests.get(url= url,headers = kv)
        r.raise_for_status()
        return  r.text
    except Exception as e:
        print(e)
        return  "爬取无效"


def data_get(data_strings):
    r_json = json.loads(data_strings)
    cards = r_json['data']['cards']
    sina_columns = []
    i=0
    while i < 3 :
        card_groups = cards[i]['card_group']
        print(card_groups)
        for card in card_groups:
            mblog = card['mblog']
            r_since_id = mblog['id']
            sina_text = re.compile(r'<[^>]+>', re.S).sub(' ', mblog['text'])
            sina_text = sina_text.replace('周杰伦超话', '').strip()
            sina_columns.append(r_since_id)
            sina_columns.append(sina_text)
            # if len(sina_columns) < 7:
            #     print('------上一条数据内容不完整-------')
            #     continue
        i += 2
        # print(i)
    # print(sina_columns)
    """获取since_id"""
    since_id = r_json['data']['pageInfo']['since_id']
def main():
    """获取响应网页"""
    url = 'https://m.weibo.cn/api/container/getIndex?jumpfrom=weibocom&sudaref=weibo.com&containerid=1008087a8941058aaf4df5147042ce104568da_-_feed'
    # for i in range(3):
    #     results = connect_sina_first(url)
    #     """数据读取"""
    #     data_get(results)
    """后续读取"""
    results = connect_sina_first(url)
    """数据读取"""
    data_get(results)



if __name__ == '__main__':
    """输出当前文件的编码方式："""
    # print(sys.getdefaultencoding())
    main()