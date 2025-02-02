"""真偽値の基本"""

is_student = True  # はい、学生です
has_pet = False  # いいえ、ペットは飼っていません

print(type(is_student))  # <class 'bool'>


"""数値の比較"""
age = 16
print(age > 15)  # True （15 より大きい）
print(age < 20)  # True （20 より小さい）
print(age == 16)  # True （16 と等しい）
print(age != 18)  # True （18 と異なる）
print(age >= 16)  # True （16 以上）
print(age <= 16)  # True （16 以下）


"""テストの合否判定"""
score = 85
pass_score = 70

is_passed: bool = score >= pass_score
print("合格ですか？:", is_passed)  # True

# 点数の範囲チェック
is_excellent: bool = score >= 90
is_good: bool = score >= 80 and score < 90
is_average: bool = score >= 70 and score < 80

print("優秀な成績ですか？:", is_excellent)  # False
print("良い成績ですか？:", is_good)  # True
print("平均的な成績ですか？:", is_average)  # False


"""文字列の比較"""
name = "山田"
print(name == "山田")  # True （完全に一致）
print(name != "田中")  # True （異なる）

# 文字の大小比較 （辞書順）
print("apple" < "banana")  # True （アルファベット順）
print("山田" < "田中")  # True （50 音順）


"""複数の条件を組み合わせる"""
age = 16
score = 85

# and （両方の条件が True なら True）
is_eligible = age >= 15 and score >= 80
print("参加資格がありますか？:", is_eligible)  # True

# or （どちらかの条件が True なら True）
needs_support = score < 60 or age < 15
print("サポートが必要ですか？:", needs_support)  # False

# not （条件を逆転させる）
is_adult = age >= 18
is_child = not is_adult
print("子供ですか？:", is_child)  # True


"""真偽値の計算例"""
age = 16
score = 85
print(age > 15 and score < 90)  # True
print(age == 18 or score >= 80)  # True
print(not (age < 15))  # True


"""実際のプログラムでの使用例"""
# 映画の年齢制限チェック
age = 16
movie_rating = 15
can_watch = age >= movie_rating
print("映画を見られますか？:", can_watch)  # True

# 商品の在庫チェック
stock = 5
min_stock = 3
needs_restock = stock <= min_stock
print("在庫の補充が必要ですか？:", needs_restock)  # False

# クーポン使用の条件チェック
purchase_amount = 3000
is_member = True
can_use_coupon = purchase_amount >= 2000 and is_member
print("クーポンは使用できますか？:", can_use_coupon)  # True
