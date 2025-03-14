"""部活動の練習時間データ"""

import matplotlib.pyplot as plt

# 部活動の練習時間データ
days = ["月", "火", "水", "木", "金"]
morning = [30, 45, 30, 45, 30]  # 朝練時間 （分）
evening = [90, 60, 90, 60, 90]  # 放課後練習時間 （分）

# 積み上げ棒グラフの作成
plt.figure(figsize=(10, 6))
plt.bar(days, morning, label="朝練", color="lightblue")
plt.bar(days, evening, bottom=morning, label="放課後", color="royalblue")

# グラフの装飾
plt.title("バスケ部の週間練習時間", fontsize=15)
plt.xlabel("曜日", fontsize=12)
plt.ylabel("練習時間（分）", fontsize=12)
plt.legend(loc="upper right")
plt.grid(True, axis="y", linestyle="--", alpha=0.7)

# 合計時間を表示
for i in range(len(days)):
    total = morning[i] + evening[i]
    plt.text(i, total + 5, f"計{total}分", ha="center")

plt.tight_layout()
plt.show()


"""練習時間の週間比較"""
import matplotlib.pyplot as plt
import numpy as np

# 練習時間データ （2 週間分）
days = ["月", "火", "水", "木", "金"]
# 通常週の練習時間 （分）
normal_week = [120, 105, 120, 105, 120]
# 大会前週の練習時間 （分）
tournament_week = [150, 135, 150, 140, 120]

# グラフの作成
plt.figure(figsize=(10, 6))

# X軸の位置を計算
x = np.arange(len(days))
width = 0.35  # 棒の幅

# 2 つの週のデータをプロット
plt.bar(x - width / 2, normal_week, width, label="通常週", color="lightblue")
plt.bar(x + width / 2, tournament_week, width, label="大会前週", color="salmon")

# グラフの装飾
plt.title("バスケ部の練習時間比較: 通常週 vs 大会前週", fontsize=15)
plt.xlabel("曜日", fontsize=12)
plt.ylabel("練習時間（分）", fontsize=12)
plt.xticks(x, days)
plt.legend()
plt.grid(True, axis="y", linestyle="--", alpha=0.7)

# 差分を表示
for i in range(len(days)):
    diff = tournament_week[i] - normal_week[i]

    if diff != 0:
        plt.text(
            i + width / 2,
            tournament_week[i] + 5,
            f"+{diff}" if diff > 0 else f"{diff}",
            ha="center",
            color="red" if diff > 0 else "blue",
        )

plt.tight_layout()
plt.show()


"""練習内容の内訳"""
import matplotlib.pyplot as plt

# 練習内容の内訳データ （1 週間の合計時間）
practice_contents = {
    "シュート練習": 120,
    "パス練習": 90,
    "ドリブル練習": 60,
    "体力トレーニング": 75,
    "ゲーム形式": 150,
    "ミーティング": 45,
}

# 色のリスト
colors = ["lightblue", "lightgreen", "lightsalmon", "lightgray", "gold", "plum"]

# 円グラフの作成
plt.figure(figsize=(10, 8))
plt.pie(
    practice_contents.values(),
    labels=practice_contents.keys(),
    autopct="%1.1f%%",  # パーセント表示
    startangle=90,  # 開始角度
    colors=colors,
)

plt.title("1週間の練習内容の内訳", fontsize=15)
plt.axis("equal")  # 円を歪ませない

# 凡例を追加 （時間も表示）
legend_labels = [f"{k} ({v}分)" for k, v in practice_contents.items()]
plt.legend(legend_labels, loc="center left", bbox_to_anchor=(1, 0.4))

plt.tight_layout()
plt.show()
