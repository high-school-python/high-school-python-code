"""教科別テスト結果"""

import matplotlib.pyplot as plt

# データの準備
subjects = ["国語", "数学", "英語", "理科", "社会"]
scores = [75, 82, 88, 85, 78]

# 棒グラフの作成
plt.figure(figsize=(10, 6))
plt.bar(subjects, scores, color="skyblue")

# グラフの装飾
plt.title("教科別テスト結果")
plt.xlabel("教科")
plt.ylabel("点数")
# Y 軸の範囲を 0 〜 100 に設定
plt.ylim(0, 100)

# 各棒の上に数値を表示
for i, score in enumerate(scores):
    plt.text(i, score + 1, str(score), ha="center")

plt.show()


"""散布図の基本"""
import matplotlib.pyplot as plt

# データの準備
math_scores = [65, 75, 60, 85, 70, 80, 75, 90, 95, 55]  # 数学の点数
japanese_scores = [70, 65, 80, 75, 65, 90, 85, 80, 75, 60]  # 国語の点数

# 散布図の作成
plt.figure(figsize=(10, 6))
plt.scatter(math_scores, japanese_scores, color="blue", alpha=0.7, s=100)

# グラフの装飾
plt.title("数学と国語のテスト結果の関係")
plt.xlabel("数学の点数")
plt.ylabel("国語の点数")
plt.grid(True, linestyle="--", alpha=0.7)

# 軸の範囲を設定 （0 〜 100 点）
plt.xlim(0, 100)
plt.ylim(0, 100)

# グラフの余白を調整
plt.tight_layout()

plt.show()
