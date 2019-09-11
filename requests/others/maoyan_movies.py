import  requests
import re
import  json
import time

def get_one_page(url):
	headers = {
		'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
	}
	response = requests.get(url,headers=headers)
	if response.status_code == 200:
		return  response.text
	return  None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
	    yield {
		    'index': item[0],
		    'image': item[1],
		    'title': item[2].strip(),
		    'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
		    'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
		    'score': item[5].strip() + item[6].strip()
	        }

# def write_to_json(content):
# 	# 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
# 	# 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
# 	with open('resule.txt','a') as f:
# 		print(type(json.dumps(content)))
# 		# JSON库的dumps()
# 		# 方法实现字典的序列化，并指定ensure_ascii参数为False，这样可以保证输出结果是中文形式而不是Unicode编码
# 		f.write(json.dumps(content,ensure_ascii=False,).encode('utf-8'))

def write_to_json(content):
    with open('result1.txt', 'a',encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')


def main(offset):
	url = 'http://maoyan.com/board/4?offset='+str(offset)
	html =  get_one_page(url)
	parse_one_page(html)
	for item in parse_one_page(html):
		print(item)
		write_to_json(item)


if __name__ == '__main__':
	for i in range(10):
		main(offset=i * 10)
		#事件单位是秒数，睡眠的是当前的线程，
		time.sleep(1)



