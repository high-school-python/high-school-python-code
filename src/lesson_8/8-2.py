"""statistics モジュールの基本"""

import statistics

# サンプルデータ
data = [75, 82, 91, 68, 88, 85, 77, 93, 84, 79]

# 基本統計量の計算
mean = statistics.mean(data)  # 平均値
median = statistics.median(data)  # 中央値
# mode は、 Python 3.8 以降では、同率一位の場合は最初に出現した値を返します
mode = statistics.mode(data)  # 最頻値 （モード）
# range とすると Python の range 関数と値が被るので、range_ とします
range_ = max(data) - min(data)  # 範囲
iqr = statistics.quantiles(data, n=4)[2] - statistics.quantiles(data, n=4)[0]  # 四分位範囲
stdev = statistics.stdev(data)  # 標準偏差
variance = statistics.variance(data)  # 分散

print(f"平均値: {mean:.1f}")
print(f"中央値: {median}")
print(f"最頻値: {mode}")
print(f"範囲: {range}")
print(f"四分位範囲: {iqr}")
print(f"標準偏差: {stdev:.2f}")
print(f"分散: {variance:.2f}")


"""テスト結果からクラスの傾向を読む"""
import statistics

# テストの点数データ （各教科 10 人分）
test_scores = {
    "国語": [75, 82, 91, 68, 88, 85, 77, 93, 84, 79],
    "数学": [82, 79, 88, 92, 75, 85, 88, 90, 78, 84],
    "英語": [88, 85, 92, 78, 85, 82, 87, 95, 89, 83],
}

for subject, scores in test_scores.items():
    # 基本統計量の計算
    mean = statistics.mean(scores)  # 平均
    median = statistics.median(scores)  # 中央値
    stdev = statistics.stdev(scores)  # 標準偏差

    print(f"\n{subject}の分析結果:")
    print(f"平均点：{mean:.1f}")
    print(f"中央値：{median}")
    print(f"標準偏差：{stdev:.1f}")
    print(f"点数分布：{min(scores)} ～ {max(scores)}")


"""得点の分布"""
import statistics

# 国語のテスト結果
japanese_scores = [75, 82, 91, 68, 88, 85, 77, 93, 84, 79]

# 得点帯ごとの人数をカウント
ranges = {
    "90点以上": 0,
    "80-89点": 0,
    "70-79点": 0,
    "60-69点": 0,
    "60点未満": 0,
}

for score in japanese_scores:
    if score >= 90:
        ranges["90点以上"] += 1
    elif score >= 80:
        ranges["80-89点"] += 1
    elif score >= 70:
        ranges["70-79点"] += 1
    elif score >= 60:
        ranges["60-69点"] += 1
    else:
        ranges["60点未満"] += 1

print("国語の得点分布:")

for range_name, count in ranges.items():
    percentage = count / len(japanese_scores) * 100
    print(f"{range_name}: {count}人 ({percentage:.1f}%)")
