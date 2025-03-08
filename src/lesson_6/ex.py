"""足し算・引き算・平均値を計算する関数を作り、モジュールとして利用するプログラム"""


def add(a: int, b: int) -> int:
    """2 つの数の和を返す.

    Args:
        a (int): 数値 1
        b (int): 数値 2

    Returns:
        int: 和
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """2 つの数の差を返す.

    Args:
        a (int): 数値 1
        b (int): 数値 2

    Returns:
        int: 差
    """
    return a - b


def average(numbers: list[int]) -> float:
    """数値リストの平均を返す.

    Args:
        numbers (list[int]): 数値リスト

    Returns:
        float: 平均
    """
    return sum(numbers) / len(numbers)


# メイン処理
if __name__ == "__main__":
    # テスト用のコード
    print(add(10, 5))  # 15
    print(subtract(10, 5))  # 5
    print(average([1, 2, 3, 4, 5]))  # 3.0


"""2 つの数値を入力して最大公約数を求める関数を作成するプログラム"""


def gcd(a: int, b: int) -> int:
    """ユークリッドの互除法で最大公約数を求める.

    Args:
        a (int): 数値 1
        b (int): 数値 2

    Returns:
        int: 最大公約数
    """
    while b:
        a, b = b, a % b

    return a


def get_positive_number(prompt: str) -> int:
    """正の整数を入力させる.

    Args:
        prompt (str): 入力を促すメッセージ

    Returns:
        int: 正の整数
    """
    while True:
        try:
            num = int(input(prompt))

            if num > 0:
                return num

            print("正の整数を入力してください")
        except ValueError:
            print("正しい数値を入力してください")


def main() -> None:
    # 2 つの数を入力
    num1 = get_positive_number("1 つ目の数を入力：")
    num2 = get_positive_number("2 つ目の数を入力：")

    # 最大公約数を計算
    result = gcd(num1, num2)

    # 結果を表示
    print(f"{num1}と{num2}の最大公約数は{result}です")


# プログラムの実行
if __name__ == "__main__":
    main()
