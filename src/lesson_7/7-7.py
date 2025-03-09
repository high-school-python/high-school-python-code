"""基本的なテスト"""


def test_calculation_functions():
    """計算関数のテスト"""

    # 足し算のテスト
    assert add(2, 3) == 5, "2 + 3 は 5 になるはず"
    assert add(-1, 1) == 0, "-1 + 1 は 0 になるはず"

    # 掛け算のテスト
    assert multiply(2, 3) == 6, "2 * 3 は 6 になるはず"
    assert multiply(0, 5) == 0, "0 * 5 は 0 になるはず"

    print("すべてのテストが成功しました！")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


try:
    test_calculation_functions()
except AssertionError as e:
    print(f"テストが失敗しました：{e}")


"""doctest を使ったテスト"""
import doctest


def add(a, b):
    """
    2つの数を足して返す関数.

    >>> add(1, 2)
    3
    """
    return a + b


if __name__ == "__main__":
    doctest.testmod(verbose=True)


"""unittest を使ったテスト"""
import unittest


class TestCalculationFunctions(unittest.TestCase):
    def test_add(self):
        """add 関数のテスト"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_multiply(self):
        """multiply 関数のテスト"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 5), 0)

    def test_average(self):
        """average 関数のテスト"""
        self.assertEqual(average([1, 2, 3]), 2)
        self.assertEqual(average([5, 5, 5]), 5)
        self.assertEqual(average([]), 0)


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    # 通常のプログラムの場合
    # unittest.main()

    # Google Colab で実行する場合
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
