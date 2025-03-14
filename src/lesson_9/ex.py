"""クラス全員の身長データから平均・中央値・標準偏差を計算して特徴をまとめる"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def analyze_height_data():
    # 身長データ （cm）
    heights = [
        158,
        160,
        165,
        168,
        170,
        172,
        175,
        163,
        167,
        169,
        164,
        166,
        171,
        173,
        168,
        167,
        165,
        170,
        172,
        169,
    ]

    # 基本統計量の計算
    mean = np.mean(heights)
    median = np.median(heights)
    std = np.std(heights)
    # 最頻値の計算
    mode_result = stats.mode(heights)
    mode = mode_result.mode

    # 結果の表示
    print("身長データの分析結果:")
    print(f"平均値：{mean:.1f}cm")
    print(f"中央値：{median:.1f}cm")
    print(f"最頻値：{mode}cm")
    print(f"標準偏差：{std:.1f}cm")

    # ヒストグラムと正規分布
    plt.figure(figsize=(10, 6))
    plt.hist(heights, bins=10, density=True, alpha=0.7, label="実データ")

    # 正規分布曲線
    x = np.linspace(min(heights), max(heights), 100)
    y = stats.norm.pdf(x, mean, std)
    plt.plot(x, y, "r-", label="正規分布")

    plt.title("クラスの身長分布")
    plt.xlabel("身長 (cm)")
    plt.ylabel("頻度")
    plt.legend()
    plt.grid(True)
    plt.show()


analyze_height_data()


"""勉強時間とテスト点数のデータで散布図を描き、相関係数や回帰直線を求めて関係を考える"""
from sklearn.linear_model import LinearRegression


def analyze_study_data():
    # 1 週間の勉強時間 （時間） とテスト点数のデータ
    study_hours = np.array([1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 2.0, 2.5, 3.0, 3.5, 4.0, 3.0, 3.5]).reshape(-1, 1)
    test_scores = np.array([65, 70, 75, 80, 85, 90, 95, 68, 72, 78, 82, 88, 77, 83])

    # 相関係数の計算
    correlation = np.corrcoef(study_hours.flatten(), test_scores)[0, 1]
    print(f"相関係数：{correlation:.3f}")

    # 回帰分析
    model = LinearRegression()
    model.fit(study_hours, test_scores)

    # 回帰直線の係数
    slope = model.coef_[0]
    intercept = model.intercept_
    print(f"\n回帰直線: y = {slope:.1f}x + {intercept:.1f}")
    print(f"傾き：{slope:.1f}（1時間勉強時間が増えると点数が{slope:.1f}点上がる）")

    # 予測例
    study_time = 5.0
    predicted_score = model.predict([[study_time]])[0]
    print(f"\n{study_time}時間勉強した場合の予測点数：{predicted_score:.1f}点")

    # グラフの作成
    plt.figure(figsize=(10, 6))

    # 散布図
    plt.scatter(study_hours, test_scores, color="blue", label="実データ", alpha=0.7)

    # 回帰直線
    x_range = np.linspace(1, 5, 100).reshape(-1, 1)
    y_pred = model.predict(x_range)
    plt.plot(x_range, y_pred, "r--", label=f"回帰直線 (相関係数: {correlation:.3f})")

    # グラフの装飾
    plt.title("勉強時間とテスト点数の関係")
    plt.xlabel("勉強時間（時間）")
    plt.ylabel("テスト点数")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()


analyze_study_data()
