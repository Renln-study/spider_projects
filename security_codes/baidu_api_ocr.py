from aip import  AipOcr
import  codecs
import os
#读取图片函数
def ocr(path):
    with open(path,'rb') as f:
        return  f.read()
def main():
    filename = "./images/code2.png"
    print("已经收到，正在处理，请稍后....")
    app_id = '17288675'
    api_key = 'Ql2TusfzwGgGgpdGsMuRqybm'
    secret_key = 'AriFnhRq6XOylCH7j6cmmA2W2xM2DZs4'
    client = AipOcr(app_id,api_key,secret_key)
#读取图片
    image = ocr(filename)
#进程OCR识别
    dict1 = client.general(image)
#    print(dict1)
    with codecs.open(filename + ".txt","w","utf-8") as f:
        for i in dict1["words_result"]:
            f.write(str(i["words"] + "\r\n"))
    print ("处理完成")



if __name__ == '__main__':
    main()