"""重複の多いコード例"""

print("1 番目の生徒")
name1 = "田中"
score1 = 85

grade1 = ""
if score1 >= 90:
    grade1 = "A"
elif score1 >= 80:
    grade1 = "B"
elif score1 >= 70:
    grade1 = "C"
else:
    grade1 = "D"

print(f"{name1}さんの成績は{grade1}です")

print("\n2 番目の生徒")
name2 = "鈴木"
score2 = 92
grade2 = ""

if score2 >= 90:
    grade2 = "A"
elif score2 >= 80:
    grade2 = "B"
elif score2 >= 70:
    grade2 = "C"
else:
    grade2 = "D"

print(f"{name2}さんの成績は{grade2}です")


"""関数を使って整理したコード"""


def get_grade(score: int) -> str:
    """点数から成績（A / B / C / D）を判定する.

    Args:
        score (int): 点数

    Returns:
        str: 成績（A / B / C / D）
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"


def print_result(name: str, score: int) -> None:
    """生徒の成績を表示する.

    Args:
        name (str): 名前
        score (int): 点数
    """
    grade = get_grade(score)
    print(f"{name}さんの成績は{grade}です")


# 複数の生徒を簡単に処理
students = [("田中", 85), ("鈴木", 92), ("佐藤", 78)]

for name, score in students:
    print_result(name, score)
