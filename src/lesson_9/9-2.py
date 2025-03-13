"""テストの点数データ"""

import matplotlib.pyplot as plt
import numpy as np

# 100 個のランダムなテスト点数データを生成 （正規分布に従う）
np.random.seed(42)
# 平均 85, 標準偏差 7 の正規分布から生成し, 60 〜 100 の範囲に制限
scores = np.random.normal(85, 7, 100).clip(60, 100).round().astype(int)

mean_score = np.mean(scores)  # 平均値
median_score = np.median(scores)  # 中央値
# 最頻値を計算
values, counts = np.unique(scores, return_counts=True)
mode_score = values[np.argmax(counts)]

print(f"平均点：{mean_score:.1f}")
print(f"中央値：{median_score}")
print(f"最頻値：{mode_score}")

# ヒストグラムの作成
plt.figure(figsize=(12, 7))
plt.hist(scores, bins=range(60, 101, 5), edgecolor="black", alpha=0.7)

# 3 つの代表値を垂直線で表示
plt.axvline(mean_score, color="red", linestyle="--", linewidth=2, label=f"平均値: {mean_score:.1f}")
plt.axvline(median_score, color="green", linestyle="-.", linewidth=2, label=f"中央値: {median_score}")
plt.axvline(mode_score, color="blue", linestyle=":", linewidth=2, label=f"最頻値: {mode_score}")

plt.title("100 人のテスト点数の分布と 3 つの代表値")
plt.xlabel("点数")
plt.ylabel("人数")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
