"""構文エラーの例"""
# カッコの閉じ忘れ
print("Hello World"  # 閉じカッコがない

# コロンの忘れ
if x > 5
    print("x は 5 より大きい")  # if 文の後のコロンがない


"""インデントエラーの例"""
if x > 5:
print("x は 5 より大きい")  # インデントがない

# または混在したインデント
if x > 5:
    print("正しいインデント")
   print("間違ったインデント")  # スペースの数が違う


"""名前エラーの例"""
# 変数名のタイプミス
message = "こんにちは"
print(mesage)  # 正しくは message

# 定義前に使用
print(total)  # total はまだ定義されていない
total = 0


"""型エラーの例"""
# 文字列と数値の足し算
name = "山田"
age = 15
result = name + age  # 文字列と数値は直接足せない

# 数値でない物に掛け算
result = "hello" * "world"  # 文字列同士の掛け算はできない


"""インデックスエラーの例"""
fruits = ["りんご", "バナナ", "オレンジ"]
print(fruits[3])  # インデックスは 0, 1, 2 しかない

name = "Python"
print(name[10])  # 文字列の長さは 6 なので 10 番目の文字はない


"""属性エラーの例"""
number = 42
number.append(10)  # 数値型には append メソッドはない

text = "Hello"
text.update()  # 文字列型には update メソッドはない


"""タイプミスの例と対策"""
# 間違った例
counter = 0
conter = conter + 1  # counter のタイプミス

# 対策：変数名を統一し、わかりやすい命名を心がける
counter = 0
counter = counter + 1  # 正しく counter と書く


"""カッコの対応忘れの例と対策"""
# 間違った例
print("Hello", (2 + 3 * 4)  # 閉じカッコが足りない

# 対策：エディタの括弧強調機能を使う
print("Hello", (2 + 3 * 4))  # 正しく閉じカッコを入れる


"""インデントのズレの例と対策"""
# 間違った例
if x > 5:
    print("x は 5 より大きい")
   print("処理を続けます")  # インデントが揃っていない

# 対策：インデントを揃える
if x > 5:
    print("x は 5 より大きい")
    print("処理を続けます")  # インデントを揃える


"""型の混在の例と対策"""
# 間違った例
age = input("年齢を入力してください: ")
birth_year = 2023 - age  # input は文字列を返すので計算できない

# 対策：適切な型変換を行う
age = input("年齢を入力してください: ")
birth_year = 2023 - int(age)  # int() で数値に変換
