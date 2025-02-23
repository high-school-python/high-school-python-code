"""リスト内包表記の基本的な形"""

# 通常の for 文での書き方
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)  # [1, 2, 3, 4, 5]

# リスト内包表記での書き方
numbers = [i for i in range(1, 6)]
print(numbers)  # [1, 2, 3, 4, 5]


"""計算を含むリスト内包表記"""
# 1 から 5 までの二乗のリスト

# 通常の for 文
squares = []

for i in range(1, 6):
    squares.append(i**2)

print(squares)  # [1, 4, 9, 16, 25]

# リスト内包表記
squares = [i**2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]


"""文字列の処理を含むリスト内包表記"""
# 文字列の各文字を大文字にする
word = "Python"

# 通常の for 文
upper_chars = []

for char in word:
    upper_chars.append(char.upper())

print(upper_chars)  # ['P', 'Y', 'T', 'H', 'O', 'N']

# リスト内包表記
upper_chars = [char.upper() for char in word]
print(upper_chars)  # ['P', 'Y', 'T', 'H', 'O', 'N']


"""if 条件を使ったリスト内包表記"""
# 10 以下の偶数をリストにする
# 通常の for 文
evens = []
for i in range(11):
    if i % 2 == 0:
        evens.append(i)
print(evens)  # [0, 2, 4, 6, 8, 10]

# リスト内包表記
evens = [i for i in range(11) if i % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10]


"""複雑で読みにくいリスト内包表記"""
# 複雑で読みにくい (かもしれない)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row if x % 2 == 0]
print(flattened)  # [2, 4, 6, 8]

# 普通に for 文で書く場合
flattened = []

for row in matrix:
    for x in row:
        if x % 2 == 0:
            flattened.append(x)

print(flattened)  # [2, 4, 6, 8]


"""辞書内包表記の基本的な形"""

# 通常の for 文での書き方
squares_dict = {}

for i in range(1, 6):
    squares_dict[i] = i**2

print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 辞書内包表記での書き方
squares_dict = {i: i**2 for i in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


"""if 条件を使った辞書内包表記"""

# 値が 10 以上の要素だけを含める
scores = {"Alice": 12, "Bob": 8, "Charlie": 15, "David": 9}

# 通常の for 文
high_scores = {}

for name, score in scores.items():
    if score >= 10:
        high_scores[name] = score

print(high_scores)  # {'Alice': 12, 'Charlie': 15}

# 辞書内包表記
high_scores = {name: score for name, score in scores.items() if score >= 10}
print(high_scores)  # {'Alice': 12, 'Charlie': 15}
