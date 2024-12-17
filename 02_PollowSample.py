"""
Pillowのサンプル
pip install pillow
画像に文字を入れる
"""
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np


# 画像に文字を入れる関数
def img_add_msg(img, message):
    # PILでフォントを定義
    font = ImageFont.truetype(r'C:\Windows\Fonts\meiryo.ttc', 50)
    # cv2(NumPy)型の画像をPIL型に変換
    img = Image.fromarray(img)
    # 描画用のDraw関数を用意
    draw = ImageDraw.Draw(img)

    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text((50, 50), message, font=font, fill=(233, 233, 233, 0))
    # PIL型の画像をcv2(NumPy)型に変換
    img = np.array(img)
    # 文字入りのデータを返す
    return img


if __name__ == '__main__':
    # カラー画像読み込み
    img = cv2.imread('sample.jpg', 1)
    # 好きな文字を入れる
    message = 'ここデートにもってこい！'
    # 画像に文字を入れる
    img = img_add_msg(img, message)

    # 画像を表示させる（何かキーを入力すると終了）
    cv2.imshow('title', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
