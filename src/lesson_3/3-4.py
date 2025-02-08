"""高校生で成績優秀な場合を判定"""

age = 16
score = 85

if age >= 15 and score >= 80:
    print("高校生で成績優秀です！")
    print("表彰状を贈ります")


"""蒸し暑い日を判定"""
temperature = 32
humidity = 75

if temperature >= 30 and humidity >= 70:
    print("蒸し暑い日です")
    print("熱中症に注意しましょう")


"""点数が範囲外かどうかを判定"""
score = 120

if score < 0 or score > 100:
    print("点数が範囲外です")
    print("0から100の間で入力してください")


"""休日かどうかを判定"""
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("今日は休みです")
    print("ゆっくり過ごしましょう")


"""晴れではないなら傘を持っていく"""
sunny = False

if not sunny:
    print("今日は曇りか雨です")
    print("傘を持っていきましょう")


"""宿題が終わっているかどうかを判定"""
has_homework = True

if not has_homework:
    print("宿題は終わっています")
else:
    print("まだ宿題が残っています")


"""カッコがあると優先順位が明確になる"""
temperature = 28
humidity = 80
is_raining = True

# カッコがないと意図が分かりにくい
if temperature >= 30 and humidity >= 70 or is_raining:
    print("1. 傘を持って行きましょう")

# カッコをつけて意図を明確にした
if (temperature >= 30 and humidity >= 70) or is_raining:
    # 雨が降っているので実行される
    print("2. 傘を持って行きましょう")

# 別の意図の例
if temperature >= 30 and (humidity >= 70 or is_raining):
    # 気温が 30 度未満なので実行されない
    print("3. 傘を持って行きましょう")
