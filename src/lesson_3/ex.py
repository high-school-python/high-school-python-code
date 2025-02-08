"""点数を入力し、合否判定するプログラム"""

score = int(input("点数を入力してください (0 〜 100):"))

if score < 0 or score > 100:
    print("エラー: 0 から 100 の間の点数を入力してください")
else:
    # 判定処理
    if score >= 90:
        print("評価: A+")
        print("素晴らしい成績です！")
    elif score >= 80:
        print("評価: A")
        print("よくできました！")
    elif score >= 70:
        print("評価: B")
        print("がんばりました")
    elif score >= 60:
        print("評価: C")
        print("合格です")
    else:
        print("評価: D")
        print("残念ながら不合格です")


"""1 から 100 までの数字で FizzBuzz ゲーム"""
for num in range(1, 101):
    if num % 15 == 0:
        # 15 の倍数のとき
        print("FizzBuzz")
    elif num % 3 == 0:
        # 3 の倍数のとき
        print("Fizz")
    elif num % 5 == 0:
        # 5 の倍数のとき
        print("Buzz")
    else:
        # それ以外のとき
        print(num)
