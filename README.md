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


## 公開API

`keiba_domain/__init__.py` の `__all__` に含まれる公開APIの一覧です。モジュールごとにまとめています。

### `exceptions`（基底例外）

| 種別 | 名前 | 用途 |
|---|---|---|
| 例外 | `KeibaDomainError` | 本ライブラリが送出する全例外の基底クラス |

### `keibajo`（競馬場）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `Keibajo` | 中央競馬場（札幌〜小倉の10場）を表す |
| 定数 | `KEIBAJO_CODE_TO_NAME` | 競馬場コード→`Keibajo`（中央10場のみ） |
| 定数 | `CENTRAL_KEIBAJO_CODES` | 中央競馬場のコード集合 |
| 定数 | `KEIBAJO_CODE_TO_LOCAL_NAME` | 競馬場コード→名称（地方・中央すべて） |
| 定数 | `KEIBAJO_TO_CODE` | `Keibajo`→競馬場コード |
| 関数 | `keibajo_from_code` | 競馬場コードから`Keibajo`を取得（中央10場以外は例外） |
| 関数 | `keibajo_from_name` | 競馬場名から`Keibajo`を取得（中央10場以外は例外） |
| 関数 | `is_central_keibajo` | 中央競馬場のコードかどうかを判定（例外を送出しない） |

### `baba`（馬場状態）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `Baba` | 馬場状態（良・稍・重・不）を表す |
| 定数 | `BABA_CODE_TO_NAME` | 馬場状態コード（"1"〜"4"）→`Baba` |
| 関数 | `baba_from_code` | 馬場状態コードから`Baba`を取得（"0"は`None`、範囲外は例外） |

### `distance`（距離区分）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `DistanceClass` | 学習用の距離区分（短距離〜長距離） |
| Enum | `ChakudosuKyoriKubun` | JV-VAN出走別着度数の距離区分 |
| 関数 | `judge_distance_class` | 距離から学習用の距離区分を判定 |
| 関数 | `judge_chakudosu_kyori_kubun` | 距離からJV-VAN出走別着度数の距離区分を判定 |

### `waku`（枠）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `Waku` | 枠番（1枠〜8枠）を表す |
| Enum | `WakuClass` | 枠区分（内枠/中枠/外枠）を表す |
| 定数 | `WAKU_NUM_TO_WAKU` | 枠番（int）→`Waku` |
| 定数 | `WAKU_TO_WAKU_CLASS` | `Waku`→枠区分 |

### `course`（コース: 芝ダ・内外・回り・コースの大小・コースキー）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `TurfDirt` | 芝・ダートの区別を表す |
| Enum | `RaceShubetsu` | レース種別（平地/障害）を表す |
| Enum | `Inout` | 内外（内/外/内-外/外-内）を表す |
| Enum | `Direction` | コースの左右方向（左回り/右回り/直線）を表す |
| Enum | `TrackSize` | コースの大小区分（大箱/小回り）を表す |
| 定数 | `MIGI_KEIBAJO` | 右回りの競馬場集合 |
| 定数 | `HIDARI_KEIBAJO` | 左回りの競馬場集合 |
| 定数 | `INOUT_REQUIRED_COURSES` | 内外の区別が必要なコース集合 |
| 定数 | `COURSE_TRACK_SIZE` | コースキー→コースの大小（直線コースは未定義） |
| 関数 | `parse_turf_dirt` | 文字列から芝ダを判定（平地障害は判定しない） |
| 関数 | `parse_inout` | 文字列から内外を判定 |
| 関数 | `judge_direction` | 競馬場・芝ダ・距離から回りを判定 |
| 関数 | `is_straight_course` | 直線コースかどうかを判定 |
| 関数 | `get_course_key_inout` | コースキー用の内外サフィックスを取得 |
| 関数 | `build_course_key` | コースキーを構築（例: "東京芝2000", "京都芝1600外"） |
| 関数 | `get_track_size` | コースキーからコースの大小を取得 |

