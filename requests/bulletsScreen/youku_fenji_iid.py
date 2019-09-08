import requests

def getIid(url):
    headers = {
        'Referer':'https://v.youku.com/v_show/id_XNDI0NDQ0ODEwNA==.html?spm=a2h0k.11417342.soresults.dselectbutton&s=efbfbd78efbfbd5cefbf',
        'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Sec-Fetch-Mode':'no-cors',
        'Cookie':'P_F=1; P_T=1567936888; __ysuid=1566796699843X5I; UM_distinctid=16d0ea10cc95b2-06dff47489946a-5373e62-144000-16d0ea10cca9e9; __aysid=1567908500068yET; cna=70zqFe4+FTwCAYz6wDhhwVxS; juid=01dk7a3ci6668; _m_h5_tk=8f08f80173d7adf63771e886b9047ff3_1567931590950; _m_h5_tk_enc=d357ac8ea03433554479eec722ef2092; CNZZDATA1277955961=234862810-1567904580-https%253A%252F%252Fso.youku.com%252F%7C1567924541; __ayft=1567929609935; __ayscnt=1; __arpvid=1567929619237XUxrmn-1567929619259; __aypstp=3; __ayspstp=34; seid=01dk7u6ml6qs9; referhost=https%3A%2F%2Fso.youku.com; seidtimeout=1567931421160; ypvid=1567929626163MJxb0X; yseid=1567929626164y5R2Qy; ysestep=1; yseidcount=2; yseidtimeout=1567936826166; ycid=0; ystep=22; isg=BHt7BwqjovbPGJ5CP_ET3Au_Cl_l0I_SqoAWCm05l3qRzJyu9qE3IuhG5iwnbOfK; __ayvstp=7; __aysvstp=297'
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.text
    return None


def main():
    url= 'https://service.danmu.youku.com/list?jsoncallback=jQuery111208156194270012287_1567929619357&mat=1&mcount=1&ct=1001&iid=1061112026&aid=322943&cid=97&lid=0&ouid=0&_=1567929619375'
    html = getIid(url)
    print(html)


if __name__ == '__main__':
    main()




