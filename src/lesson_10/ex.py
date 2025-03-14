"""コイン投げシミュレーション"""

import random
from collections import Counter

import matplotlib.pyplot as plt


def coin_flip_experiment(flips: int = 100) -> Counter:
    # コインを指定回数投げる
    results = []
    for _ in range(flips):
        result = "裏" if random.random() < 0.5 else "表"
        results.append(result)

    # 結果を集計
    count = Counter(results)

    # 結果を表示
    print(f"\n{flips}回コインを投げた結果:")
    for face, num in count.items():
        percentage = (num / flips) * 100
        print(f"{face}: {num}回 ({percentage:.1f}%)")

    # グラフの作成
    plt.figure(figsize=(8, 6))
    plt.bar(count.keys(), count.values())
    plt.title(f"コイン投げの結果 ({flips}回)")
    plt.ylabel("回数")
    plt.show()

    return count


result = coin_flip_experiment(100)


"""サイコロの確率収束シミュレーション"""


def dice_probability_simulation(trials: int = 1000) -> None:
    # 結果を記録する配列
    counts = {i: 0 for i in range(1, 7)}
    probabilities = {i: [] for i in range(1, 7)}

    # サイコロを振るシミュレーション
    for i in range(1, trials + 1):
        roll = random.randint(1, 6)
        counts[roll] += 1

        # 各目の確率を計算して記録
        for num in range(1, 7):
            prob = counts[num] / i
            probabilities[num].append(prob)

    # グラフの描画
    plt.figure(figsize=(12, 6))

    # 各目の確率の推移をプロット
    for num in range(1, 7):
        plt.plot(probabilities[num], label=f"{num}の目", alpha=0.7)

    # 理論値 （1 / 6） の線を追加
    plt.axhline(y=1 / 6, color="r", linestyle="--", label="理論値 (1 / 6)")

    plt.xlabel("試行回数")
    plt.ylabel("確率")
    plt.title("サイコロの確率収束シミュレーション")
    plt.legend()
    plt.grid(True)
    plt.show()

    # 最終的な確率を表示
    print("\n最終的な確率:")
    for num in range(1, 7):
        final_prob = probabilities[num][-1]
        print(f"{num}の目: {final_prob:.3f}")


dice_probability_simulation(1000)
