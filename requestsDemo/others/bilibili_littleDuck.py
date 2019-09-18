import requests
import  time
#first  request--url get——response

def get_one_page(url):
    headers = {
        'User - Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) '+
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.text
    return None




def main():
    url = 'https://www.bilibili.com/video/av34406087?from=search&seid=2848483686653906200'
    time.sleep(2)
    html = get_one_page(url)
    print(html)


if __name__ == '__main__':
    main()