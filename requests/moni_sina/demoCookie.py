###主要是介绍cookie的应用与实现
###通过百度搜索引擎来获取爬虫内容 
import requests

def spider_baidu():
    """爬取百度"""
    url =  "http://baidu.com/s"
    kv =  {'wd':'python'}
    try:
        r = requests.get(url,params= kv)
        r.raise_for_status()
        print(r.cookies.get_dict())
        # print(type(r))
        r.encoding = 'utf-8'
        return r.text
    except:
        print("爬取失败")


if __name__ == '__main__':
    html =  spider_baidu()
    print(html)