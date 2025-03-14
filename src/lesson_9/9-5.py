"""様々な相関パターン"""

import matplotlib.pyplot as plt
import numpy as np

# 乱数の種を固定 （再現性のため）
np.random.seed(42)

# 4 つの異なるパターンのデータを生成
n = 50  # データ点の数

# 1. 強い正の相関
x1 = np.linspace(0, 10, n)
y1 = 2 * x1 + 5 + np.random.normal(0, 1, n)

# 2. 強い負の相関
x2 = np.linspace(0, 10, n)
y2 = 20 - 1.5 * x2 + np.random.normal(0, 1, n)

# 3. 相関なし
x3 = np.linspace(0, 10, n)
y3 = np.random.normal(10, 3, n)

# 4. 非線形の関係
x4 = np.linspace(0, 10, n)
y4 = 2 * (x4 - 5) ** 2 + np.random.normal(0, 3, n)

# 4 つのサブプロットを作成
plt.figure(figsize=(12, 10))

# 強い正の相関
plt.subplot(2, 2, 1)
plt.scatter(x1, y1, color="blue", alpha=0.7)
plt.title("強い正の相関")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

# 強い負の相関
plt.subplot(2, 2, 2)
plt.scatter(x2, y2, color="red", alpha=0.7)
plt.title("強い負の相関")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

# 相関なし
plt.subplot(2, 2, 3)
plt.scatter(x3, y3, color="green", alpha=0.7)
plt.title("相関なし")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

# 非線形の関係
plt.subplot(2, 2, 4)
plt.scatter(x4, y4, color="purple", alpha=0.7)
plt.title("非線形の関係")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
