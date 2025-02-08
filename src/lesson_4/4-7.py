"""無限ループの例"""

count = 1

# count が 0 より大きい間はループが続く
while count > 0:
    print(count)
    # count が増え続けるので永遠に終わらない
    count += 1


"""安全な例（proper な終了条件）"""
count = 1

# count が 5 まで増えたら終了
while count <= 5:
    print(count)
    count += 1

print("ループが正常に終了しました")


"""条件の間違い: 間違った例"""
total = 0

while total < 100:
    print(total)
    # マイナスになり続けて終わらない
    total -= 10


"""条件の間違い: 正しい例"""
total = 0

while total < 100:
    print(total)
    # 100 に近づく
    total += 10


"""条件の更新忘れ: 間違った例"""
answer = ""

while answer != "exit":
    print("現在実行中...")
    # answer の値を更新し忘れている


"""条件の更新忘れ: 正しい例"""
answer = ""
while answer != "exit":
    print("現在実行中...")
    answer = input("終了するには'exit'と入力：")


"""メニュー選択プログラム"""
while True:
    print("\n=== メニュー ===")
    print("1: 新規作成")
    print("2: 編集")
    print("3: 終了")

    choice = input("選択してください：")

    if choice == "1":
        print("新規作成します")
    elif choice == "2":
        print("編集を開始します")
    elif choice == "3":
        print("プログラムを終了します")
        break  # ここで適切に終了
    else:
        print("正しい選択肢を入力してください")


"""最大試行回数付きのパスワード入力"""
max_attempts = 3
attempts = 0
password = ""

while attempts < max_attempts:
    password = input("パスワードを入力：")
    attempts += 1

    if password == "secret":
        print("ログイン成功！")
        break

    remaining = max_attempts - attempts
    print(f"パスワードが違います。残り{remaining}回")

if attempts >= max_attempts:
    print("ログインに失敗しました")


"""タイムアウトの設定"""
import time

start_time = time.time()
# 10 秒でタイムアウト
timeout = 10

while True:
    current_time = time.time()
    if current_time - start_time > timeout:
        print("タイムアウトしました")
        break

    # 何らかの処理
    print("処理中...")
    # 1 秒待機
    time.sleep(1)
