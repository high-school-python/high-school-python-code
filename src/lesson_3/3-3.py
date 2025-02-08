"""テストの成績判定"""

score = 82

if score >= 90:
    print("評価: A")
elif score >= 80:
    print("評価: B")
elif score >= 70:
    print("評価: C")
else:
    print("評価: D")


"""条件チェックの順序が重要"""
# 間違った例
score = 95
if score >= 60:  # ここで True になってしまう
    print("合格")
elif score >= 80:  # ここはチェックされない
    print("よくできました")
elif score >= 90:  # ここもチェックされない
    print("大変よくできました")

# 正しい例 （条件を上から厳しくする）
if score >= 90:
    print("大変よくできました")
elif score >= 80:
    print("よくできました")
elif score >= 60:
    print("合格")


"""料金判定の例"""
age = 16

if age < 0:  # 例外的な条件 （最初に）
    print("エラー")
elif age <= 12:  # より具体的な条件 （子供）
    print("600円")
elif age <= 18:  # 次に具体的な条件 （学生）
    print("800円")
else:  # 最も広い条件 （大人）
    print("1000円")
