"""一様分布のシミュレーション"""

import random

import matplotlib.pyplot as plt
import numpy as np

# 一様分布からの乱数生成
uniform_values = [random.uniform(0, 1) for _ in range(1000)]

# ヒストグラムの描画
plt.figure(figsize=(10, 6))

# ヒストグラムを描画（正規化して確率密度関数として表示）
counts, bins, patches = plt.hist(
    uniform_values, bins=20, color="skyblue", edgecolor="black", alpha=0.7, density=True, label="シミュレーション結果"
)

# 理論値の計算と描画
x = np.linspace(0, 1, 100)
y = np.ones_like(x)  # 一様分布の確率密度関数は区間内で常に 1
plt.plot(x, y, "r-", linewidth=2, label="理論値")

plt.title("一様分布 (0から1の範囲)", fontsize=14)
plt.xlabel("値", fontsize=12)
plt.ylabel("確率密度", fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# 平均と標準偏差
mean = np.mean(uniform_values)
std_dev = np.std(uniform_values)
print(f"平均: {mean:.4f}")
print(f"標準偏差: {std_dev:.4f}")
print("理論上の平均: 0.5")
print(f"理論上の標準偏差: {1 / np.sqrt(12):.4f}")


"""二項分布のシミュレーション"""
import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom


# コイン投げのシミュレーション （10 回投げて表が出る回数）
def coin_flip_experiment():
    flips = [random.random() < 0.5 for _ in range(10)]  # Trueが表、Falseが裏
    return sum(flips)  # 表の回数を返す


# 1000 回の実験を行う
results = [coin_flip_experiment() for _ in range(1000)]

# ヒストグラムの描画
plt.figure(figsize=(10, 6))
values, counts, _ = plt.hist(results, bins=np.arange(-0.5, 11, 1), color="lightblue", edgecolor="black")

# 理論値の計算と描画
n, p = 10, 0.5  # 試行回数と成功確率
x = np.arange(0, 11)
pmf = binom.pmf(x, n, p)  # 確率質量関数
plt.plot(x, 1000 * pmf, "ro-", ms=8, label="理論値")

plt.title("二項分布: 10回のコイン投げで表が出る回数", fontsize=14)
plt.xlabel("表の回数", fontsize=12)
plt.ylabel("頻度", fontsize=12)
plt.xticks(range(11))
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 平均と標準偏差
mean = np.mean(results)
std_dev = np.std(results)
print(f"平均: {mean:.4f}")
print(f"標準偏差: {std_dev:.4f}")
print(f"理論上の平均: {n * p}")
print(f"理論上の標準偏差: {np.sqrt(n * p * (1 - p)):.4f}")


"""正規分布のシミュレーション"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# 正規分布からの乱数生成 （平均 170 cm, 標準偏差 5 cm の身長データ）
heights = np.random.normal(170, 5, 1000)

# ヒストグラムの描画
plt.figure(figsize=(10, 6))
plt.hist(heights, bins=30, color="lightblue", edgecolor="black", density=True)

# 理論的な正規分布曲線の描画
x = np.linspace(150, 190, 1000)
plt.plot(x, norm.pdf(x, 170, 5), "r-", linewidth=2, label="理論曲線")

plt.title("正規分布: 平均 170cm, 標準偏差 5cm の身長データ", fontsize=14)
plt.xlabel("身長 (cm)", fontsize=12)
plt.ylabel("確率密度", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 平均と標準偏差
mean = np.mean(heights)
std_dev = np.std(heights)
print(f"平均: {mean:.4f}cm")
print(f"標準偏差: {std_dev:.4f}cm")


"""偏差値と正規分布の関係"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# グラフの設定
plt.figure(figsize=(12, 8))

# 正規分布のパラメータ
mu = 50  # 平均
sigma = 10  # 標準偏差

# x軸の範囲
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)

# 正規分布の確率密度関数
pdf = norm.pdf(x, mu, sigma)

