# !pip install japanize-matplotlib

"""サイコロのシミュレーション"""

import random

import matplotlib.pyplot as plt

results = []

for _ in range(100):
    dice = random.randint(1, 6)  # 1 から 6 までの整数をランダムに生成
    results.append(dice)

# 結果の集計 (count 関数を使って各目の出現回数を数える)
counts = [results.count(i) for i in range(1, 7)]

for number in range(1, 7):
    count = results.count(number)
    percentage = count / len(results) * 100
    print(f"{number}の目: {count}回 ({percentage:.1f}%)")

# 結果をグラフで表示
plt.figure(figsize=(8, 6))
plt.bar(range(1, 7), counts)
plt.title("サイコロを 100 回振った結果")
plt.xlabel("出た目")
plt.ylabel("回数")
plt.xticks(range(1, 7))
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
