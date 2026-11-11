# track_code.py

JRA-VANのトラックコードから芝ダ（`TurfDirt`）とレース種別（`RaceShubetsu`）を引く対応表と判定関数を提供する。

## `TRACK_CODE_TO_TURF_DIRT`

トラックコード（2桁）→芝ダのマッピング。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `str` | `"10"`〜`"22"` | `TurfDirt` | `TurfDirt.TURF` | 平地の芝 |
| `str` | `"23"`〜`"29"` | `TurfDirt` | `TurfDirt.DIRT` | 平地のダート（サンドの `"27"`・`"28"` を含む） |
| `str` | `"51"`〜`"59"` | `TurfDirt` | `TurfDirt.TURF` | 障害 |

障害コースの芝ダは芝として扱う。
芝からダートへ移る `"52"` も芝になる。

---

## `TRACK_CODE_TO_RACE_SHUBETSU`

トラックコード（2桁）→レース種別のマッピング。
キーは `TRACK_CODE_TO_TURF_DIRT` と同じ29個である。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `str` | `"10"`〜`"29"` | `RaceShubetsu` | `RaceShubetsu.HEICHI` | 平地 |
| `str` | `"51"`〜`"59"` | `RaceShubetsu` | `RaceShubetsu.SHOGAI` | 障害 |

---

## `turf_dirt_from_track_code()`

### 概要

トラックコードから芝ダを取得する。

### 引数

| 引数 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `code` | `str` | - | トラックコード（例: `"17"`） |

### 返り値

| 型 | 説明 |
|---|---|
| `TurfDirt \| None` | 芝ダ。`code` が `"00"`（未設定）の場合は `None` |

### 例外

| 例外 | 条件 |
|---|---|
| `KeibaDomainError` | `code` が `"00"` でも定義済みのトラックコードでもない場合 |

---

## `race_shubetsu_from_track_code()`

### 概要

トラックコードからレース種別（平地・障害）を取得する。

### 引数

| 引数 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `code` | `str` | - | トラックコード（例: `"17"`） |

### 返り値

| 型 | 説明 |
|---|---|
| `RaceShubetsu \| None` | レース種別。`code` が `"00"`（未設定）の場合は `None` |

### 例外

| 例外 | 条件 |
|---|---|
| `KeibaDomainError` | `code` が `"00"` でも定義済みのトラックコードでもない場合 |

---

## `get_track_codes()`

### 概要

芝ダとレース種別に該当するトラックコードを昇順で取得する。

### 引数

| 引数 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `turf_dirt` | `TurfDirt \| None` | `None` | 芝ダ。`None` の場合は芝ダで絞り込まない |
| `race_shubetsu` | `RaceShubetsu \| None` | `None` | レース種別。`None` の場合はレース種別で絞り込まない |

### 返り値

| 型 | 説明 |
|---|---|
| `tuple[str, ...]` | 該当するトラックコード（昇順）。該当が無い場合は空のタプル |

### 補足

トラックコードで絞り込む条件を組み立てるために使う。

| 呼び出し | 返り値 |
|---|---|
| `get_track_codes(TurfDirt.TURF, RaceShubetsu.HEICHI)` | `"10"`〜`"22"` |
| `get_track_codes(TurfDirt.DIRT)` | `"23"`〜`"29"` |
| `get_track_codes(race_shubetsu=RaceShubetsu.HEICHI)` | `"10"`〜`"29"` |
| `get_track_codes(TurfDirt.TURF)` | `"10"`〜`"22"` と `"51"`〜`"59"` |
