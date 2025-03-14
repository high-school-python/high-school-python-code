"""クラス全員の点数をグラフ化し、平均点を表示するプログラム"""

import matplotlib.pyplot as plt
import numpy as np


def visualize_class_scores():
    students = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    scores = [85, 92, 78, 88, 95, 73, 89, 84, 91, 87]
    # 平均点の計算
    average = np.mean(scores)
    # グラフの作成
    plt.figure(figsize=(12, 6))
    # 棒グラフの描画
    bars = plt.bar(students, scores, color="skyblue")
    # 平均点の線を追加
    plt.axhline(y=average, color="red", linestyle="--", label=f"平均点: {average:.1f}")

    # グラフの装飾
    plt.title("クラスのテスト結果", fontsize=14, pad=15)
    plt.xlabel("生徒", fontsize=12)
    plt.ylabel("点数", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.3)
    plt.legend()

    # 各棒グラフの上に点数を表示
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f"{int(height)}", ha="center", va="bottom")

    plt.show()


visualize_class_scores()


"""部活動の練習日数を棒グラフで表示し、タイトルやラベルを付けるプログラム"""


def visualize_club_activities():
    # 月ごとの練習日数データ
    months = ["4月", "5月", "6月", "7月", "8月", "9月"]
    regular_days = [15, 18, 20, 16, 22, 19]  # 通常練習
    special_days = [2, 3, 5, 8, 10, 4]  # 特別練習

    # グラフのサイズ設定
    plt.figure(figsize=(12, 7))

    # バーの位置を計算
    x = np.arange(len(months))
    width = 0.35

    # 棒グラフの作成
    plt.bar(x - width / 2, regular_days, width, label="通常練習", color="lightblue")
    plt.bar(x + width / 2, special_days, width, label="特別練習", color="lightgreen")

    # グラフの装飾
    plt.title("部活動月間練習日数", fontsize=14, pad=15)
    plt.xlabel("月", fontsize=12)
    plt.ylabel("練習日数", fontsize=12)
    plt.xticks(x, months)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.3)

    # 各棒グラフの上に日数を表示
    for i, v in enumerate(regular_days):
        plt.text(i - width / 2, v + 0.5, str(v), ha="center")
    for i, v in enumerate(special_days):
        plt.text(i + width / 2, v + 0.5, str(v), ha="center")

    # 合計日数を表示
    total_days = [r + s for r, s in zip(regular_days, special_days)]
    for i, total in enumerate(total_days):
        plt.text(i, max(regular_days[i], special_days[i]) + 2, f"計{total}日", ha="center")

    plt.show()


visualize_club_activities()
