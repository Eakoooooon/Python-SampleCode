"""
Opencvのサンプルプログラム
https://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/index.html

写真のエッジ検出
pip install opencv-python
pip install matplotlib

"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sample.jpg', 0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
