"""二重ループの例"""

for i in range(3):  # 外側: 3 回
    for j in range(2):  # 内側: 2 回
        print(f"i={i}, j={j}")

# 実行結果
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1


"""掛け算表"""
for i in range(1, 4):  # 外側のループ（行）
    for j in range(1, 4):  # 内側のループ（列）
        # end=" " を指定することで、改行する代わりにスペースを入れます
        print(f"{i}×{j}={i * j}", end=" ")

    # 行の終わりで改行
    print()

# 実行結果
# 1×1=1 1×2=2 1×3=3
# 2×1=2 2×2=4 2×3=6
# 3×1=3 3×2=6 3×3=9


"""星のピラミッド"""
for i in range(1, 6):  # 行数を制御
    for j in range(i):  # 各行の ★ の数を制御
        print("★", end="")

    # 行の終わりで改行
    print()

# 実行結果
# ★
# ★★
# ★★★
# ★★★★
# ★★★★★


"""座席表の作成"""
# トレイリングカンマを付けています
seats = [
    ["山田", "田中", "佐藤"],
    ["鈴木", "高橋", "伊藤"],
    ["渡辺", "山本", "中村"],
]

print("=== 座席表 ===")

for i in range(len(seats)):
    print(f"列{i + 1}:", end=" ")

    for j in range(len(seats[i])):
        print(f"{seats[i][j]}", end=" ")

    # 改行
    print()

# 実行結果
# === 座席表 ===
# 列1: 山田 田中 佐藤
# 列2: 鈴木 高橋 伊藤
# 列3: 渡辺 山本 中村


"""市松模様を描く"""
size = 5

# 偶数なら ■, 奇数なら □ を描く
for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("■", end="")
        else:
            print("□", end="")

    # 改行
    print()

# 実行結果
# ■□■□■
# □■□■□
# ■□■□■
# □■□■□
# ■□■□■
