"""辞書の値の追加・更新"""

student = {"name": "山田太郎", "age": 16}

# 新しい要素の追加
student["grade"] = 2
student["class"] = "A"
print(student)  # {'name': '山田太郎', 'age': 16, 'grade': 2, 'class': 'A'}

# 値の更新
student["age"] = 17
print(student)  # {'name': '山田太郎', 'age': 17, 'grade': 2, 'class': 'A'}


"""複数の要素を一度に追加"""
student = {"name": "山田太郎", "age": 16, "class": "A"}
student.update({"grade": 2, "club": "サッカー部"})
print(student)


"""del による削除"""
student = {"name": "山田太郎", "age": 16, "grade": 2, "temp": "仮データ"}

# 特定の要素を削除
del student["temp"]
print(student)  # temp キーが削除された辞書が表示される


"""pop による削除（値の取り出し）"""
# popで要素を削除しながら値を取得
student = {"name": "山田太郎", "age": 16, "grade": 2}

# 要素を削除して値を取得
age = student.pop("age")
print(f"取り出した年齢: {age}")
print(f"残りのデータ: {student}")

# 存在しないキーでもエラーにならない
club = student.pop("club", "未所属")  # キーが存在しない場合のデフォルト値
print(f"部活動: {club}")  # 未所属


"""clear() による全要素の削除"""
scores = {"国語": 85, "数学": 92, "英語": 78}
print(f"クリア前: {scores}")

scores.clear()  # すべての要素を削除
print(f"クリア後: {scores}")  # {}
