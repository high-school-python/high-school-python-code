"""引数を使ったあいさつプログラム"""


def greet_person(name: str) -> None:
    """名前を引数に取る関数.

    Args:
        name (str): 名前
    """
    print(f"こんにちは、{name}さん！")
    print("今日も頑張りましょう！")


# いろいろな名前で呼び出してみる
greet_person("太郎")  # こんにちは、太郎さん！
greet_person("花子")  # こんにちは、花子さん！
greet_person("先生")  # こんにちは、先生さん！


"""BMI を計算する関数"""


def calculate_bmi(weight: float, height: float) -> float:
    """BMI を計算する関数.

    Args:
        weight (float): 体重（kg）
        height (float): 身長（cm）
    """
    # 身長をメートルに変換
    height_m = height / 100
    # BMI の計算式: 体重 (kg) ÷ 身長 (m) の 2 乗
    bmi = weight / (height_m * height_m)
    # 小数第 1 位まで丸めて返す
    return round(bmi, 1)


# 関数を使って BMI を計算
my_bmi = calculate_bmi(60, 170)  # 体重 60 kg, 身長 170 cm
print(f"BMI 値: {my_bmi}")

friend_bmi = calculate_bmi(55, 165)  # 体重 55 kg, 身長 165 cm
print(f"友達の BMI 値: {friend_bmi}")


"""デフォルト値を使った関数"""


def power(base: int, exponent: int = 2) -> int:
    """数値のべき乗を計算する.

    Args:
        base (int): 基数
        exponent (int, optional): 指数（デフォルトは 2）
    """
    return base**exponent


# いろいろな使い方
print(power(3))  # 3 の 2 乗 = 9 （exponent を省略 → デフォルト値の 2 が使われる）
print(power(3, 3))  # 3 の 3 乗 = 27 （exponent に 3 を指定）
print(power(2, 4))  # 2 の 4 乗 = 16 （exponent に 4 を指定）


def create_greeting(name: str, greeting: str = "こんにちは") -> str:
    """あいさつ文を作る.

    Args:
        name (str): 名前
        greeting (str, optional): あいさつ（デフォルトは「こんにちは」）
    """
    return f"{greeting}、{name}さん！"


print(create_greeting("太郎"))  # こんにちは、太郎さん！
print(create_greeting("花子", "おはよう"))  # おはよう、花子さん！


"""キーワード引数を使う"""


def create_profile(name: str, age: int, hobby: str) -> str:
    return f"私は{name}です。{age}歳です。趣味は{hobby}です。"


# 通常の呼び出し （順番通りに渡す）
profile1 = create_profile("太郎", 16, "サッカー")
# キーワード引数を使う （順番は関係ない）
profile2 = create_profile(hobby="野球", name="次郎", age=15)

print(profile1)
print(profile2)
