# !pip install japanize-matplotlib

"""クラスの身長データ例"""

import matplotlib.pyplot as plt
import numpy as np

# クラスの身長データ例 （cm）
heights = [165, 172, 168, 170, 175, 163, 169, 167, 173, 166]

# 基本的な統計量の計算
mean_height = np.mean(heights)  # 平均
max_height = np.max(heights)  # 最大値
min_height = np.min(heights)  # 最小値
range_height = max_height - min_height  # 範囲（最大と最小の差）

print(f"平均身長：{mean_height:.1f}cm")
print(f"最大身長：{max_height}cm")
print(f"最小身長：{min_height}cm")
print(f"身長の範囲：{range_height}cm")

# ヒストグラムで分布を可視化
plt.figure(figsize=(10, 6))
plt.hist(heights, bins=5, edgecolor="black")
plt.title("クラスの身長分布")
plt.xlabel("身長 (cm)")
plt.ylabel("人数")
plt.grid(True, alpha=0.3)
plt.show()


"""テストの点数データ分析"""
import matplotlib.pyplot as plt
import numpy as np

# 数学テストの点数 (0 から 100 までの整数を、ランダムに 100 個生成)
math_scores = np.random.randint(0, 100, 100)

# 基本統計量の計算
mean_score = np.mean(math_scores)  # 平均点
median_score = np.median(math_scores)  # 中央値
std_score = np.std(math_scores)  # 標準偏差
min_score = np.min(math_scores)  # 最低点
max_score = np.max(math_scores)  # 最高点

print(f"平均点：{mean_score:.1f}")
print(f"中央値：{median_score}")
print(f"標準偏差：{std_score:.1f}")
print(f"最低点：{min_score}")
print(f"最高点：{max_score}")

# ヒストグラムの作成
plt.figure(figsize=(10, 6))
plt.hist(math_scores, bins=10, color="skyblue", edgecolor="black")
# 平均点を示す垂直線を追加
plt.axvline(mean_score, color="red", linestyle="dashed", linewidth=1, label=f"平均点：{mean_score:.1f}")
plt.title("数学テストの点数分布")
plt.xlabel("点数")
plt.ylabel("人数")
# 凡例を表示
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
