"""タイトルと軸ラベルの詳細設定"""

import matplotlib.pyplot as plt

# データ
months = ["1月", "2月", "3月", "4月", "5月"]
sales = [120, 150, 180, 160, 210]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker="o")

# タイトルの詳細設定
plt.title(
    "2024年上半期 月間販売数の推移",
    fontsize=16,  # フォントサイズ
    fontweight="bold",  # 太字
    color="navy",  # 色
    pad=15,  # タイトルと図の間隔
)

# 軸ラベルの詳細設定
plt.xlabel("月", fontsize=12, labelpad=10, color="darkblue")
plt.ylabel("販売数（個）", fontsize=12, labelpad=10, color="darkblue")

plt.show()


"""グリッド線と目盛りの調整"""
import matplotlib.pyplot as plt

months = ["1月", "2月", "3月", "4月", "5月"]
sales = [120, 150, 180, 160, 210]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker="o")

# グリッド線の詳細設定
plt.grid(
    True,  # グリッド線を表示
    axis="both",  # x 軸と y 軸の両方にグリッド線
    linestyle="--",  # 破線スタイル
    color="gray",  # 色
    alpha=0.5,  # 透明度
)

# 目盛りの設定
plt.xticks(fontsize=10)  # x 軸目盛りのフォントサイズ
plt.yticks(range(100, 221, 20), fontsize=10)  # y 軸目盛りの範囲と間隔を指定

plt.show()


"""複数のグラフを並べて表示"""
import matplotlib.pyplot as plt

months = ["1月", "2月", "3月", "4月", "5月"]
sales_2023 = [110, 130, 160, 140, 190]
sales_2024 = [120, 150, 180, 160, 210]

# 2 × 1 のサブプロット （2 行 1 列） を作成
plt.figure(figsize=(12, 8))

# 1 つ目のサブプロット （2023 年データ）
plt.subplot(2, 1, 1)  # 2 行 1 列の 1 番目
plt.plot(months, sales_2023, marker="o", color="green")
plt.title("2023年 月間販売数", fontsize=14)
plt.ylabel("販売数（個）")
plt.grid(True, linestyle="--")

# 2 つ目のサブプロット （2024 年データ）
plt.subplot(2, 1, 2)  # 2 行 1 列の 2 番目
plt.plot(months, sales_2024, marker="o", color="blue")
plt.title("2024年 月間販売数", fontsize=14)
plt.ylabel("販売数（個）")
plt.grid(True, linestyle="--")

# サブプロット間の余白を調整
plt.tight_layout(pad=3.0)

plt.show()
