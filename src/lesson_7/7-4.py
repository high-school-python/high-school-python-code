"""基本的な print デバッグ"""


def calculate_total(items):
    total = 0
    print(f"計算開始：items = {items}")  # デバッグ用出力

    for item in items:
        print(f"処理中：item = {item}")  # 各ステップの確認
        total += item
        print(f"現在の合計：{total}")  # 中間結果の確認

    print(f"計算終了：total = {total}")  # 最終結果の確認
    return total


# プログラムの実行
numbers = [10, 20, 30]
result = calculate_total(numbers)


"""目印をつけた print デバッグ"""
x = 10
y = 20

print("===== [DEBUG] 関数開始 =====")
print(f"[DEBUG] 変数 x の値: {x}")
print(f"[DEBUG] 変数 y の値: {y}")
print("===== [DEBUG] 関数終了 =====")


"""変数の型を確認する"""
value = input("数値を入力: ")
print(f"[DEBUG] value の値: {value}, 型: {type(value)}")
# 出力例: [DEBUG] value の値: 123, 型: <class 'str'>

# 数値計算の前に型を確認し、必要に応じて変換
if isinstance(value, str):
    value = int(value)


"""条件分岐の追跡"""
score = 75

print(f"[DEBUG] score の値: {score}")

if score >= 90:
    print("[DEBUG] 条件1が True: score >= 90")
    grade = "A"
elif score >= 80:
    print("[DEBUG] 条件2が True: score >= 80")
    grade = "B"
elif score >= 70:
    print("[DEBUG] 条件3が True: score >= 70")
    grade = "C"
else:
    print("[DEBUG] すべての条件が False")
    grade = "D"

print(f"[DEBUG] 最終的な grade: {grade}")


"""ループの追跡"""
numbers = [10, -5, 20, -8, 15]
positive_sum = 0

print(f"[DEBUG] 入力リスト: {numbers}")

for i, num in enumerate(numbers):
    print(f"[DEBUG] ループ {i + 1}回目: num = {num}")

    if num > 0:
        print(f"[DEBUG] 正の数を検出: {num}")
        positive_sum += num
        print(f"[DEBUG] 現在の positive_sum: {positive_sum}")

print(f"[DEBUG] 最終的な正の数の合計: {positive_sum}")
