"""インデックスエラーの修正"""

# エラーコード
fruits = ["りんご", "バナナ", "オレンジ"]
print(fruits[3])  # IndexError: list index out of range

# 修正方法 1: 正しいインデックスを使用
print(fruits[2])  # オレンジ（3番目の要素はインデックス2）

# 修正方法 2: インデックスの範囲をチェック
if len(fruits) > 3:
    print(fruits[3])
else:
    print("インデックスが範囲外です")


"""名前エラーの修正"""
# エラーコード
price = 1200
total = price * quantity  # NameError: name 'quantity' is not defined

# 修正方法: 変数を事前に定義する
price = 1200
quantity = 3  # 変数を定義
total = price * quantity  # これで正しく動作


"""型エラーの修正"""
# エラーコード
text = "答え：" + 42  # TypeError: can only concatenate str (not "int") to str

# 修正方法 1: 整数を文字列に変換
text = "答え：" + str(42)  # str() で整数を文字列に変換

# 修正方法 2: f文字列を使用
text = f"答え：{42}"  # f文字列なら型を気にする必要がない
