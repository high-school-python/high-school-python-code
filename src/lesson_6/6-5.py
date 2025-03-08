"""モジュールの基本的な使い方"""

# math モジュールを読み込む
import math

# モジュールの機能を使う
radius = 5
area = math.pi * radius * radius  # 円の面積を計算
print(f"半径{radius}の円の面積：{area:.2f}")


"""数学関連の機能を使う例"""
import math

# 円周率と平方根
print(f"円周率：{math.pi}")  # 3.141592...
print(f"2の平方根：{math.sqrt(2)}")  # 1.4142...

# 三角関数（ラジアン）
angle_deg = 45  # 45 度
angle_rad = math.radians(angle_deg)  # 度 → ラジアン (rad)
sin_value = math.sin(angle_rad)  # サイン (sin)
cos_value = math.cos(angle_rad)  # コサイン (cos)
print(f"{angle_deg}度の sin 値: {sin_value:.4f}")

# 切り上げ, 切り捨て, 四捨五入
price = 1234.56
print(f"切り上げ: {math.ceil(price)}")  # 1235
print(f"切り捨て: {math.floor(price)}")  # 1234
print(f"四捨五入: {round(price)}")  # 1235


"""ランダム機能を使う例"""
import random

# サイコロを振る
dice = random.randint(1, 6)  # 1 から 6 のランダムな整数
print(f"サイコロの目：{dice}")

# じゃんけんをランダムに選ぶ
hands = ["グー", "チョキ", "パー"]
computer_hand = random.choice(hands)  # リストからランダムに選択
print(f"コンピュータの手：{computer_hand}")

# カードをシャッフル
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
random.shuffle(cards)  # リストをシャッフル
print(f"シャッフル後：{cards}")


"""日付と時刻の処理例"""
from datetime import datetime, timedelta

# 現在の日時を取得
now = datetime.now()
print(f"現在の日時：{now}")
print(f"今日は{now.year}年{now.month}月{now.day}日")
print(f"現在時刻：{now.hour}時{now.minute}分{now.second}秒")

# 日付の計算
tomorrow = now + timedelta(days=1)  # 1 日後
next_week = now + timedelta(weeks=1)  # 1 週間後
print(f"明日：{tomorrow.date()}")
print(f"来週：{next_week.date()}")

# 誕生日までの日数を計算
birthday = datetime(2024, 12, 25)  # 2024年12月25日
days_until = (birthday - now).days
print(f"誕生日まであと{days_until}日")


"""日付と時刻の処理例（まとめて読み込む）"""
import datetime

# 現在の日時を取得
now = datetime.datetime.now()
print(f"現在の日時：{now}")
print(f"今日は{now.year}年{now.month}月{now.day}日")
print(f"現在時刻：{now.hour}時{now.minute}分{now.second}秒")

# 日付の計算
tomorrow = now + datetime.timedelta(days=1)  # 1 日後
next_week = now + datetime.timedelta(weeks=1)  # 1 週間後
print(f"明日：{tomorrow.date()}")
print(f"来週：{next_week.date()}")

# 誕生日までの日数を計算
birthday = datetime.datetime(2024, 12, 25)  # 2024年12月25日
days_until = (birthday - now).days
print(f"誕生日まであと{days_until}日")
