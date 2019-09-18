# import tesserocr
# import  os
from PIL import Image
import matplotlib.pyplot as plt

"""获取当前路径和上一级路径"""
# print(os.getcwd())
image = Image.open('./images/demo.jpg')
image = image.convert('L')
# image.show()
# result = tesserocr.image_to_text(image)
# print(result)
plt.imshow(image)
plt.show()


# print(tesserocr.file_to_text('./images/image.png'))

# print(tesserocr.image_to_text('./images/code3.jpg'))

