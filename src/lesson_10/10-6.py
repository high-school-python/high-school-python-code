"""在庫管理シミュレーション"""

import random


def simulate_inventory(
    days: int = 30,
    initial_stock: int = 10,
    reorder_threshold: int = 5,
    reorder_amount: int = 10,
    lead_time: int = 3,
) -> tuple[list[int], list[int], int]:
    """在庫管理シミュレーション.

    Args:
        days (int): シミュレーション日数
        initial_stock (int): 初期在庫数
        reorder_threshold (int): 発注する在庫数のしきい値
        reorder_amount (int): 発注数
        lead_time (int): 発注から到着までの日数

    Returns:
        tuple[list[int], list[int], int]: (在庫履歴, 注文中リスト履歴, 品切れ日数)
    """
    stock = initial_stock
    pending_orders = []  # (到着予定日, 発注数) のリスト
    stock_history = [stock]
    pending_history = [len(pending_orders)]
    stockout_days = 0

    print(f"初期状態: 在庫数 = {stock}, 発注中 = {pending_orders}")

    for day in range(1, days + 1):
        print(f"\n--- 日付: {day} ---")

        # 注文が到着する場合
        new_pending = []
        arrived_orders = []

        for arrival_day, amount in pending_orders:
            if day >= arrival_day:
                stock += amount
                arrived_orders.append((arrival_day, amount))
            else:
                new_pending.append((arrival_day, amount))

        if arrived_orders:
            for arrival_day, amount in arrived_orders:
                print(f"注文到着: {amount}個 (発注日: {arrival_day - lead_time})")

        pending_orders = new_pending

        # 今日の需要
        demand = random.randint(0, 5)
        print(f"本日の需要: {demand}個")

        # 在庫から出荷
        if stock >= demand:
            stock -= demand
            print(f"出荷完了: 残り在庫 = {stock}個")
        else:
            # 在庫不足の場合
            print(f"在庫不足! 要求: {demand}個, 在庫: {stock}個")
            stockout_days += 1
            stock = 0

        # 発注判断
        if stock <= reorder_threshold and not pending_orders:
            pending_orders.append((day + lead_time, reorder_amount))
            print(f"発注実行: {reorder_amount}個 (到着予定日: {day + lead_time})")

        # 履歴を記録
        stock_history.append(stock)
        pending_history.append(len(pending_orders))

        # 現在の状況サマリー
        print(f"日終了時点: 在庫数 = {stock}個, 発注中 = {[(d, a) for d, a in pending_orders]}")

    print("\n--- シミュレーション終了 ---")

    return stock_history, pending_history, stockout_days


# シミュレーションを実行
stock_history, pending_history, stockout_days = simulate_inventory()
print(f"\n30 日間の品切れ日数: {stockout_days}日")
print(f"最終在庫: {stock_history[-1]}個")
print(f"在庫推移: {stock_history}")
print(f"発注中数推移: {pending_history}")
