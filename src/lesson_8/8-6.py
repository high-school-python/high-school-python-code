"""同じデータの異なる表現同じデータの異なる表現"""

import matplotlib.pyplot as plt

# 月間の天気データ
weather_data = {"晴れ": 18, "曇り": 8, "雨": 4}

# 1. 数値データとして表示
print("月間の天気データ:")
for weather, days in weather_data.items():
    print(f"{weather}: {days}日")

# 2. 円グラフとして表示
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)  # 1 行 2 列の 1 番目
plt.pie(
    weather_data.values(),
    labels=weather_data.keys(),
    autopct="%1.1f%%",  # パーセント表示
    colors=["lightskyblue", "lightgray", "lightgreen"],
)
plt.title("今月の天気の割合（円グラフ）")

# 3. 棒グラフとして表示
plt.subplot(1, 2, 2)  # 1 行 2 列の 2 番目
plt.bar(weather_data.keys(), weather_data.values(), color=["lightskyblue", "lightgray", "lightgreen"])
plt.title("今月の天気の日数（棒グラフ）")
plt.ylabel("日数")

plt.tight_layout()
plt.show()


"""同じデータでも印象が変わる例"""
import matplotlib.pyplot as plt

months = ["1月", "2月", "3月", "4月", "5月"]
sales = [100, 105, 103, 106, 110]

# 2 つのグラフを並べて表示
plt.figure(figsize=(12, 5))

# 1 つ目: Y 軸が 0 から始まるグラフ
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o", linewidth=2, color="blue")
plt.title("売上推移（Y 軸: 0 〜 120）")
plt.ylabel("売上（万円）")
plt.ylim(0, 120)  # Y 軸の範囲を 0 〜 120 に設定
plt.grid(True)

# 2 つ目: Y 軸が狭い範囲のグラフ
plt.subplot(1, 2, 2)
plt.plot(months, sales, marker="o", linewidth=2, color="blue")
plt.title("売上推移（Y 軸: 95 〜 115）")
plt.ylabel("売上（万円）")
plt.ylim(95, 115)  # Y 軸の範囲を 95 〜 115 に設定
plt.grid(True)

plt.tight_layout()
plt.show()