### `race_code`（レースコード）

| 種別 | 名前 | 用途 |
|---|---|---|
| 定数 | `RACE_CODE_LENGTH` | レースコードの桁数（16） |
| 関数 | `validate_race_code` | レースコードが半角数字16桁であることを検証（不正な形式は例外） |
| 関数 | `extract_race_code_parts` | レースコードを年・月日・競馬場コード・回・日目・Rに分解 |

### `track_code`（トラックコード）

| 種別 | 名前 | 用途 |
|---|---|---|
| 定数 | `TRACK_CODE_TO_TURF_DIRT` | トラックコード→`TurfDirt` |
| 定数 | `TRACK_CODE_TO_RACE_SHUBETSU` | トラックコード→`RaceShubetsu` |
| 関数 | `turf_dirt_from_track_code` | トラックコードから`TurfDirt`を取得（"00"は`None`、定義外は例外） |
| 関数 | `race_shubetsu_from_track_code` | トラックコードから`RaceShubetsu`を取得（"00"は`None`、定義外は例外） |
| 関数 | `get_track_codes` | 芝ダとレース種別に該当するトラックコードを昇順で取得 |

### `ijo_kubun`（異常区分）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `IjoKubun` | 異常区分（出走取消〜降着）を表す |
| 定数 | `IJO_KUBUN_CODE_TO_NAME` | 異常区分コード（"1"〜"7"）→`IjoKubun` |
| 定数 | `NOT_STARTED_IJO_KUBUN_CODES` | 出走しなかった馬の異常区分コード集合 |
| 定数 | `NOT_FINISHED_IJO_KUBUN_CODES` | 完走しなかった馬の異常区分コード集合 |
| 関数 | `ijo_kubun_from_code` | 異常区分コードから`IjoKubun`を取得（"0"は`None`、範囲外は例外） |

### `grade`（グレード）

| 種別 | 名前 | 用途 |
|---|---|---|
| Enum | `Grade` | グレード（G1〜リステッド）を表す |
| 定数 | `GRADE_CODE_TO_NAME` | グレードコード→`Grade` |
| 関数 | `grade_from_code` | グレードコードから`Grade`を取得（空白と"_"は`None`、定義外は例外） |


## 使い方

基底例外クラス `KeibaDomainError`、競馬場・馬場状態・距離区分・枠・コース・レースコード・トラックコード・異常区分・グレードのドメイン定義と判定関数を提供しています。

```python
from keiba_domain import KeibaDomainError

try:
    ...
except KeibaDomainError as e:
    print(f"keiba-domain由来のエラーです: {e}")
```

```python
from keiba_domain import (
    Baba,
    KeibaDomainError,
    Keibajo,
    baba_from_code,
    is_central_keibajo,
    keibajo_from_code,
)

# 競馬場コードから中央競馬場を取得（中央10場以外は例外）
keibajo = keibajo_from_code("05")
assert keibajo == Keibajo.TOKYO
try:
    keibajo_from_code("42")  # 地方（浦和）のコード
except KeibaDomainError as e:
    print(f"中央競馬場ではありません: {e}")

# 中央競馬場のコードかどうかの判定（地方・未知のコードでも例外を送出せずFalseを返す。
# 過去成績のフィルタリングなど、想定外のコードが1件混ざっても処理全体を止めたくない用途向け）
assert is_central_keibajo("05") is True
assert is_central_keibajo("42") is False
assert is_central_keibajo("99") is False

# 馬場状態コードから馬場状態を取得（"0"は未設定を意味しNoneを返す。範囲外のコードは例外）
assert baba_from_code("1") == Baba.GOOD
assert baba_from_code("0") is None
try:
    baba_from_code("9")
except KeibaDomainError as e:
    print(f"馬場状態コードが不正です: {e}")
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

```python
from keiba_domain import (
    Direction,
    Inout,
    Keibajo,
    TrackSize,
    TurfDirt,
    build_course_key,
    get_track_size,
    is_straight_course,
    judge_direction,
    parse_inout,
    parse_turf_dirt,
)

