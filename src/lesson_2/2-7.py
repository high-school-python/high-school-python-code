"""成績管理プログラムの例"""

# 生徒の情報を変数で管理
name: str = "山田太郎"
grade: int = 2
class_number: str = "A"
math_score: int = 92
english_score: int = 78
is_passed: bool = True

# 情報を整形して表示
print("=== 成績情報 ===")
print("名前：" + name)
print("学年：" + str(grade))
print("クラス：" + class_number)
print("数学：" + str(math_score) + "点")
print("英語：" + str(english_score) + "点")
print("合格：" + str(is_passed))

# 平均点の計算と判定
total = math_score + english_score
average = total / 2
is_excellent = average >= 90

print("合計点：" + str(total) + "点")
print("平均点：" + str(average) + "点")
print("優秀者：" + str(is_excellent))


"""f-strings を使った表示方法"""
print(f"=== {name}の成績情報 ===")
print(f"学年：{grade}年{class_number}組")
print(f"数学：{math_score}点")
print(f"英語：{english_score}点")
print(f"平均：{average:.1f}点")  # 小数点 1 桁まで表示


"""商品情報の管理"""
product_name: str = "ノート"
price: int = 280
quantity: int = 25
tax_rate: float = 0.10
is_available: bool = True

# 在庫金額の計算
total_price: int = price * quantity
tax_amount: float = total_price * tax_rate
total_with_tax: float = float(total_price) + tax_amount

# 在庫状況の判定
is_low_stock: bool = quantity < 20
needs_reorder: bool = quantity <= 10

# 情報の表示
print("【商品情報】")
print(f"商品名：{product_name}")
print(f"単価：{price}円")
print(f"在庫数：{quantity}個")
print(f"在庫金額：{total_price}円")
print(f"消費税：{tax_amount}円")
print(f"税込金額：{total_with_tax}円")
print(f"販売可能：{is_available}")
print(f"在庫少：{is_low_stock}")
print(f"要発注：{needs_reorder}")


"""本の情報管理"""
title: str = "Python入門"
author: str = "情報太郎"
page_count: int = 248
price: int = 2800
rating: float = 4.5
is_borrowed: bool = False
return_date: str = "2024-02-15"

# 貸出状況の表示
print("【書籍情報】")
print(f"タイトル：{title}")
print(f"著者：{author}")
print(f"ページ数：{page_count}ページ")
print(f"価格：{price}円")
print(f"評価：{rating}点")

if is_borrowed:
    print(f"貸出中（返却予定日：{return_date}）")
else:
    print("貸出可能")


"""f-strings の便利な機能"""
price: int = 1234567
rate: float = 3.14159

print(f"価格：{price:,}円")  # カンマ区切り
print(f"比率：{rate:.2f}")  # 小数点 2 桁まで
print(f"名前：{'山田':10}さん")  # 10 文字分の空白確保
