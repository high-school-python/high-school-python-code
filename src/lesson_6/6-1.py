"""関数の基本的な使い方"""


# --- 関数を「作る」部分 （定義） ---
# def 関数名(): の形で、関数を作ります
def greet():
    print("こんにちは！")
    print("元気ですか？")
    print("今日もよろしくお願いします")


# --- 関数を「使う」部分 （呼び出し） ---
# 関数名() で実行します
greet()
print("--- 他の処理 ---")
# 何度でも同じ処理を実行できます
greet()


"""関数の定義を表示してみる"""


def greet():
    print("こんにちは！")
    print("元気ですか？")
    print("今日もよろしくお願いします")


print("--- 関数の定義を表示 ---")
# () を付けないと呼び出されません
# 関数の定義を表示すると、関数の名前と、その関数がどこにあるかを示すアドレスが表示されます
print(greet)  # <function greet at 0x7b70b00c7100>

print("--- 関数の返す値を表示 ---")
# この関数は、値を返していないので、 print すると None になります
print(greet())  # None
