"""在庫管理シミュレーションの可視化"""

import matplotlib.pyplot as plt
import numpy as np


def visualize_inventory_simulation(
    reorder_thresholds: list[int] = [5, 10, 15],
    reorder_amounts: list[int] = [5, 10, 15],
) -> None:
    """在庫管理シミュレーションの可視化.

    Args:
        reorder_thresholds (list[int]): 試す発注しきい値のリスト
        reorder_amounts (list[int]): 試す発注数のリスト
    """
    fig, axes = plt.subplots(len(reorder_thresholds), len(reorder_amounts), figsize=(15, 10))

    stockout_results = np.zeros((len(reorder_thresholds), len(reorder_amounts)))

    for i, threshold in enumerate(reorder_thresholds):
        for j, amount in enumerate(reorder_amounts):
            # 先ほど定義した関数を使用
            stock_history, pending_history, stockout_days = simulate_inventory(
                days=30, initial_stock=10, reorder_threshold=threshold, reorder_amount=amount, lead_time=3
            )

            ax = axes[i, j]
            days = range(31)  # 0 日目を含む

            ax.plot(days, stock_history, "b-", label="在庫数")
            ax.set_title(f"しきい値={threshold}, 発注数={amount}\n品切れ={stockout_days}日")
            ax.set_ylim(0, max(max(stock_history) + 2, 20))
            ax.grid(True)

            if i == len(reorder_thresholds) - 1:
                ax.set_xlabel("日数")
            if j == 0:
                ax.set_ylabel("在庫数")

            stockout_results[i, j] = stockout_days

    plt.tight_layout()
    plt.show()


visualize_inventory_simulation()
