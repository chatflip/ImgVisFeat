# Development Guidelines

このドキュメントには、このコードベースでの作業に関する重要な情報が含まれています。これらのガイドラインに正確に従ってください。

## プロジェクト概要

ImgVisFeatは、画像の可視化と特徴抽出のためのPythonライブラリです。カラーチャンネル、勾配、HoG、LBP、キーポイント（SIFT、AKAZE、ORB）、パワースペクトラム解析など、画像特徴を分析するための様々な可視化ツールを提供します。

## コア開発ルール

### パッケージ管理

- **uvのみを使用し、pipは使用しない**
- **禁止**: `uv pip install`, `@latest` 構文

```bash
uv sync                    # 依存関係のインストール
uv add <package>          # 依存関係の追加
uv add --dev <package>    # 開発用依存関係の追加
uv remove <package>       # パッケージの削除
```

### コード品質

- すべてのコードに型ヒントが必要
- パブリックAPIにはdocstringが必須
- 関数は焦点を絞り、小さく保つ
- 既存のパターンに正確に従う
- 行の長さ: 最大88文字

### テスト

- フレームワーク: `make test`
- カバレッジ: 80%以上必須
- 新機能にはテストが必要
- バグ修正には回帰テストが必要

## コミットとプルリクエスト

### コミットトレーラー

```bash
git commit --trailer "Reported-by:<name>"        # ユーザー報告の場合
git commit --trailer "Github-Issue:#<number>"    # GitHub issue関連
```

- **絶対に `co-authored-by` やツール名を記載しない**

### プルリクエスト

- 問題とその解決方法に焦点を当てた詳細な説明を作成
- コードの詳細は明確性を高める場合のみ記載

## 開発コマンド

### Makeターゲット

```bash
make help        # 利用可能なターゲットを表示
make format      # フォーマット（ruff + mdformat）
make lint        # リントと型チェック（ruff + ty）
make test        # テスト実行（pytest + カバレッジ）
make builddocs   # ドキュメントをビルド
make cleandocs   # ドキュメント成果物を削除
```

### 直接実行

```bash
# フォーマット・リント
uv run ruff check --fix .
uv run ruff format .
uv run ty check

# テスト
uv run pytest tests/ --cov=./ --cov-report=xml
uv run pytest tests/test_<name>.py                        # 単一テスト
uv run pytest tests/test_<name>.py::test_function_name    # 特定テスト

# Pre-commit
uv run pre-commit run --all-files

# ビルド・公開
uv build
uv publish
uv publish --publish-url https://test.pypi.org/legacy/

# CLI
uv run ivf path/to/image.jpg
```

## エラー解決

### CI失敗時の修正順序

1. フォーマット
2. 型エラー
3. リンティング

### よくある問題

**行の長さ**: 括弧で文字列を分割、関数呼び出しを複数行に、インポートを分割

**型エラー**: Noneチェックを追加、型ナローイング、既存パターンに合わせる

### ベストプラクティス

- コミット前にgit statusを確認
- 型チェックの前にフォーマッタを実行
- 変更を最小限に保つ
- 既存のパターンに従う

## 例外処理

- **`logger.exception()` を使用**（`logger.error()` ではない）
- 例外をメッセージに含めない: `logger.exception("Failed")`

### 特定の例外をキャッチ

```python
except (OSError, PermissionError):        # ファイル操作
except json.JSONDecodeError:              # JSON
except (ConnectionError, TimeoutError):   # ネットワーク
```

### `Exception` を使用する場合

- クラッシュしてはならないトップレベルハンドラー
- クリーンアップブロック（デバッグレベルでログ）

## コードアーキテクチャ

### Visualizerパターン

```text
AbstractVisualizer (抽象基底)
├── ColorChannelVisualizer → ColorChannelResult
├── GradientVisualizer (勾配タイプの基底)
│   ├── ColorGradientVisualizer → GradientResult
│   └── GrayGradientVisualizer → GradientResult
├── HoGVisualizer → HogResult
├── LBPVisualizer → LBPResult
├── KeypointVisualizer → KeypointResult ("SIFT", "AKAZE", "ORB")
└── PowerSpectrumVisualizer → PowerSpectrumResult
```

- **AbstractVisualizer**: `NDArray[np.uint8]`を受け取り`VisualizationResult`を返す
- 各可視化ツールは`__call__`メソッドを実装
- 結果は`type.py`で定義された型付きデータクラス

### メインVisualizerクラス

`Visualizer.py`は高レベルインターフェースを提供：

- すべての可視化ツールをインスタンス化
- 入力画像にすべての可視化を適用
- 結果を保存・表示

### テスト構造

- pytest + `conftest.py`のフィクスチャ
- `tests/utils.py`に共通ユーティリティ
- 各可視化ツールに対応するテストファイル
- テスト画像は`get_image()`でプログラム的に生成

## コードスタイル

- **Docstring**: Googleスタイル（D100は無視）
- **行の長さ**: 88文字（Black互換）
- **型ヒント**: すべての関数シグネチャに必須、配列は`NDArray`を使用
- **Ruff**: pycodestyle (E, W)、Pyflakes (F)、isort (I)、pydocstyle (D)、McCabe (C)
- **Pythonバージョン**: 3.10+

## 主要な制約

- テストカバレッジ: 80%以上（`.coveragerc`）
- Pythonバージョン: 3.10+
- 画像タイプ: `NDArray[np.uint8]`
- ビルドシステム: uv_build
- CLIエントリポイント: `ivf`（`pyproject.toml`で設定）
