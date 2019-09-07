import  requests
import  re
r = requests.get("https://cuiqingcai.com/5517.html")
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

data = {
	'name':"22",
	'age':"renln"

}

# r = requests.get('http://httpbin.org/get',params=data)
#
# print(type(r.text))
# # print(r.text)
# print(r.json())
# print(type(r.json()))


# 文件的下载get
# r = requests.get("http://github.com/favicon.ico")
# print(r.text)
# print(r.content)
# # 这里用了open()方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可以向文件里写入二进制数据。
# with open('favicon.ico','wb') as f:
# 	f.write(r.content)

#文件的上传post
# 这里用了open()方法，它的第一个参数是文件名称，第二个参数代表以二进制写的形式打开，可读文件的信息
# files = {'file': open('favicon.ico','rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)


#Cooikes
#item()方法遍历字典
# r = requests.get("http://www.baidu.com")
# # print(r.cookies)
# # print(type(r.cookies))
# for key,value in r.cookies.items():
# 	print(key+'='+value)


#
# header = {
# 		 'Cookie':'_zap=4f84a021-3bab-4228-861f-a5d08af94528; _xsrf=LWIbkJ2LzT0X7ptfSlDUPebkPwI66r3P; d_c0="AFBiRnsi6A-PTua2ewQlQS7qL29U4A4yZos=|1566056333"; capsion_ticket="2|1:0|10:1566056352|14:capsion_ticket|44:ZmI0YzAwOGI3ZGU4NGE4YjhhNzZmYWVlZTAwNjJkM2Q=|21ff4adf9347ae671445f41fdfd89c014f1891717eb5d652d0e0e3b16b8e3b9c"; z_c0="2|1:0|10:1566056356|4:z_c0|92:Mi4xWDVaNkJRQUFBQUFBVUdKR2V5TG9EeVlBQUFCZ0FsVk5wRzFGWGdBamUxYksxbzBPdHMtamNiMjYtUnFRYS1LQlRn|111369d1b79a6e033b217f4303b7c1345fb46d5adec19a2eb821a37c91cf2dcc"; tst=r; q_c1=279fc06e8cb441cab8b319b92d627290|1566117036000|1566117036000; tgw_l7_route=4860b599c6644634a0abcd4d10d37251',
# 	     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
# 		 'Host': 'www.zhihu.com'
# }
# r = requests.get("https://www.zhihu.com",headers = header)
# print(r.text)


#证书验证
response = requests.get('https://www.12306.cn')
print(response.status_code)
print(response.content)

