"""色々なデータ型"""

# 整数型 （int）
age = 16
year = 2024

# 小数型 （float）
height = 170.5
weight = 58.3

# 文字列型 （str）
name = "鈴木"
message = "今日は晴れです"

# データ型を確認するには type() を使う
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(name))  # <class 'str'>


"""整数型の例"""
students = 40  # クラスの人数
score = 85  # テストの点数
year = 2024  # 西暦

# 整数の計算
total = students + 5  # 足し算
double = score * 2  # 掛け算


"""小数型の例"""
height = 170.5  # 身長 (cm)
weight = 58.3  # 体重 (kg)

# 小数の計算
bmi = weight / (height / 100) ** 2  # BMI の計算
average = (80.5 + 92.0 + 88.5) / 3  # 平均点の計算

# その他の例
temperature = 22.8  # 気温 (度)
price = 1200.50  # 価格 (円)


"""文字列型の例"""
name = "山田太郎"  # 名前
message = "こんにちは"  # メッセージ
address = "東京都渋谷区"  # 住所

# 文字列の連結
full_message = "こんにちは、" + name + "さん"
print(full_message)  # こんにちは、山田太郎さん


"""様々な変数の型を確認する"""
age = 16
height = 170.5
name = "鈴木"

print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(name))  # <class 'str'>


"""データ型の違いによる計算の例"""
print(5 / 2)  # 2.5 （小数の割り算）
print(5 // 2)  # 2 （整数の割り算）
print("ABC" * 3)  # ABCABCABC （文字列の繰り返し）
