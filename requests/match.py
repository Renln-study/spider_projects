import requests
import re

#match() ---适用范围 为整个字符串，不能匹配其中部分
# content = 'hello 123 4567 world_this day'
# print(len(content))
#
# result = re.match('hello\s\d{3}\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.span())

#()截取一部分内容
# content = 'Hello 123456789 world'
# result  =re.match('Hello\s(\d+)\sworld',content)
# print(result)
# print(result.group())
# print(result.group(1))

#万能匹配符
# result = re.match('Hello.*world',content)
# print(result)
# print(result.group())

#search()---搜索整个HTML文本，找到符合正则表达式的第一个内容返回
#findAll()--- ----返回所有符合正则表达式的内容返回

