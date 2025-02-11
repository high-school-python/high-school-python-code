"""yes, no で終了を制御"""

while True:
    answer = input("続けますか？(y/n):")

    if answer == "n":
        print("終了します")
        break

    print("続けます")

print("プログラムを終了しました")


"""数当てゲームの例"""
target = 7

for i in range(5):
    guess = int(input(f"1 から 10 の数を当ててください（残り {5 - i} 回）："))

    if guess == target:
        print("正解！おめでとう！")
        break

    print("違います")

else:  # for ループが正常に （break されずに） 終了した場合
    print("ゲームオーバー")


# while 文でも同様に else が使えます
count = 5
while count > 0:
    guess = int(input(f"1 から 10 の数を当ててください（残り {count} 回）："))
    count -= 1

    if guess == target:
        print("正解！おめでとう！")
        break

    print("違います")

else:  # while ループが正常に （break されずに） 終了した場合
    print("ゲームオーバー")


"""3 の倍数をスキップする"""
for i in range(1, 6):
    if i % 3 == 0:
        print(f"{i} はスキップします")
        continue

    print(f"数字: {i}")

# 実行結果
# 数字: 1
# 数字: 2
# 3 はスキップします
# 数字: 4
# 数字: 5


"""正しい点数が入力されるまで繰り返す"""
while True:
    score = int(input("テストの点数を入力してください (0 〜 100):"))

    # 範囲外の値はスキップ
    if score < 0 or score > 100:
        print("0 から 100 の間で入力してください")
        # continue で次回のループに移動
        continue

    # 正しい値が入力された
    print(f"入力された点数：{score}")
    break
