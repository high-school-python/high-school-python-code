"""文字列の連結"""

first = "山田"
last = "太郎"
full_name = first + last
print(full_name)  # 山田太郎

# スペースを入れて連結
full_name = first + " " + last
print(full_name)  # 山田 太郎

# 文字列と数値を連結する時は str() で変換が必要
age = 16
message = "私は" + str(age) + "歳です"
print(message)  # 私は16歳です


"""文字列の繰り返し"""
star = "★"
print(star * 3)  # ★★★
print("わくわく" * 2)  # わくわくわくわく

# 装飾的な使い方
print("=" * 20)  # ====================
print("Hello!")  # Hello!
print("=" * 20)  # ====================


"""文字列の長さを調べる"""
message = "こんにちは"
print(len(message))  # 5

name = "山田 太郎"  # スペースも 1 文字として数えます
print(len(name))  # 5

english = "Hello!"
print(len(english))  # 6


"""文字列から一部を取り出す"""
text = "Python"
print(text[0])  # P （最初の文字）
print(text[1])  # y （2番目の文字）
print(text[-1])  # n （最後の文字）

# スライスで範囲を指定して取り出す
print(text[0:2])  # Py （0 番目から 2 番目の手前まで）
print(text[2:4])  # th （2 番目から 4 番目の手前まで）
print(text[:3])  # Pyt （最初から 3 番目の手前まで）
print(text[2:])  # thon （2 番目から最後まで）


"""文字列の検索と置換"""
# 文字列の検索
text = "私は Python が好きです"
print("Python" in text)  # True （含まれているか確認）
print(text.find("Python"))  # 3 （出現位置。見つからない場合は -1）
print(text.find("JavaScript"))  # -1 （見つからないので -1）

# 文字列の置換
message = "私はりんごが好きです"
new_message = message.replace("りんご", "バナナ")
print(new_message)  # 私はバナナが好きです


"""よく使う文字列メソッド"""
# あえて左右に空白を入れています
text = "  Hello, Python!  "

# 空白の削除
print(text.strip())  # "Hello, Python!" (前後の空白を削除)

# 大文字・小文字の変換
print(text.upper())  # "  HELLO, PYTHON!  " (大文字に)
print(text.lower())  # "  hello, python!  " (小文字に)

# 文字列の分割
words = "りんご,バナナ,オレンジ"
fruit_list = words.split(",")  # ["りんご", "バナナ", "オレンジ"]


"""実践的な文字列操作の例"""
# ユーザー名とパスワードの作成
username = "yamada_taro"
domain = "example.com"
email = username + "@" + domain  # メールアドレスの作成
print(email)  # yamada_taro@example.com

# 整形された出力の作成
name = "山田太郎"
score = 85
result = f"{name}さんの点数は{score}点です"
print(result)  # 山田太郎さんの点数は85点です

# ファイル名から拡張子を取り出す
filename = "report.pdf"
extension = filename[-4:]  # 後ろから 4 文字を取得
print(extension)  # .pdf
