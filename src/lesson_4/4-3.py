"""カウントダウンタイマー"""

count = 5

while count > 0:
    print(count)
    count = count - 1

print("時間切れ！")

# 実行結果
# 5
# 4
# 3
# 2
# 1
# 時間切れ！


"""パスワード入力"""
# 正しいパスワードが入力されるまで繰り返す
password = ""
attempts = 0  # 試行回数

while password != "secret":
    attempts += 1
    password = input(f"パスワードを入力してください（{attempts}回目）：")

    if attempts >= 3:  # 3回まで
        print("回数の上限を超えました")
        break

if password == "secret":
    print("ログイン成功！")


"""数当てゲーム"""
import random

# 1 から 100 までのランダムな数を当てるゲーム
target = random.randint(1, 100)
guess = 0
tries = 0

print("1 から 100 までの数を当ててください")

while guess != target:
    tries += 1
    guess = int(input(f"{tries}回目の予想："))

    if guess > target:
        print("もっと小さい数です")
    elif guess < target:
        print("もっと大きい数です")

print(f"正解！{tries}回で当てました！")


"""合計値の計算"""
# 合計が 100 を超えるまで数を足していく
total = 0
count = 0

while total <= 100:
    count += 1
    total += count
    print(f"現在の合計: {total}")

print(f"{count}回で合計が{total}になりました")


"""無限ループの例"""
# 無限ループの例 (実行しないでください！)
count = 1
while count > 0:
    print(count)  # count が減らないので永遠に続く

# 正しい例
count = 1
while count > 0:
    print(count)
    # count を減らして必ず終わるようにする
    count -= 1
