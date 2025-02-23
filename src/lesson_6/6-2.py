"""長方形の面積を計算して返す関数"""


def calculate_rectangle_area(width, height):
    area = width * height  # 面積を計算
    return area  # 計算結果を返す


# 関数を使う
result = calculate_rectangle_area(5, 3)  # 戻り値を変数に入れる
print(f"面積は{result}平方センチメートルです")  # 面積は15平方センチメートルです

# 関数の結果を直接使うこともできます
total_area = calculate_rectangle_area(4, 6) + calculate_rectangle_area(3, 2)
print(f"2つの長方形の面積の合計：{total_area}")  # 30平方センチメートル


"""型ヒントと Docstring を使った関数"""


def calculate_rectangle_area(width: float, height: float) -> float:
    """長方形の面積を計算して返す.

    Args:
        width (float): 長方形の幅
        height (float): 長方形の高さ

    Returns:
        float: 長方形の面積
    """
    area = width * height
    return area


"""戻り値を使った計算例"""


def calculate_price_with_tax(price: float) -> float:
    """税込価格を計算して返す.

    Notes:
        消費税率は 10% で計算します。

    Args:
        price (float): 税抜価格

    Returns:
        float: 税込価格
    """
    tax_rate = 0.1
    tax = price * tax_rate
    total = price + tax

    return total


# 商品の合計金額を計算
item1_price = calculate_price_with_tax(1000)  # 1,100 円
item2_price = calculate_price_with_tax(2000)  # 2,200 円
total_price = int(item1_price + item2_price)

# カンマを使って桁区切りを表示
print(f"合計金額（税込）：{total_price:,} 円")  # 3,300円


"""成績判定をする関数"""


def calculate_grade(score: int) -> str:
    """点数から成績を計算して返す.

    Args:
        score (int): 点数

    Returns:
        str: 成績
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"

    # 60 点未満は F
    return "F"


# 関数を使って成績を判定
my_score = 85
my_grade = calculate_grade(my_score)
print(f"{my_score} 点の成績は {my_grade} です")  # 85 点の成績は B です
