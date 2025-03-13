# !pip install japanize-matplotlib

"""日々の気温データ"""

# matplotlib の pyplot モジュールをインポートします
# 慣習として、 plt という名前で名前付きインポートをすることが多いです
import matplotlib.pyplot as plt

# 日々の気温データ
days = list(range(1, 8))  # 1 週間分の日付 [1, 2, 3, 4, 5, 6, 7]
temperatures = [22, 24, 23, 25, 26, 24, 23]  # 各日の気温（℃）

# グラフの作成
plt.figure(figsize=(10, 6))  # グラフのサイズ指定（幅 10 インチ、高さ 6 インチ）
plt.plot(days, temperatures, marker="o")  # 折れ線グラフの描画、各点に丸印を付ける

# グラフの表示
plt.title("1週間の気温変化")  # グラフのタイトル
plt.xlabel("日付")  # x 軸のラベル
plt.ylabel("気温（℃）")  # y 軸のラベル
plt.grid(True)  # グリッド線の表示
plt.show()  # グラフを画面に表示
