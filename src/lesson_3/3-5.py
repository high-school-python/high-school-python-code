"""条件を変数にまとめる"""

age = 16
score = 85
attendance = 95

# 整理する前
if age >= 15 and age <= 18 and score >= 80 and attendance >= 90:
    print("表彰の対象です")

# 整理した後
is_high_school_student = age >= 15 and age <= 18
has_good_score = score >= 80
has_good_attendance = attendance >= 90

if is_high_school_student and has_good_score and has_good_attendance:
    print("表彰の対象です")


"""変数名で条件の意味を明確にする"""
# 商品の注文システム
quantity = 10
price = 1200
total = 10000
is_member = True
is_premium_member = False

is_in_stock = quantity > 0
is_valid_price = price >= 100 and price <= 10000
can_use_coupon = total >= 3000 and is_member
is_free_shipping = total >= 5000 or is_premium_member

if is_in_stock and is_valid_price:
    if can_use_coupon:
        print("クーポンが使えます")
    if is_free_shipping:
        print("送料無料です")


"""段階的にチェックする"""
score = 85

# 最初に異常値をチェック
if score < 0 or score > 100:
    print("エラー：不正な点数です")
else:
    # 成績の判定
    if score >= 90:
        print("評価: A")
    elif score >= 80:
        print("評価: B")
    elif score >= 70:
        print("評価: C")
    else:
        print("評価: D")
