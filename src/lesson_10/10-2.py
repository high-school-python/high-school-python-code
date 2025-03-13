"""random モジュールの基本"""

import random

# 基本的な乱数生成関数
random_float = random.random()  # 0.0 以上 1.0 未満の浮動小数点数
print(f"0 から 1 の乱数: {random_float}")

# 指定範囲の整数乱数
dice = random.randint(1, 6)  # 1 から 6 までの整数
print(f"サイコロの目: {dice}")

# 指定範囲の浮動小数点乱数
temperature = random.uniform(20.0, 30.0)  # 20.0 から 30.0 までの浮動小数点数
print(f"気温: {temperature:.1f}°C")

# 既存のリストからランダムに選択
fruits = ["りんご", "バナナ", "オレンジ", "ぶどう", "メロン"]
chosen_fruit = random.choice(fruits)
print(f"選ばれた果物: {chosen_fruit}")

# リストをシャッフル
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)
print(f"シャッフルされたカード: {cards}")

# 重複なしでランダムに複数選択
lottery_numbers = random.sample(range(1, 46), 6)  # 1 から 45 までの数から重複なしで 6 つ選択
print(f"宝くじの番号: {sorted(lottery_numbers)}")


"""乱数のシード設定"""
import random

# シードを固定
random.seed(42)

# 乱数を生成
for _ in range(5):
    print(random.random())

print("\n同じシードで再度生成:")
# 同じシードを設定すると同じ乱数列が生成される
random.seed(42)

for _ in range(5):
    print(random.random())
