"""回帰分析の基本"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression

# シード値を設定して再現性を確保
np.random.seed(42)
n = 100  # データ数
x_mean = 3  # x 軸の平均値
x_std = 1  # x 軸の標準偏差
slope = 8  # 実際の傾き
intercept = 60  # 実際の切片
noise_level = 10  # ノイズレベル （大きいほど相関係数が小さくなる）

# 勉強時間のデータを生成 （正規分布に従う）
study_hours = np.random.normal(loc=x_mean, scale=x_std, size=n)
study_hours = np.clip(study_hours, 0, 6)  # 現実的な範囲に収める (0 〜 6 時間)

# ノイズを加えてテスト点数を生成
noise = np.random.normal(loc=0, scale=noise_level, size=n)
test_scores = slope * study_hours + intercept + noise
test_scores = np.clip(test_scores, 40, 100)  # 現実的な点数範囲に収める (40 〜 100 点)

# 相関係数を計算
correlation, _ = pearsonr(study_hours, test_scores)

# 線形回帰モデルの作成
X = study_hours.reshape(-1, 1)  # 形状を変換
model = LinearRegression()
model.fit(X, test_scores)  # モデルの学習

# モデルの係数 （傾きと切片）
slope_fitted = model.coef_[0]
intercept_fitted = model.intercept_

# 散布図と回帰直線の可視化
plt.figure(figsize=(12, 8))
plt.scatter(study_hours, test_scores, color="blue", s=70, alpha=0.6, label="実データ")

# 回帰直線
x_range = np.linspace(0, 6, 100).reshape(-1, 1)
y_pred = model.predict(x_range)
plt.plot(x_range, y_pred, "r-", linewidth=2, label=f"回帰直線: y = {slope_fitted:.2f}x + {intercept_fitted:.2f}")

# グラフの装飾
plt.title(f"勉強時間とテスト点数の回帰分析 (相関係数: {correlation:.2f})", fontsize=16)
plt.xlabel("勉強時間（時間）", fontsize=14)
plt.ylabel("テスト点数", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(fontsize=12)
plt.xlim(0, 6)
plt.ylim(40, 100)
plt.tight_layout()
plt.show()

# 回帰直線の解釈
print(f"回帰直線: y = {slope_fitted:.2f}x + {intercept_fitted:.2f}")
print(f"解釈: 勉強時間が 1 時間増えると、テスト点数は平均して {slope_fitted:.2f} 点上がる")
