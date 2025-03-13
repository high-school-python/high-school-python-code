"""テストの点数データ"""

# テストの点数データ
scores = [78, 85, 92, 67, 88, 73, 95, 82, 89, 70]

# 基本的な統計値の計算
total = sum(scores)  # 合計
average = total / len(scores)  # 平均
maximum = max(scores)  # 最大値
minimum = min(scores)  # 最小値

print(f"合計点：{total}")
print(f"平均点：{average:.1f}")  # 小数点以下 1 桁まで表示
print(f"最高点：{maximum}")
print(f"最低点：{minimum}")
