"""
Matplotlibサンプルコード

https://matplotlib.org/stable/gallery/index.html

# 日本語対応
pip install japanize-matplotlib
"""
import japanize_matplotlib
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fig, ax = plt.subplots()

    # 項目
    fruits = ['りんご', 'ブルーベリー', 'さくらんぼ', 'orange']
    # 数値データ
    counts = [40, 100, 30, 55]
    #棒グラフのスタイル設定
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    # バーの実装
    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    # y軸のスタイルとタイトルの設定
    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')
    # グラフの表示
    plt.show()