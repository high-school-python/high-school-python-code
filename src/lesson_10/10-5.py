"""モンテカルロ法による円周率の計算"""

import random

import matplotlib.pyplot as plt
import numpy as np


def estimate_pi(num_points):
    """モンテカルロ法で円周率を推定する"""
    inside_circle = 0  # 円の内側に入った点の数

    # 点のデータを保存するためのリスト
    x_inside, y_inside = [], []  # 円の内側の点
    x_outside, y_outside = [], []  # 円の外側の点

    # num_points個のランダムな点を生成
    for _ in range(num_points):
        x = random.random()  # 0から1の乱数
        y = random.random()  # 0から1の乱数

        # 点が円の内側かどうか判定（x^2 + y^2 <= 1 なら内側）
        if x * x + y * y <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    # 円周率の推定値を計算
    pi_estimate = 4 * inside_circle / num_points

    return pi_estimate, x_inside, y_inside, x_outside, y_outside


# 一度に計算する点の数
num_points = 10000

# 円周率を推定
pi_estimate, x_in, y_in, x_out, y_out = estimate_pi(num_points)

# 結果を表示
print(f"点の数: {num_points}")
print(f"円の内側に入った点の数: {len(x_in)}")
print(f"推定された円周率: {pi_estimate}")
print(f"実際の円周率との誤差: {abs(pi_estimate - np.pi)}")

# 点をプロット
plt.figure(figsize=(8, 8))
plt.scatter(x_in, y_in, color="blue", s=1, alpha=0.6, label="円の内側")
plt.scatter(x_out, y_out, color="red", s=1, alpha=0.6, label="円の外側")

# 四分割した円を描画
theta = np.linspace(0, np.pi / 2, 100)
plt.plot(np.cos(theta), np.sin(theta), "g-", linewidth=2)

# グラフの設定
plt.axis("equal")
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title(f"モンテカルロ法による円周率の計算\n推定値: {pi_estimate:.6f}（点の数: {num_points}）", fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
