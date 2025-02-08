"""append() で末尾に追加"""

foods = ["カレー", "ラーメン"]
foods.append("寿司")
print(foods)  # ['カレー', 'ラーメン', '寿司']

# 複数回追加
foods.append("うどん")
foods.append("そば")
print(foods)  # ['カレー', 'ラーメン', '寿司', 'うどん', 'そば']


"""insert() で指定位置に追加"""
foods = ["カレー", "ラーメン", "寿司"]
# インデックス 1 の位置に挿入
foods.insert(1, "うどん")
print(foods)  # ['カレー', 'うどん', 'ラーメン', '寿司']

# 先頭に追加
foods.insert(0, "そば")
print(foods)  # ['そば', 'カレー', 'うどん', 'ラーメン', '寿司']


"""remove() で指定した要素を削除"""
foods = ["カレー", "ラーメン", "寿司", "うどん"]
foods.remove("ラーメン")
print(foods)  # ['カレー', '寿司', 'うどん']

# 存在しない要素を削除しようとするとエラーになります
foods.remove("パスタ")


"""del でインデックスを指定して削除"""
foods = ["カレー", "ラーメン", "寿司", "うどん"]
# インデックス 1 の要素を削除
del foods[1]
print(foods)  # ['カレー', '寿司', 'うどん']

# 範囲を指定して削除
# インデックス 1 から 2 までを削除
del foods[1:3]
print(foods)  # ['カレー']

# 範囲外のインデックスを指定するとエラーになります
del foods[10]


"""pop() で要素を取り出して削除"""
foods = ["カレー", "ラーメン", "寿司"]
last_food = foods.pop()
print(f"取り出した要素: {last_food}")  # 寿司
print(f"残りのリスト: {foods}")  # ['カレー', 'ラーメン']

# インデックスを指定して取り出し
second_food = foods.pop(1)  # インデックス1の要素を取り出す
print(f"取り出した要素: {second_food}")  # ラーメン
print(f"残りのリスト: {foods}")  # ['カレー']


"""sort() で要素の並び替え"""
# 数値のソート
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()  # 昇順に並び替え
print(numbers)  # [1, 1, 2, 3, 4, 5, 9]

numbers.sort(reverse=True)  # 降順に並び替え
print(numbers)  # [9, 5, 4, 3, 2, 1, 1]

# 文字列のソート
names = ["田中", "山田", "佐藤", "鈴木"]
names.sort()  # 50音順に並び替え
print(names)  # ['佐藤', '鈴木', '田中', '山田']


"""reverse() で順序を反転"""
foods = ["カレー", "ラーメン", "寿司"]
foods.reverse()
print(foods)  # ['寿司', 'ラーメン', 'カレー']


"""count() で要素の数を数える"""
numbers = [1, 2, 3, 2, 1, 2, 4, 5]
count_2 = numbers.count(2)
print(f"2 の出現回数: {count_2}")  # 3

# 文字列でも使える
fruits = ["りんご", "バナナ", "りんご", "オレンジ", "りんご"]
count_apple = fruits.count("りんご")
print(f"りんごの数: {count_apple}")  # 3
