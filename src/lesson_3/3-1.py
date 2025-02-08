"""色々な条件分岐"""

# 天気による判断
weather = "雨"
if weather == "雨":
    print("傘を持っていきましょう")

# 点数による判断
score = 85
if score >= 80:
    print("よくできました！")

# 気温による判断
temperature = 32
if temperature >= 30:
    print("暑いので水分補給を忘れずに！")


"""コロンを忘れた例"""
if score >= 80
    print("合格です")  # SyntaxError: invalid syntax


"""字下げした例"""
temperature = 32

if temperature >= 30:
    # 字下げあり
    print("暑いです")

# 字下げなし （if 文の外）
print("気温は32度です")


"""字下げを忘れた例"""
temperature = 32

if temperature >= 30:
print("暑いです")  # IndentationError: expected an indented block


"""複数の処理を書いた例"""
score = 95

if score >= 90:
    print("大変よくできました！")
    print("次も頑張りましょう！")
    print("シールを貼りますね")


"""if 文の間違いの例"""
if score = 80: # = を使っている
if score == 80 # コロンがない
if score == 80: print("合格") # インデントがない


"""数値の比較"""
age = 16

if age >= 16:  # 16歳以上
    pass
if age < 20:  # 20歳未満
    pass
if age == 18:  # ちょうど18歳
    pass


"""文字列の比較"""
name = "山田"

if name == "山田":  # 文字列が完全に一致
    pass
if "山" in name:  # 文字列を含むか
    pass


"""真偽値の判定"""
is_student = True

if is_student:  # True かどうか
    pass
if not is_student:  # False かどうか
    pass
