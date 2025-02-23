"""パンの作り方の手順"""

steps = ["材料を集める", "粉と水を混ぜる", "こねる", "発酵させる", "焼く"]
print("\nパンの作り方：")

for i, step in enumerate(steps, 1):
    print(f"手順{i}: {step}")


"""テストの点数リスト"""
test_scores: list[int] = [85, 92, 78, 90, 88]

# 基本的な統計計算
average = sum(test_scores) / len(test_scores)
highest = max(test_scores)
lowest = min(test_scores)

print(f"平均点: {average}")
print(f"最高点: {highest}")
print(f"最低点: {lowest}")


"""生徒の情報"""
student = {
    "name": "鈴木花子",
    "age": 16,
    "grade": 2,
    "class": "A",
    "hobby": "バスケ",
    "favorite_subject": "数学",
}

# 必要な情報だけを取り出せる
print(f"{student['name']}さん（{student['grade']}-{student['class']}）")
print(f"趣味: {student['hobby']}")


"""電話帳"""
phone_book = {
    "太郎": "090-1111-2222",
    "花子": "080-3333-4444",
    "次郎": "070-5555-6666",
}

# 名前 （キー） から電話番号の取得ができる
print(phone_book["太郎"])
