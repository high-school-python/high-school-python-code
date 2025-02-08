"""生徒の情報を辞書で管理"""

student = {
    "name": "山田太郎",  # キー: "name", 値: "山田太郎"
    "age": 16,  # キー: "age", 値: 16
    "grade": 2,  # キー: "grade", 値: 2
    "class": "A",  # キー: "class", 値: "A"
}

# 空の辞書を作る
my_dict = {}


"""辞書の値を取り出す"""
student = {"name": "山田太郎", "age": 16, "grade": 2, "class": "A"}

# [ ] を使って取り出す
print(student["name"])  # 山田太郎
print(student["age"])  # 16

# get() を使って安全に取り出す
print(student.get("name"))  # 山田太郎
print(student.get("height"))  # None （キーが存在しない場合）
print(student.get("height", 0))  # 0 （デフォルト値を指定）


"""キーと値の取得"""
student = {"name": "山田太郎", "age": 16, "grade": 2, "class": "A"}

# キーの一覧を取得
keys = student.keys()
print(list(keys))  # ['name', 'age', 'grade', 'class']

# 値の一覧を取得
values = student.values()
print(list(values))  # ['山田太郎', 16, 2, 'A']

# キーと値のペアを取得
items = student.items()
for key, value in items:
    print(f"{key}: {value}")
