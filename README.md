# high-school-python-code

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

- [`ハイスクールPython`](https://high-school-python.jp) で使用されているソースコードをまとめたものです
- [GitHub Repository](https://github.com/high-school-python/high-school-python-code)

`ハイスクールPython` で使用されているソースコードをまとめたものです。

## ディレクトリ構成

このようなディレクトリ構成になっています

```sh
high-school-python-code/  # このリポジトリのルートディレクトリ
├── .vscode/              # VSCode の設定ファイル
├── colab/                # Google Colab 用の Jupyter Notebook ファイル
│   ├── lesson_1.ipynb    # レッスン 1 のソースコード
│   ├── lesson_2.ipynb    # レッスン 2 のソースコード
│   └── ...
└── src/                  # ソースコード (uv 環境で実行可能)
    ├── lesson_1/         # レッスン 1 のソースコード
    │   ├── 1.py
    │   ├── 2.py
    │   └── ...
    ├── lesson_2/         # レッスン 2 のソースコード
    ├── lesson_3/         # レッスン 3 のソースコード
    ├── ...
    └── hello.py          # サンプルスクリプト
```

### その他のファイル

- `.gitignore`: このリポジトリで無視するファイルを指定するファイル
- `.python-version`: Python のバージョンを指定するファイル (3.13)
- `LICENSE`: このリポジトリのライセンス (MIT ライセンス)
- `pyproject.toml`: uv の設定ファイル
- `README.md`: このファイル (説明書)
- `uv.lock`: uv でインストールしたパッケージのバージョンを固定するためのファイル (依存関係の解決)

## 開発環境の構築

### 1. uv のインストール

このリポジトリでは、パッケージ管理に [uv](https://docs.astral.sh/uv/) を使用しています。まずはこちらの内容に従って、PC に uv をインストールしてください。

```sh
# Windows の場合
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Mac の場合
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. パッケージのインストール

以下のコマンドを実行してください。すると、`pyproject.toml` に記載されているパッケージがインストールされます。仮想環境は、`.venv/` に作成されます。

```sh
uv sync
```

パッケージを追加する場合は、以下のように `uv add` コマンドを使用してください。

```sh
# requests を追加
uv add requests

# 開発環境のみに追加
uv add --dev types-requests

# アップデート
uv add --upgrade requests
```

## 3. スクリプトの実行

以下のように、`uv run` コマンドを使用して、スクリプトを実行できます。

```sh
uv run src/hello.py
```
