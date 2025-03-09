"""読みやすいコード（良い例）"""


def calculate_result(base_num: int, add_num: int, multiplier: int) -> int | float:
    """2 つの数の和を計算し、条件に応じて乗算または除算を行う.

    Args:
        base_num: 基準となる数
        add_num: 加算する数
        multiplier: 乗除算に使う数

    Returns:
        int: 計算結果
    """
    # 最初の 2 つの数を加算
    sum_result = base_num + add_num

    # 合計が 10 より大きければ乗算、それ以外は除算
    if sum_result > 10:
        final_result = sum_result * multiplier
    else:
        final_result = sum_result / multiplier

    return final_result


print(calculate_result(1, 2, 3))


"""変数名の良い例と悪い例"""
# 悪い例
a = 15  # 何を表す変数か分からない
lst = [10, 20, 30]  # 中身が分からない
tmp = "東京都"  # 一時的な変数なのか、何のデータなのか不明

# 良い例
age = 15  # 年齢であることが明確
scores = [10, 20, 30]  # 点数のリストであることが分かる
city_name = "東京都"  # 都市名であることが分かる


"""関数名の良い例と悪い例"""


# 悪い例
def calc(scores):  # 何を計算するのか不明
    return sum(scores) / len(scores)


# 良い例
def calculate_average(scores):  # 平均値を計算することが明確
    return sum(scores) / len(scores)


"""ドキュメンテーション文字列"""


def calculate_discount(price, discount_rate):
    """
    商品の割引後価格を計算する関数

    Args:
        price: 元の価格
        discount_rate: 割引率（0.0〜1.0）

    Returns:
        割引後の価格（小数点以下切り捨て）
    """
    discounted_price = price * (1 - discount_rate)
    return int(discounted_price)


"""コード説明コメントの例"""
# ユーザー入力の値を数値に変換し、エラー処理を行う
try:
    user_input = input("数値を入力してください: ")
    number = float(user_input)
except ValueError:
    print("有効な数値を入力してください")
    number = 0


"""警告コメントの例"""


def fetch_data_from_api(user_id: str) -> None:
    """API からデータを取得する関数.

    Args:
        user_id: ユーザーの ID
    """
    pass


# 注意: この API は 1 分間に最大 60 回までしか呼び出せません
# 頻繁に呼び出すとエラーになる可能性があります
fetch_data_from_api(user_id="1234567890")


"""インデントと空白の例"""


# 良い例 （一貫したインデント、適切な空白）
def calculate(a, b):
    result = a + b

    if result > 10:
        return result * 2
    else:
        return result


"""空行による区切りの例"""
# 入力を受け取る
name = input("名前を入力してください: ")
age = int(input("年齢を入力してください: "))

# 条件に基づいて処理
if age >= 20:
    message = f"{name}さんは成人です"
else:
    message = f"{name}さんは未成年です"

# 結果を表示
print(message)
