# keiba-domain

## 概要

`keiba-domain`は、競馬ドメインのマスタ定義と判定処理（競馬場・馬場状態・芝ダ・内外・回り・距離区分・コースの大小・枠など）を集約する最下層ライブラリです。

データ取得層（スクレイピング・DB入出力）と特徴量生成層の双方から参照されることを想定しており、それ自体はDB・外部API・他のKeibaAIライブラリのいずれにも依存しません。競馬ドメインの分類・判定ロジックをこのライブラリに集約することで、各層での定義の重複や不整合を防ぎます。


## 動作要件

- Python 3.12以上


## 依存パッケージ

なし（標準ライブラリのみ）


## インストール

```bash
pip install -e /path/to/keiba-domain
```


## 使い方

現時点では基底例外クラス `KeibaDomainError` のみを提供しています。

```python
from keiba_domain import KeibaDomainError

try:
    ...
except KeibaDomainError as e:
    print(f"keiba-domain由来のエラーです: {e}")
```

今後、競馬場・馬場状態・芝ダ・内外・回り・距離区分・コースの大小・枠といったドメイン定義や判定関数がモジュールとして追加されていきます。


## エラーハンドリング

本ライブラリが送出する例外は全て`KeibaDomainError`を基底クラスとしています：

| 例外クラス | 説明 |
|---|---|
| `KeibaDomainError` | 基底例外クラス |


## ドキュメント

- （ドキュメントへのリンクを記述）
