'''
    내가 그린 손글씨 읽기
'''
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('num.png')
img = np.array(im.resize((28, 28), Image.ANTIALIAS).convert('L'))
# print(img)

# 정규화
data = img.reshape([1, 784])
data = data / 255
print(data)

plt.imshow(data.reshape(28, 28), cmap='Greys')
plt.show()