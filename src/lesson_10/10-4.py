"""コイン投げの大数の法則"""

import random

import matplotlib.pyplot as plt


def coin_flip_simulation(trials):
    """コイン投げをシミュレーションし、各試行後の表の割合を記録"""
    heads = 0  # 表の回数
    heads_ratio = []  # 表の割合の履歴

    for i in range(1, trials + 1):
        # コインを投げる（0.5の確率で表）
        if random.random() < 0.5:
            heads += 1

        # i回目の試行後の表の割合を記録
        heads_ratio.append(heads / i)

    return heads_ratio


# 異なる試行回数でシミュレーション
trials_100 = coin_flip_simulation(100)
trials_1000 = coin_flip_simulation(1000)
trials_10000 = coin_flip_simulation(10000)

# グラフの描画
plt.figure(figsize=(12, 6))

# 各シミュレーション結果をプロット
plt.plot(range(1, 101), trials_100, label="100 回試行", alpha=0.7)
plt.plot(range(1, 1001), trials_1000, label="1,000 回試行", alpha=0.7)
plt.plot(range(1, 10001), trials_10000, label="10,000 回試行", alpha=0.7)

# 理論値（0.5）の水平線
plt.axhline(y=0.5, color="r", linestyle="--", label="理論値(0.5)")

# グラフの装飾
plt.xscale("log")  # x軸を対数スケールに
plt.xlabel("試行回数", fontsize=12)
plt.ylabel("表の出る割合", fontsize=12)
plt.title("コイン投げシミュレーション：大数の法則", fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

# 範囲を制限して見やすく
plt.ylim(0.3, 0.7)

plt.show()

# 最終的な表の割合
print(f"100 回試行後の表の割合: {trials_100[-1]:.4f}")
print(f"1,000 回試行後の表の割合: {trials_1000[-1]:.4f}")
print(f"10,000 回試行後の表の割合: {trials_10000[-1]:.4f}")
