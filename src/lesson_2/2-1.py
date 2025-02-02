"""変数にデータを入れる (代入する)"""

score = 85  # score という箱に 85 を入れる
name = "田中"  # name という箱に "田中" を入れる

# 変数の中身を表示する
print(score)  # 85 が表示される
print(name)  # 田中が表示される


"""変数の値を変更する"""
print("1回目のテスト:", score)  # 1回目のテスト: 85
# 同じ変数に新しい値を代入
score = 92
print("2回目のテスト:", score)  # 2回目のテスト: 92

name = "山田"
print("以前の名前:", name)  # 以前の名前: 山田
name = "鈴木"
print("新しい名前:", name)  # 新しい名前: 鈴木


"""変数を使って平均点を計算する"""
math_score = 85
english_score = 92
total = math_score + english_score  # 合計点
average = total / 2  # 平均点
print("平均点:", average)  # 平均点: 88.5


"""日本語の変数名でも一応書ける (非推奨)"""
なまえ = "山田"
print(なまえ)  # 山田


"""値が入っていない変数を使うと例外になる"""
print(undefined_score)  # NameError: name 'undefined_score' is not defined
