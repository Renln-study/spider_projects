"""用于基本的验证的处理  ----
    1.转灰度
    2.二值化
"""
import tesserocr
from PIL import Image
import matplotlib.pyplot as plt

path = "./images/"
# filename = input("输入文件名"+"\n")
filename = 'code2.png'

image = Image.open(path+filename)
"""对图像进行灰度处理"""
image = image.convert('L')
threshold = 160
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table,'1')
""""对图像进行二值化处理"""
# image = image.convert('1')
plt.imshow(image)
plt.show()
result = tesserocr.image_to_text(image)
print(result)





