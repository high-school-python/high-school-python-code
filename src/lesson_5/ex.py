"""クラスの成績管理プログラム"""

class_scores = {
    "山田太郎": 85,
    "鈴木花子": 92,
    "佐藤次郎": 78,
    "田中美咲": 95,
    "高橋健一": 88,
}

# 平均点を計算
total = sum(class_scores.values())
average = total / len(class_scores)
# 平均点を小数第 1 位まで表示
print(f"クラスの平均点：{average:.1f}")

# 平均点以上の生徒を表示
print("\n平均点以上の生徒：")

for name, score in class_scores.items():
    if score >= average:
        print(f"{name}: {score}点")


"""好きな果物リストを作り、最初と最後の要素を表示するプログラム"""
# 果物リストを作成
fruits = []

# 果物を追加
while True:
    fruit = input("好きな果物を入力してください（終了する場合は quit と入力してください）:")

    if fruit == "quit":
        break

    fruits.append(fruit)

# リストが空でない場合のみ表示
if fruits:
    print("\n入力された果物リスト：")
    print(fruits)
    print(f"最初の果物：{fruits[0]}")
    print(f"最後の果物：{fruits[-1]}")
    print(f"果物の総数：{len(fruits)}個")
else:
    print("果物が入力されませんでした")
