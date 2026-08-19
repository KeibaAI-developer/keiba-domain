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

基底例外クラス `KeibaDomainError`、競馬場・馬場状態・距離区分・枠のドメイン定義と判定関数を提供しています。

```python
from keiba_domain import KeibaDomainError

try:
    ...
except KeibaDomainError as e:
    print(f"keiba-domain由来のエラーです: {e}")
```

```python
from keiba_domain import (
    WAKU_TO_WAKU_CLASS,
    ChakudosuKyoriKubun,
    DistanceClass,
    Waku,
    judge_chakudosu_kyori_kubun,
    judge_distance_class,
)

# 学習用の距離区分（境界: 短距離≤1400 / マイル<1800 / 中距離≤2200 / 中長距離≤2600 / 長距離）
distance_class = judge_distance_class(2000)
assert distance_class == DistanceClass.MIDDLE

# JV-VAN出走別着度数の距離区分（学習用のDistanceClassとは境界が異なる別概念）
kyori_kubun = judge_chakudosu_kyori_kubun(2000)
assert kyori_kubun == ChakudosuKyoriKubun.FROM_1801_TO_2000

# 枠区分（内枠/中枠/外枠）
waku_class = WAKU_TO_WAKU_CLASS[Waku.WAKU1]
```

今後、芝ダ・内外・回り・コースの大小といったドメイン定義や判定関数がモジュールとして追加されていきます。


## エラーハンドリング

本ライブラリが送出する例外は全て`KeibaDomainError`を基底クラスとしています：

| 例外クラス | 説明 |
|---|---|
| `KeibaDomainError` | 基底例外クラス |

