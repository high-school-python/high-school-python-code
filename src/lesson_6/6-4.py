"""テストの点数を分析する例"""

# クラスのテスト点数リスト
scores = [82, 75, 90, 65, 88, 72, 95, 60]

# 点数の分析
max_score = max(scores)  # 最高点を求める
min_score = min(scores)  # 最低点を求める
total = sum(scores)  # 合計点を求める
count = len(scores)  # 人数を求める
average = total / count  # 平均点を計算

print("テスト結果の分析：")
print(f"最高点：{max_score}点")  # 95点
print(f"最低点：{min_score}点")  # 60点
print(f"平均点：{average:.1f}点")  # 78.4点
print(f"受験者数：{count}人")  # 8人


"""文字列を処理する例"""
# 名前の処理
name = "python programming"

# 様々な文字列操作
print(len(name))  # 文字数: 17
print(name.upper())  # すべて大文字: PYTHON PROGRAMMING
print(name.lower())  # すべて小文字: python programming
print(name.title())  # 単語の先頭を大文字: Python Programming
print(name.replace("p", "P"))  # 文字の置換: Python Programming

# 文字列の検索と判定
print(name.startswith("py"))  # "py" で始まる？: True
print(name.endswith("ing"))  # "ing" で終わる？: True
print("gram" in name)  # "gram" を含む？: True

# 空白の処理
text = "   Hello, World!   "
print(text.strip())  # 前後の空白を削除: Hello, World!


"""データ型の変換例"""
# 文字列から数値への変換
age_str = "16"
age_num = int(age_str)  # 文字列 → 整数: 16
height_str = "170.5"
height_num = float(height_str)  # 文字列 → 小数: 170.5

# 数値を文字列に変換
price = 1200
price_str = str(price)  # 整数 → 文字列: "1200"

# ユーザーからの入力を処理
height = float(input("身長 (cm) を入力："))  # 入力: "165.5" → 数値: 165.5
weight = float(input("体重 (kg) を入力："))  # 入力: "60.2" → 数値: 60.2

# BMI の計算 （小数第 1 位まで）
bmi = weight / ((height / 100) ** 2)
print(f"BMI 値: {round(bmi, 1)}")  # 小数第 1 位まで表示


"""リストの操作例"""
# 部活動の記録
times = [12.3, 11.8, 12.1, 11.5, 12.0]  # 100m 走のタイム

# 基本的な統計
best_time = min(times)  # ベストタイム
worst_time = max(times)  # ワーストタイム
average_time = sum(times) / len(times)  # 平均タイム

print("タイム分析：")
print(f"ベスト：{best_time}秒")
print(f"ワースト：{worst_time}秒")
print(f"平均：{average_time:.1f}秒")

# リストの操作
times.sort()  # タイムを昇順に並び替え
print(f"タイム一覧：{times}")  # [11.5, 11.8, 12.0, 12.1, 12.3]
times.reverse()  # 逆順に並び替え
print(f"逆順一覧：{times}")  # [12.3, 12.1, 12.0, 11.8, 11.5]
