"""名前と年齢を入力し、「あなたは ◯ 歳です」と表示するプログラム"""

# input() 関数を使ってキーボードから入力を受け取る
name = input("お名前を入力してください：")
age: str = input("年齢を入力してください：")

# 入力された年齢は文字列なので、計算するときは数値に変換する
age_num = int(age)

print("こんにちは、" + name + "さん！")
print("あなたは" + age + "歳です")
print("来年は" + str(age_num + 1) + "歳になりますね")

# f-strings を使うと、もっと簡潔に書けます。自動で str に変換してくれます。
print(f"こんにちは、{name}さん！")
print(f"あなたは{age}歳です")
print(f"来年は{age_num + 1}歳になりますね")


"""2 つの数字を入力し、その合計を「◯ + ◯ = ◯」と表示するプログラム"""
num1 = input("1 つ目の数字を入力してください：")
num2 = input("2 つ目の数字を入力してください：")

num1 = int(num1)
num2 = int(num2)

sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")
