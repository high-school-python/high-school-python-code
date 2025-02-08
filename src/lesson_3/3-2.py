"""合格判定の例"""

score = 65
if score >= 70:
    print("合格です！")
    print("次のステージに進めます")
else:
    print("残念、不合格です")
    print("もう一度チャレンジしましょう")


"""天気予報の例"""
weather = "晴れ"
if weather == "雨":
    print("傘を持っていきましょう")
else:
    print("良い天気です")


"""インデントを揃える"""
if score >= 80:
    print("合格！")  # if ブロックは 4 スペース
else:  # else は if と同じ位置
    print("不合格")  # else ブロックも 4 スペース


"""else は if の直後"""
# 正しい例
if score >= 80:
    print("合格")
else:
    print("不合格")

# 間違った例
if score >= 80:
    print("合格")
# 間に他の処理を入れるとエラー
print("判定終了")
else:  # IndentationError: expected an indented block
    print("不合格")
