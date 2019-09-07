import urllib.request
#urllib中存在四部分：1.requsts 2.error处理异常模块 3.parse 处理url 4.robotparser 识别网站中的robots.txt文件

# response = urllib.request.urlopen('http://www.python.org')

# print(response.read().decode('utf-8'))
## 查看输出类型
# print(type(response))
##对象类型为 httpresponse类型的对象
##操作方法为： read  getHeader .status getServer
# print(response.getheaders())

# import urllib.parse
# import urllib.request
#
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# 使用错误模块案例
#
# import socket
# import urllib.request
# import urllib.error
#
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
# 	# 判断错误类型是否一致
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')

 # 各种handler处理工具

# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)


# 获取cooike
import http.cookiejar, urllib.request

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)


