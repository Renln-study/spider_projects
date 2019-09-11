import  data_cleaning

data  = data_cleaning
def main():
    print("无参函数构造")
    source_file = 'J:\JD_comments_jpg\douban_comments.txt'
    method = 'r'
    codeStyle = 'utf-8'
    Img_place = 'J:\JD_comments_jpg\TestDataCleaning.jpg'
    # data.cut_word('',source_file)
    data.createCloud(None,Img_place,None,source_file,method,codeStyle)




if __name__ == '__main__':
    print("测试共用类")
    main()


