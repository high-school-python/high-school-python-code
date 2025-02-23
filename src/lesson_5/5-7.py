"""生徒の辞書リスト"""

students = [
    {"name": "山田太郎", "age": 16, "class": "A"},
    {"name": "鈴木花子", "age": 15, "class": "B"},
    {"name": "佐藤次郎", "age": 17, "class": "C"},
]

# データの表示
for student in students:
    print(f"{student['name']} ({student['age']}歳) - {student['class']}組")


"""各教科の試験結果"""
# 4 人分の試験結果
test_results = {
    "数学": [85, 92, 78, 90],
    "英語": [92, 88, 85, 95],
    "国語": [88, 90, 85, 82],
}

# 教科ごとの平均点を計算
for subject, scores in test_results.items():
    average = sum(scores) / len(scores)
    # 平均点を小数第 1 位まで表示
    print(f"{subject}の平均点: {average:.1f}")


"""クラスごとの成績管理"""
classes_data = {
    "A組": [
        {"name": "山田太郎", "scores": {"数学": 85, "英語": 92, "国語": 88}},
        {"name": "鈴木花子", "scores": {"数学": 92, "英語": 88, "国語": 90}},
    ],
    "B組": [
        {"name": "佐藤次郎", "scores": {"数学": 78, "英語": 85, "国語": 85}},
        {"name": "田中明", "scores": {"数学": 90, "英語": 95, "国語": 82}},
    ],
}

# クラスごとの成績表示
for class_name, students in classes_data.items():
    print(f"{class_name}の成績:")

    for student in students:
        print(f"{student['name']}の成績:")

        for subject, score in student["scores"].items():
            print(f"  {subject}: {score}点")

    print()
