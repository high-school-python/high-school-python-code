"""テストの点数の計算"""

# 5 教科の点数
scores = [85, 92, 78, 90, 88]

# 合計点を計算
total = 0
for score in scores:
    total += score

# 平均点を計算
# len 関数は、 str 型の場合は文字数でしたが、 list 型の場合は要素数です
average = total / len(scores)

print(f"点数：{scores}")
print(f"合計：{total}")
print(f"平均：{average}")

# 合格した教科の数を数える （80 点以上）
pass_count = 0

for score in scores:
    if score >= 80:
        pass_count += 1

print(f"合格した教科：{pass_count}教科")


"""名前の検索"""
names = ["山田", "田中", "佐藤", "鈴木", "高橋"]

# 「田中」 さんを探す
for name in names:
    if name == "田中":
        print("田中さんが見つかりました！")
        break
else:
    print("田中さんは見つかりませんでした")

# 「山」 のつく名前を探す
print("\n「山」のつく名前：")
for name in names:
    if "山" in name:
        print(name)
