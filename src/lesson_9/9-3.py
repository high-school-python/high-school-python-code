"""箱ひげ図の作成"""

import matplotlib.pyplot as plt
import numpy as np

# テストの点数データ
test_scores = [65, 70, 75, 78, 80, 82, 85, 88, 90, 92, 95]

# 箱ひげ図の作成
plt.figure(figsize=(10, 6))
plt.boxplot(test_scores, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# 四分位数を計算して表示
q1 = np.percentile(test_scores, 25)
q2 = np.percentile(test_scores, 50)
q3 = np.percentile(test_scores, 75)
iqr = q3 - q1

print(f"第1四分位数（Q1）：{q1}")
print(f"中央値（Q2）：{q2}")
print(f"第3四分位数（Q3）：{q3}")
print(f"四分位範囲（IQR）：{iqr}")

# 箱ひげ図に統計情報を追加
plt.title("テスト点数の箱ひげ図")
plt.xlabel("点数")
plt.yticks([1], ["テスト点数"])  # y軸のラベル

# 四分位数の位置に垂直線を追加
plt.axvline(q1, color="green", linestyle="--", alpha=0.5)
plt.axvline(q2, color="red", linestyle="--", alpha=0.5)
plt.axvline(q3, color="blue", linestyle="--", alpha=0.5)

# 統計情報をテキストで表示
plt.text(q1, 1.2, f"Q1: {q1}", color="green", ha="center")
plt.text(q2, 1.2, f"Q2: {q2}", color="red", ha="center")
plt.text(q3, 1.2, f"Q3: {q3}", color="blue", ha="center")
plt.text((q1 + q3) / 2, 1.3, f"四分位範囲: {iqr}", ha="center", bbox=dict(facecolor="white", alpha=0.5))

plt.grid(True, axis="x")
plt.tight_layout()
plt.show()


"""外れ値の検出"""
import matplotlib.pyplot as plt
import numpy as np

# テストの点数データ （外れ値: 55 を含む）
test_scores = [55, 70, 75, 78, 80, 82, 85, 88, 90, 92, 95, 98]

# 箱ひげ図の作成（外れ値も表示）
plt.figure(figsize=(10, 6))
plt.boxplot(test_scores, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# 四分位数の計算
q1 = np.percentile(test_scores, 25)
q2 = np.percentile(test_scores, 50)
q3 = np.percentile(test_scores, 75)
iqr = q3 - q1

# 外れ値の基準
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# 外れ値を検出
outliers = [x for x in test_scores if x < lower_bound or x > upper_bound]

print(f"第1四分位数（Q1）：{q1}")
print(f"中央値（Q2）：{q2}")
print(f"第3四分位数（Q3）：{q3}")
print(f"四分位範囲（IQR）：{iqr}")
print(f"外れ値の基準：{lower_bound} 未満 または {upper_bound} 超過")
print(f"検出された外れ値：{outliers}")

# グラフに外れ値の基準線を追加
plt.axvline(lower_bound, color="red", linestyle=":", label=f"外れ値の基準 ({lower_bound:.1f}, {upper_bound:.1f})")
plt.axvline(upper_bound, color="red", linestyle=":")

plt.title("テスト点数の分布と外れ値の検出")
plt.xlabel("点数")
plt.yticks([1], ["テスト点数"])
plt.legend()
plt.grid(True, axis="x")
plt.tight_layout()
plt.show()
