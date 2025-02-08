"""単純な繰り返し"""

for i in range(5):
    print("こんにちは")

# 実行結果
# こんにちは
# こんにちは
# こんにちは
# こんにちは
# こんにちは


"""繰り返しの番号を使う"""
for i in range(3):
    print(f"{i + 1}回目：こんにちは")

# 実行結果
# 1回目：こんにちは
# 2回目：こんにちは
# 3回目：こんにちは


"""文字列の一文字ずつ処理"""
# 文字列の各文字を表示
word = "Python"
for char in word:
    print(char)

# 実行結果
# P
# y
# t
# h
# o
# n


"""数値の範囲を指定する"""
# 1 から 5 までを表示
for i in range(1, 6):
    print(f"数字：{i}")

# 2 ずつ増やす
for i in range(0, 10, 2):
    print(f"偶数：{i}")


"""合計値を計算する"""
# 1 から 10 までの合計値を計算
total = 0
for i in range(1, 11):
    total = total + i
print(f"合計：{total}")  # 55

# テストの平均点を計算
scores = [85, 92, 78, 90, 88]
sum = 0
for score in scores:
    sum = sum + score
average = sum / len(scores)
print(f"平均点：{average}")
