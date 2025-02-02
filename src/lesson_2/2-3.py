"""変数名の付け方の良い例"""

student_name = "山田"  # 生徒の名前
test_score = 85  # テストの点数
total_price = 1200  # 合計金額
first_name = "太郎"  # 名前（氏名の一部）
birth_year = 2007  # 生まれた年


"""変数名の付け方の悪い例"""
なまえ = "山田"      # 日本語は避ける
test score = 85    # スペースは使えない
1st_place = "金賞"  # 数字から始まれない
if = "条件"         # 予約語は使えない
$price = 100       # 記号は使えない （ _ 以外）


"""具体的な名前をつける"""
# 悪い例
x = 85  # x が何を表すのか分からない
n = "山田"  # n が何を表すのか分からない

# 良い例
math_score = 85  # 数学の点数だと分かる
student_name = "山田"  # 生徒の名前だと分かる


"""複数の単語は _（アンダースコア）でつなぐ"""
# 推奨される書き方 （スネークケース）
user_age = 16
total_score = 85
average_height = 170.5

# スペースは使えません
user age = 16  # エラーになる


"""省略しすぎない"""
# 悪い例 （意味が分かりづらい）
num = 30  # number の意味？ count の意味？
calc = 85 + 90  # calculation? calculator?

# 良い例 （分かりやすい）
student_count = 30
total_score = 85 + 90


"""成績管理プログラムの例"""
student_name = "山田太郎"                 # 生徒の名前
math_score = 85                           # 数学の点数
english_score = 92                        # 英語の点数
total_score = math_score + english_score  # 合計点
average_score = total_score / 2           # 平均点


"""買い物プログラムの例"""
item_name = "リンゴ"                  # 商品名
unit_price = 120                     # 1個の値段
quantity = 5                         # 個数
total_price = unit_price * quantity  # 合計金額
