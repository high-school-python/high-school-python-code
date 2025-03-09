"""基本的な try-except"""

try:
    # エラーが発生するかもしれない処理
    number = int(input("数字を入力してください："))
    print(f"入力された数字は {number} です")
except ValueError:
    # 数値に変換できないときの処理
    print("数字以外が入力されました")


"""複数のエラーを扱う"""
try:
    num1 = int(input("1つ目の数字："))
    num2 = int(input("2つ目の数字："))
    result = num1 / num2
    print(f"結果：{result}")
except ValueError:
    # 数値への変換に失敗した場合
    print("数字を入力してください")
except ZeroDivisionError:
    # 0 で割ろうとした場合
    print("0 で割ることはできません")
except Exception:
    # その他のすべてのエラー
    print("予期せぬエラーが発生しました")


"""else と finally を使った完全な形"""
try:
    number = int(input("数字を入力してください："))
except ValueError:
    print("数字以外が入力されました")
else:
    # エラーが発生しなかった場合に実行される
    print(f"正しく数字 {number} が入力されました")
finally:
    # エラーの有無にかかわらず必ず実行される
    print("処理を終了します")
