"""range(stop) の使い方"""

print("5 回繰り返し:")

for i in range(5):
    print(i)

# 5 回繰り返し:
# 0
# 1
# 2
# 3
# 4


"""range(start, stop) の使い方"""
print("1 から 5 まで表示:")

for i in range(1, 6):
    print(i)

# 1 から 5 まで表示:
# 1
# 2
# 3
# 4
# 5


"""range(start, stop, step) の使い方"""
# 0 から 8 まで 2 ずつ増やす
print("偶数の表示:")

for i in range(0, 10, 2):
    print(i)

# 偶数の表示:
# 0
# 2
# 4
# 6
# 8


"""逆順に使う"""
# 5 から 1 まで表示
for i in range(5, 0, -1):
    print(i)

# 5 から 1 まで表示:
# 5
# 4
# 3
# 2
# 1