# 正規分布曲線をプロット
plt.plot(x, pdf, "k-", linewidth=2, label="正規分布")

# 平均 ±1 標準偏差 （約 68%） の範囲を塗りつぶす
x_fill_1sigma = np.linspace(mu - sigma, mu + sigma, 100)
plt.fill_between(
    x_fill_1sigma, norm.pdf(x_fill_1sigma, mu, sigma), color="lightblue", alpha=0.7, label="平均±1σ (68.3%)"
)

# 平均 ±2 標準偏差 （約 95%） の範囲を塗りつぶす
x_fill_2sigma = np.linspace(mu - 2 * sigma, mu + 2 * sigma, 100)
x_fill_1sigma_mask = (x_fill_2sigma >= mu - sigma) & (x_fill_2sigma <= mu + sigma)
x_fill_2sigma_only = np.copy(x_fill_2sigma)
y_values = norm.pdf(x_fill_2sigma_only, mu, sigma)
y_values[x_fill_1sigma_mask] = 0
plt.fill_between(x_fill_2sigma_only, y_values, color="lightgreen", alpha=0.7, label="平均±2σ (95.4%)")

# 平均 ±3 標準偏差 （約 99.7%） の範囲を塗りつぶす
x_fill_3sigma = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
x_fill_2sigma_mask = (x_fill_3sigma >= mu - 2 * sigma) & (x_fill_3sigma <= mu + 2 * sigma)
x_fill_3sigma_only = np.copy(x_fill_3sigma)
y_values = norm.pdf(x_fill_3sigma_only, mu, sigma)
y_values[x_fill_2sigma_mask] = 0
plt.fill_between(x_fill_3sigma_only, y_values, color="lightyellow", alpha=0.7, label="平均±3σ (99.7%)")

# 偏差値の目盛りを追加
plt.axvline(x=mu, color="red", linestyle="-", alpha=0.7, label="平均値 (偏差値50)")
plt.axvline(x=mu + sigma, color="blue", linestyle="--", alpha=0.7, label="偏差値60")
plt.axvline(x=mu - sigma, color="blue", linestyle="--", alpha=0.7)
plt.axvline(x=mu + 2 * sigma, color="green", linestyle="--", alpha=0.7, label="偏差値70")
plt.axvline(x=mu - 2 * sigma, color="green", linestyle="--", alpha=0.7)
plt.axvline(x=mu + 3 * sigma, color="orange", linestyle="--", alpha=0.7, label="偏差値80")
plt.axvline(x=mu - 3 * sigma, color="orange", linestyle="--", alpha=0.7)

# 軸ラベルとタイトル
plt.title("偏差値と正規分布の関係", fontsize=16)
plt.xlabel("得点（偏差値）", fontsize=14)
plt.ylabel("確率密度", fontsize=14)
plt.xticks(
    [mu - 3 * sigma, mu - 2 * sigma, mu - sigma, mu, mu + sigma, mu + 2 * sigma, mu + 3 * sigma],
    ["20", "30", "40", "50", "60", "70", "80"],
)
plt.grid(True, alpha=0.3)
plt.legend(loc="upper left", fontsize=12)

# テキスト注釈を追加
plt.annotate(
    "偏差値50: 平均値",
    xy=(mu, 0.005),
    xytext=(mu + 5, 0.01),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1.5),
)
plt.annotate(
    "偏差値60: 上位16%",
    xy=(mu + sigma, 0.024),
    xytext=(mu + sigma + 5, 0.03),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1.5),
)
plt.annotate(
    "偏差値70: 上位2.3%",
    xy=(mu + 2 * sigma, 0.005),
    xytext=(mu + 2 * sigma + 5, 0.01),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1.5),
)
plt.annotate(
    "偏差値40: 下位16%",
    xy=(mu - sigma, 0.024),
    xytext=(mu - sigma - 15, 0.03),
    arrowprops=dict(facecolor="black", shrink=0.05, width=1.5),
)

plt.tight_layout()
plt.show()
