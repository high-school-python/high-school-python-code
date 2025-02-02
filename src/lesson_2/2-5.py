"""型変換が必要なケース"""

score = 85
message = "得点は" + score + "点です"  # エラー！
# TypeError: can only concatenate str (not "int") to str


"""型変換をしたケース"""
score = 85
message = "得点は" + str(score) + "点です"  # 得点は85点です


"""文字列を数値に変換"""
# 文字列 → 整数 int()
age_str = "16"
age_num = int(age_str)  # 文字列を整数に変換
print(age_num + 1)  # 17 (計算ができる)

# 文字列 → 小数 float()
height_str = "170.5"
height_num = float(height_str)  # 文字列を小数に変換
print(height_num + 1)  # 171.5 (計算ができる)


"""数値を文字列に変換"""
# 数値 → 文字列 str()
score = 85
score_str = str(score)  # 数値を文字列に変換
message = "得点は" + score_str + "点です"
print(message)  # 得点は85点です

# 小数 → 文字列 str()
height = 170.5
height_str = str(height)  # 小数を文字列に変換
print("身長は" + height_str + "cmです")  # 身長は170.5cmです


"""整数と小数の変換"""
# 小数 → 整数 (小数点以下切り捨て)
height = int(170.8)  # 170
price = int(1200.9)  # 1200

# 整数 → 小数
count = float(80)  # 80.0
rate = float(100)  # 100.0


"""具体的な型変換の例"""
# 入力された文字列を数値として計算
height_str = "170.5"
weight_str = "60.2"

height = float(height_str)
weight = float(weight_str)

# BMI の計算
bmi = weight / (height / 100) ** 2
# 小数点第 1 位まで表示
print("BMI:", round(bmi, 1))  # BMI: 24.2

# 計算結果を文字列として整形
result = f"身長 {height} cm, 体重 {weight} kg の BMI は {round(bmi, 1)} です"
print(result)  # 身長 170.5cm, 体重60.2kg の BMI は 24.2 です


"""ユーザー入力の処理"""
# ユーザーからの入力は常に文字列として扱われます
# 実際のプログラムでは input() を使って、ユーザーからの入力を受け取ります
age_str = "16"
age = int(age_str)
next_year = age + 1
print(f"来年は{next_year}歳になります")  # 来年は17歳になります


"""データの表示整形"""
score = 85
total = 100
rate = score / total * 100
message = f"得点率は {str(round(rate, 1))}% です"
print(message)  # 得点率は 85.0% です


"""複数の型変換を組み合わせる"""
# 文字列の小数を整数に変換
price_str = "1200.8"
price = int(float(price_str))  # 一度 float に変換してから int に変換
print(price)  # 1200
