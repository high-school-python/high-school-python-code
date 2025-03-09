"""入力ミスがあっても止まらず再入力を促す計算プログラム"""


def get_number(prompt: str) -> int:
    """数値を安全に入力させる関数."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("数字を入力してください")


def safe_calculator() -> None:
    """エラーに強い電卓プログラム."""
    while True:
        try:
            # 数値の入力
            num1 = get_number("1つ目の数字を入力：")
            num2 = get_number("2つ目の数字を入力：")

            # 演算子の入力
            operator = input("演算子を入力（+, -, *, /）：")

            # 計算実行
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("0での割り算はできません")
                    continue
                result = num1 / num2
            else:
                print("無効な演算子です")
                continue

            # 結果表示
            print(f"結果：{result}")

            # 継続確認
            if input("続けますか？(y/n)：") != "y":
                break

        except Exception as e:
            print(f"エラーが発生しました：{e}")
            print("もう一度試してください")


safe_calculator()


"""存在しないファイルを開こうとしたときにエラーを回避するプログラム"""


class VirtualFileSystem:
    """仮想ファイルシステムクラス."""

    def __init__(self) -> None:
        # 仮想ファイルディレクトリ
        self.files = {
            "sample.txt": "これはサンプルファイルです。\n複数行のテキストを含んでいます。\nPythonプログラミングは楽しいですね。",
            "data.csv": "名前,年齢,職業\n田中,25,エンジニア\n佐藤,30,デザイナー\n鈴木,28,マーケター",
            "secret.txt": "このファイルはアクセス権限が必要です。",
        }

        # ファイルのアクセス権限 （True ならアクセス可能）
        self.permissions = {"sample.txt": True, "data.csv": True, "secret.txt": False}

    def list_files(self) -> None:
        """利用可能なファイル一覧を表示."""
        print("利用可能なファイル一覧：")
        for filename in self.files.keys():
            print(f"- {filename}")

    def read_file(self, filename: str) -> str | None:
        """ファイルを安全に読み込む."""
        try:
            if filename not in self.files:
                raise FileNotFoundError(f"ファイル '{filename}' が見つかりません")

            return self.files[filename]

        except FileNotFoundError as e:
            print(str(e))
            return None
        except Exception as e:
            print(f"予期せぬエラーが発生しました：{e}")
            return None


def process_file() -> None:
    """ファイル処理プログラム."""
    # 仮想ファイルシステムの初期化
    vfs = VirtualFileSystem()

    while True:
        print("\n")
        vfs.list_files()
        filename = input("\n処理するファイル名を入力してください：")

        # ファイルの読み込み
        content = vfs.read_file(filename)

        if content is not None:
            # ファイルの内容を処理
            print("\nファイルの内容:")
            print(content)

        # 継続確認
        if input("\n他のファイルを処理しますか？(y/n)：") != "y":
            break


process_file()
