"""1 から 100 までの合計を求めるプログラム"""

# 方法 1: for ループを使う
total = 0
for i in range(1, 101):
    total += i
print(f"1から100までの合計：{total}")

# 方法 2: while ループを使う
total = 0
num = 1
while num <= 100:
    total += num
    num += 1
print(f"1から100までの合計：{total}")

# チャレンジ：
# - 偶数だけの合計を求めてみよう
# - 3の倍数だけの合計を求めてみよう
# - 入力された数までの合計を求めてみよう


"""1 から 10 までの数字で掛け算表を表示するプログラム"""
# 見やすい九九表を作成
print("     ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n" + "-" * 50)

for i in range(1, 11):
    print(f"{i:2}  |", end="")
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()  # 改行

"""
出力例：
     1   2   3   4   5   6   7   8   9  10
--------------------------------------------------
1  |   1   2   3   4   5   6   7   8   9  10
2  |   2   4   6   8  10  12  14  16  18  20
...
"""

# チャレンジ：
# - 表の範囲を変更できるようにしてみよう
# - 縦と横に線を引いて見やすくしてみよう
# - 3 の段だけ色を変えてみよう （print 文のオプションで）
