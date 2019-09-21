import tesserocr
from PIL import Image
import matplotlib.pyplot as plt

def showImage():
    path = './images/code2.png'
    image = Image.open(path)
    print("当前验证码是展示："+image)
    plt.imshow(image)
    plt.show()
def printImage(image):
    print("当前验证码是输出："+image)
    result = tesserocr.image_to_text(image)
    return result
# def main():
    '''输出验证码内容'''
    # showImage(image)
    # """展示验证码图片"""
    # print(image)
def printtt():
    print("你真好")
