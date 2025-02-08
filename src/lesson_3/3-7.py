"""年齢に応じたメッセージ"""

age = int(input("年齢を入力してください："))

if age < 0:
    print("エラー：正しい年齢を入力してください")
elif age < 13:
    print("子供料金：600円です")
elif age < 65:
    print("大人料金：1200円です")
else:
    print("シニア料金：800円です")


"""パスワードの安全性チェック"""
password = input("パスワードを入力してください：")

if len(password) < 8:
    print("パスワードが短すぎます")
    print("8文字以上にしてください")
elif password.isdigit():
    print("数字だけのパスワードは危険です")
    print("文字も混ぜてください")
elif password.isalpha():
    print("文字だけのパスワードは危険です")
    print("数字も混ぜてください")
else:
    print("パスワードOK!")
