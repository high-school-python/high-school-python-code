"""色々な値の相関関係のグラフ"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# フォントサイズの設定
plt.rcParams["font.size"] = 12

# 相関係数のリスト
correlations = [0.9, 0.7, 0.5, 0.3, 0.0, -0.3, -0.5, -0.7, -0.9]

# サブプロットの設定
fig, axes = plt.subplots(3, 3, figsize=(15, 15))
axes = axes.flatten()

# 各相関係数についてデータを生成し、散布図と回帰直線を描画
for i, corr in enumerate(correlations):
    # データ数
    n = 100

    # 相関係数からデータを生成する
    mean = [0, 0]
    cov = [[1, corr], [corr, 1]]
    x, y = np.random.multivariate_normal(mean, cov, n).T

    # 散布図の描画
    axes[i].scatter(x, y, alpha=0.7)

    # 回帰直線の描画
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x_line = np.linspace(min(x), max(x), 100)
    y_line = slope * x_line + intercept
    axes[i].plot(x_line, y_line, "r-", linewidth=2)

    # 相関係数の表示（計算された実際の値）
    title = f"相関係数 = {r_value:.2f}"
    axes[i].set_title(title)
    axes[i].set_xlabel("X変数")
    axes[i].set_ylabel("Y変数")

    # 軸の範囲を統一
    axes[i].set_xlim(-3, 3)
    axes[i].set_ylim(-3, 3)

    # グリッド表示
    axes[i].grid(True, linestyle="--", alpha=0.7)

plt.tight_layout()
plt.savefig("correlation_examples.png", dpi=300)
plt.show()
