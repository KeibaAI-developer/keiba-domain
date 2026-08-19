# keibajo.py

中央競馬場を表すEnum・競馬場コードとの対応表・判定関数を提供する。

## `Keibajo`

中央競馬場（JRAが開催する10場）を表すEnum。

| 属性 | 型 | 値 | 説明 |
|---|---|---|---|
| `SAPPORO` | `str` | `"札幌"` | 札幌 |
| `HAKODATE` | `str` | `"函館"` | 函館 |
| `FUKUSHIMA` | `str` | `"福島"` | 福島 |
| `NIIGATA` | `str` | `"新潟"` | 新潟 |
| `TOKYO` | `str` | `"東京"` | 東京 |
| `NAKAYAMA` | `str` | `"中山"` | 中山 |
| `CHUKYO` | `str` | `"中京"` | 中京 |
| `KYOTO` | `str` | `"京都"` | 京都 |
| `HANSHIN` | `str` | `"阪神"` | 阪神 |
| `KOKURA` | `str` | `"小倉"` | 小倉 |

---

## `KEIBAJO_CODE_TO_NAME`

競馬場コード（2桁）→中央競馬場のマッピング。中央10場のコードのみを含む。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `str` | `"01"` | `Keibajo` | `Keibajo.SAPPORO` | 札幌 |
| `str` | `"02"` | `Keibajo` | `Keibajo.HAKODATE` | 函館 |
| `str` | `"03"` | `Keibajo` | `Keibajo.FUKUSHIMA` | 福島 |
| `str` | `"04"` | `Keibajo` | `Keibajo.NIIGATA` | 新潟 |
| `str` | `"05"` | `Keibajo` | `Keibajo.TOKYO` | 東京 |
| `str` | `"06"` | `Keibajo` | `Keibajo.NAKAYAMA` | 中山 |
| `str` | `"07"` | `Keibajo` | `Keibajo.CHUKYO` | 中京 |
| `str` | `"08"` | `Keibajo` | `Keibajo.KYOTO` | 京都 |
| `str` | `"09"` | `Keibajo` | `Keibajo.HANSHIN` | 阪神 |
| `str` | `"10"` | `Keibajo` | `Keibajo.KOKURA` | 小倉 |

---

## `CENTRAL_KEIBAJO_CODES`

中央競馬場のコード集合（`KEIBAJO_CODE_TO_NAME` のキー集合と一致）。

| 定数名 | 型 | 値 | 説明 |
|---|---|---|---|
| `CENTRAL_KEIBAJO_CODES` | `frozenset[str]` | `{"01", "02", "03", "04", "05", "06", "07", "08", "09", "10"}` | 中央10場の競馬場コード集合 |

---

## `KEIBAJO_CODE_TO_LOCAL_NAME`

競馬場コード→競馬場名のマッピング。中央10場に加えて地方競馬場を含む（海外競馬場は含まない）。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `str` | `"01"`〜`"10"` | `str` | `Keibajo.SAPPORO.value` 〜 `Keibajo.KOKURA.value` | 中央10場（`KEIBAJO_CODE_TO_NAME` と同じ10件） |
| `str` | `"30"` | `str` | `"門別"` | 門別 |
| `str` | `"35"` | `str` | `"盛岡"` | 盛岡 |
| `str` | `"36"` | `str` | `"水沢"` | 水沢 |
| `str` | `"42"` | `str` | `"浦和"` | 浦和 |
| `str` | `"43"` | `str` | `"船橋"` | 船橋 |
| `str` | `"44"` | `str` | `"大井"` | 大井 |
| `str` | `"45"` | `str` | `"川崎"` | 川崎 |
| `str` | `"46"` | `str` | `"金沢"` | 金沢 |
| `str` | `"47"` | `str` | `"笠松"` | 笠松 |
| `str` | `"48"` | `str` | `"名古屋"` | 名古屋 |
| `str` | `"50"` | `str` | `"園田"` | 園田 |
| `str` | `"51"` | `str` | `"姫路"` | 姫路 |
| `str` | `"54"` | `str` | `"高知"` | 高知 |
| `str` | `"55"` | `str` | `"佐賀"` | 佐賀 |
| `str` | `"65"` | `str` | `"帯広"` | 帯広（ばんえい） |

中央10場の値は `Keibajo` Enumインスタンス、地方競馬場の値は素の `str` である点に注意
（辞書の値型としては両者とも `Keibajo | str` に含まれる）。

---

## `keibajo_from_code()`

### 概要

競馬場コードから中央競馬場（`Keibajo`）を取得する。

### 引数

| 引数 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `code` | `str` | - | 競馬場コード（例: `"05"`） |

### 返り値

| 型 | 説明 |
|---|---|
| `Keibajo` | 中央競馬場 |

### 例外

| 例外 | 条件 |
|---|---|
| `KeibaDomainError` | `code` が中央10場のコードでない場合 |

---

## `is_central_keibajo()`

### 概要

競馬場コードが中央競馬場のコードかどうかを判定する。

### 引数

| 引数 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `code` | `str` | - | 競馬場コード |

### 返り値

| 型 | 説明 |
|---|---|
| `bool` | 中央競馬場のコードであれば`True` |

### 補足

`keibajo_from_code` は中央10場以外のコードで `KeibaDomainError` を送出するが、この関数は
地方競馬場のコードはもちろん未知のコードであっても例外を投げず `False` を返す。

これは `keibajo_from_code` がコードの妥当性検証を兼ねる変換関数であるのに対し、
`is_central_keibajo` は「中央競馬場かどうか」を問う述語関数であるため。過去成績データから
中央競馬場のレースだけを抽出するフィルタ用途を想定しており、想定外のコードが1件混ざっただけで
処理全体が例外停止しないよう、意図的に例外を送出しない設計にしている。コードそのものの妥当性を
検証したい場合は `keibajo_from_code` を使うこと。
