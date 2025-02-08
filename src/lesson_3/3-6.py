"""部活動の練習場所"""

day = "月曜日"
weather = "雨"

if day == "月曜日":
    if weather == "晴れ":
        print("グラウンドで練習です")
    else:
        print("体育館で練習です")
else:
    print("今日は部活動はありません")


"""商品の購入判断"""
price = 1200  # 商品の値段
money = 1000  # 持っているお金
discount = True  # 割引クーポンを持っている

if money >= price:
    print("購入できます")
    print(f"残金：{money - price}円")
else:
    if discount:
        # 20% オフ
        discounted_price = price * 0.8

        if money >= discounted_price:
            print("割引価格なら購入できます")
            print(f"割引後価格：{discounted_price}円")
            print(f"残金：{money - discounted_price}円")
        else:
            print("割引されても予算オーバーです")
            print(f"あと{discounted_price - money}円必要です")
    else:
        print("予算が足りません")
        print(f"あと{price - money}円必要です")
