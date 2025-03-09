"""基本的なエラー"""


def practice_errors():
    # 1. NameError: 定義されていない変数を使用
    try:
        print(undefined_name)  # この変数は定義されていない
    except NameError as e:
        print(f"変数が定義されていません：{e}")
        print(f"エラーの種類：{type(e).__name__}")
        print("--------------------")

    # 2. TypeError: 異なる型の演算
    try:
        result = "hello" + 123  # 文字列と数値は直接足せない
    except TypeError as e:
        print(f"型が合っていません：{e}")
        print(f"エラーの種類：{type(e).__name__}")
        print("--------------------")

    # 3. IndexError: リストの範囲外にアクセス
    try:
        list_data = [1, 2, 3]
        print(list_data[10])  # リストの範囲外のインデックス
    except IndexError as e:
        print(f"リストの範囲外です：{e}")
        print(f"エラーの種類：{type(e).__name__}")
        print("--------------------")


# 実行
practice_errors()


"""例外クラスの階層を確認"""


def explore_exception_hierarchy():
    # 例外クラスの階層を確認
    import builtins

    # 組み込み例外の一覧を取得
    exception_classes = []

    for name in dir(builtins):
        obj = getattr(builtins, name)
        if isinstance(obj, type) and issubclass(obj, BaseException):
            exception_classes.append(obj)

    # 例外の階層を表示
    for exc_class in exception_classes:
        if exc_class.__base__ is BaseException or exc_class.__base__ is Exception:
            print(f"{exc_class.__name__}")

            # サブクラスを表示
            for sub_class in exception_classes:
                if sub_class.__base__ is exc_class and sub_class is not exc_class:
                    print(f"  └─ {sub_class.__name__}")


explore_exception_hierarchy()


"""Student クラスの例"""


class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def calculate_grade(self, score: int) -> str:
        """点数から成績を計算するメソッド.

        Args:
            score (int): 点数

        Returns:
            str: 成績
        """
        if score < 0 or score > 100:
            raise ValueError("点数は0〜100の範囲で入力してください")

        if score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        else:
            return "D"


"""Student オブジェクトの作成"""
student_1 = Student("John", 20)
student_2 = Student("Michel", 22)


"""HighSchoolStudent クラスの作成"""


class HighSchoolStudent(Student):
    def __init__(self, name: str, age: int, grade: int):
        super().__init__(name, age)
        self.grade = grade


"""HighSchoolStudent オブジェクトの作成"""
high_school_student = HighSchoolStudent("John", 20, 3)
