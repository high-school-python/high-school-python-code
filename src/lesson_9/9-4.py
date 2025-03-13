"""テストの点数データ"""

import matplotlib.pyplot as plt
import numpy as np

# 2 つのクラスの点数データ
class_a = [82, 85, 88, 84, 87, 83, 86, 85, 84, 86]  # ばらつきが小さい
class_b = [65, 95, 75, 90, 85, 70, 95, 65, 80, 85]  # ばらつきが大きい


# 分析関数の定義
def analyze_scores(scores, class_name):
    mean = np.mean(scores)  # 平均
    var = np.var(scores)  # 分散
    std = np.std(scores)  # 標準偏差

    print(f"\n{class_name}の分析:")
    print(f"平均点：{mean:.1f}")
    print(f"分散：{var:.1f}")
    print(f"標準偏差：{std:.1f}")

    return mean, std


# 2 つのクラスを分析
mean_a, std_a = analyze_scores(class_a, "クラスA")
mean_b, std_b = analyze_scores(class_b, "クラスB")

# ヒストグラムで比較
plt.figure(figsize=(12, 5))

# クラス A のヒストグラム
plt.subplot(1, 2, 1)
plt.hist(class_a, bins=5, edgecolor="black", alpha=0.7)
plt.title("クラスAの点数分布（ばらつき小）")
plt.xlabel("点数")
plt.ylabel("人数")
plt.xlim(60, 100)
plt.axvline(mean_a, color="red", linestyle="--", label=f"平均: {mean_a:.1f}")
plt.axvline(mean_a + std_a, color="green", linestyle=":", label=f"標準偏差: {std_a:.1f}")
plt.axvline(mean_a - std_a, color="green", linestyle=":")
plt.legend()

# クラス B のヒストグラム
plt.subplot(1, 2, 2)
plt.hist(class_b, bins=5, edgecolor="black", alpha=0.7)
plt.title("クラスBの点数分布（ばらつき大）")
plt.xlabel("点数")
plt.xlim(60, 100)
plt.axvline(mean_b, color="red", linestyle="--", label=f"平均: {mean_b:.1f}")
plt.axvline(mean_b + std_b, color="green", linestyle=":", label=f"標準偏差: {std_b:.1f}")
plt.axvline(mean_b - std_b, color="green", linestyle=":")
plt.legend()

plt.tight_layout()
plt.show()
