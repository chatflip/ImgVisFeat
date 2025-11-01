# CLAUDE.md

このファイルは、このリポジトリのコードを扱う際にClaude Code (claude.ai/code) へのガイダンスを提供します。

## プロジェクト概要

ImgVisFeatは、画像の可視化と特徴抽出のためのPythonライブラリです。カラーチャンネル、勾配、HoG、LBP、キーポイント（SIFT、AKAZE、ORB）、パワースペクトラム解析を含む、画像特徴を分析するための様々な可視化ツールを提供します。

## 開発コマンド

### Makeターゲット（推奨）

プロジェクトはMakefileを提供しており、一般的な開発タスクを簡単に実行できます：

```bash
# 利用可能なターゲットを表示
make help

# コードをフォーマット（ruff + mdformat）
make format

# リントチェックを実行（ruff + mypy）
make lint

# テストを実行（pytest + カバレッジ）
make test

# ドキュメントをビルド
make builddocs

# ドキュメントのビルド成果物を削除
make cleandocs
```

### パッケージ管理

プロジェクトは依存関係管理に[uv](https://docs.astral.sh/uv/)を使用しています：

```bash
# 依存関係のインストール（全ての依存グループを含む）
uv sync

# 本番依存関係のみインストール
uv sync --no-dev

# 新しい依存関係の追加
uv add <package>

# 開発用依存関係の追加
uv add --dev <package>

# パッケージの削除
uv remove <package>

# 依存関係のリストを表示
uv pip list
```

### テスト

```bash
# Makeを使用（推奨）
make test

# または直接uvを使用
uv run pytest tests/ --cov=./ --cov-report=xml

# 単一のテストファイルを実行
uv run pytest tests/test_<name>.py

# 特定のテストを実行
uv run pytest tests/test_<name>.py::test_function_name

# 注意：カバレッジは100%に到達する必要があります（pyproject.tomlでfail_under = 100）
```

### リンティングとフォーマット

```bash
# Makeを使用（推奨）
make lint      # リントチェック
make format    # フォーマット修正

# または直接uvを使用
uv run ruff check .              # リンターを実行
uv run ruff check --fix .        # 自動修正付き
uv run ruff format .             # コードをフォーマット
uv run mypy .                    # 型チェック
uv run mdformat README.md        # Markdownをフォーマット

# pre-commitフックを手動で実行
uv run pre-commit run --all-files
```

### ビルドと公開

```bash
# パッケージをビルド
uv build

# PyPIに公開
uv publish

# TestPyPIに公開
uv publish --publish-url https://test.pypi.org/legacy/
```

### ドキュメントビルド

```bash
# Makeを使用（推奨）
make builddocs   # ドキュメントをビルド
make cleandocs   # ビルド成果物を削除

# または直接uvを使用
uv run sphinx-build docs _build
```

### CLIツール

パッケージは`ivf`というCLIコマンドを提供します：

```bash
# 可視化CLIを実行
uv run ivf path/to/image.jpg

# またはインストール後
ivf path/to/image.jpg --method all
```

## コードアーキテクチャ

### Visualizerパターン

すべての可視化ツールは、`AbstractVisualizer.py`で定義された抽象基底クラスパターンに従います：

- **AbstractVisualizer**: `NDArray[np.uint8]`を受け取り`VisualizationResult`を返す抽象`__call__`メソッドを持つ基底クラス
- 各可視化ツールは、特定の可視化を実行するために`__call__`メソッドを実装します
- 結果は`type.py`で定義された型付きデータクラスとして返されます

### Visualizer階層

```text
AbstractVisualizer (抽象基底)
├── ColorChannelVisualizer → ColorChannelResult
├── GradientVisualizer (勾配タイプの基底)
│   ├── ColorGradientVisualizer → GradientResult
│   └── GrayGradientVisualizer → GradientResult
├── HoGVisualizer → HogResult
├── LBPVisualizer → LBPResult
├── KeypointVisualizer → KeypointResult
│   ("SIFT"、"AKAZE"、"ORB"アルゴリズムをサポート)
└── PowerSpectrumVisualizer → PowerSpectrumResult
```

### メインVisualizerクラス

`Visualizer.py`は以下を行う高レベルインターフェースを提供します：

- 利用可能なすべての可視化ツールをインスタンス化
- 入力画像にすべての可視化を適用
- 入力画像名に基づいたディレクトリに結果を保存
- OpenCVウィンドウで結果を表示

### 結果タイプ

すべての可視化結果は`VisualizationResult`基底クラスを継承し、`type.py`でデータクラスとして定義されています：

- `ColorChannelResult`: blue、green、redチャンネル
- `GradientResult`: gradient_x、gradient_y、gradient_xy
- `HogResult`: hog可視化
- `LBPResult`: lbp可視化
- `KeypointResult`: keypoint、rich_keypoint
- `PowerSpectrumResult`: power_spectrum

### テスト構造

- テストは`conftest.py`で定義されたフィクスチャを持つpytestを使用
- `tests/utils.py`に共通テストユーティリティ
- 各可視化ツールには対応するテストファイルがあります（例：`test_HoGVisualizer.py`）
- テスト画像は`get_image()`ユーティリティを使用してプログラム的に生成されます

## コードスタイル

### ドキュメント

- Googleスタイルのdocstringを使用（ruff.tomlで設定）
- モジュールレベルのdocstringが必要（ただしD100は無視）
- すべてのパブリッククラスとメソッドは文書化する必要があります

### フォーマット

- 行の長さ：88文字（Black互換）
- Ruffが強制：pycodestyle (E, W)、Pyflakes (F)、isort (I)、pydocstyle (D)、McCabe (C)
- Pythonターゲットバージョン：3.10

### 型ヒント

- すべての関数シグネチャには型ヒントを含める必要があります
- 配列タイプには`numpy.typing.NDArray`を使用
- Mypyの厳密チェックが有効

### Pre-commitフック

プロジェクトはpre-commitを使用：

- `ruff check --fix`: リンティング問題を自動修正
- `ruff format`: コードを自動フォーマット

## 主要な制約

- **テストカバレッジ**: 100%のテストカバレッジを維持する必要があります
- **Pythonバージョン**: Python 3.10+をサポート（pyproject.tomlに記載）
- **画像タイプ**: すべての画像入力は`NDArray[np.uint8]`である必要があります
- **ビルドシステム**: uvをビルドバックエンドとして使用（uv_build）

## CLIエントリポイント

CLIは`cli.py`で定義され、エントリポイントは`ivf`です（pyproject.tomlで設定）：

- 必須引数として画像パスを受け取ります
- オプションの`--method`フラグ（現在可視化ツールでは完全に実装されていません）
- エラー時は終了コード1、成功時は0で終了します