# 芝ダ・内外の判定（平地か障害かはRaceShubetsuが表す別概念）
turf_dirt = parse_turf_dirt("芝2000m(左 A)")
assert turf_dirt == TurfDirt.TURF
assert parse_turf_dirt("障2880m") is None  # 芝ダの記載がない文字列はNone
inout = parse_inout("右 外 B")
assert inout == Inout.SOTO

# 回りの判定（新潟芝1000mのみ直線コースの例外）
direction = judge_direction(Keibajo.NIIGATA, TurfDirt.TURF, 1000)
assert direction == Direction.STRAIGHT
assert is_straight_course(Keibajo.NIIGATA, TurfDirt.TURF, 1000)

# コースキーの構築（内外区別が必要なコースのみサフィックスが付く。内外マークなしは内扱い）
course_key = build_course_key(Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.SOTO)
assert course_key == "京都芝1600外"

# コースの大小の取得（直線・未定義コースはNone）
track_size = get_track_size("東京芝2000")
assert track_size == TrackSize.BIG
```

```python
from keiba_domain import (
    KEIBAJO_TO_CODE,
    KeibaDomainError,
    Keibajo,
    extract_race_code_parts,
    keibajo_from_name,
    validate_race_code,
)

# 競馬場名から中央競馬場と競馬場コードを取得（中央10場以外は例外）
keibajo = keibajo_from_name("京都")
assert keibajo == Keibajo.KYOTO
assert KEIBAJO_TO_CODE[keibajo] == "08"

# レースコードの検証（半角数字16桁でなければ例外）と分解
validate_race_code("2026111508050411")
parts = extract_race_code_parts("2026111508050411")
assert parts["年"] == "2026"
assert parts["競馬場コード"] == "08"
try:
    validate_race_code("20261115")
except KeibaDomainError as e:
    print(f"レースコードが不正です: {e}")
```

```python
from keiba_domain import (
    NOT_STARTED_IJO_KUBUN_CODES,
    Grade,
    IjoKubun,
    RaceShubetsu,
    TurfDirt,
    get_track_codes,
    grade_from_code,
    ijo_kubun_from_code,
    race_shubetsu_from_track_code,
    turf_dirt_from_track_code,
)

# トラックコードから芝ダとレース種別を取得（"00"は未設定を意味しNoneを返す。定義外のコードは例外）
assert turf_dirt_from_track_code("24") == TurfDirt.DIRT
assert race_shubetsu_from_track_code("52") == RaceShubetsu.SHOGAI
assert turf_dirt_from_track_code("00") is None

# 芝ダとレース種別に該当するトラックコードの取得（絞り込みの条件を組み立てる用途）
assert get_track_codes(TurfDirt.DIRT) == ("23", "24", "25", "26", "27", "28", "29")

# 異常区分コードから異常区分を取得（"0"は異常なしを意味しNoneを返す）
assert ijo_kubun_from_code("4") == IjoKubun.KYOSO_CHUSHI
assert ijo_kubun_from_code("0") is None
assert "1" in NOT_STARTED_IJO_KUBUN_CODES  # 出走取消は出走していない

# グレードコードからグレードを取得（空白と"_"は一般競走を意味しNoneを返す）
assert grade_from_code("A") == Grade.G1
assert grade_from_code(" ") is None
assert grade_from_code("_") is None
```


## エラーハンドリング

本ライブラリが送出する例外は全て`KeibaDomainError`を基底クラスとしています：

| 例外クラス | 説明 |
|---|---|
| `KeibaDomainError` | 基底例外クラス |


## ドキュメント

各モジュールのAPI仕様は [doc/](doc/README.md) を参照してください。
