# ijo_kubun.py

異常区分を表すEnum・異常区分コードとの対応表・判定関数を提供する。

## `IjoKubun`

異常区分を表すEnum。

| 属性 | 型 | 値 | 説明 |
|---|---|---|---|
| `SHUSSO_TORIKESHI` | `str` | `"出走取消"` | 出走取消 |
| `HASSO_JOGAI` | `str` | `"発走除外"` | 発走除外 |
| `KYOSO_JOGAI` | `str` | `"競走除外"` | 競走除外 |
| `KYOSO_CHUSHI` | `str` | `"競走中止"` | 競走中止 |
| `SHIKKAKU` | `str` | `"失格"` | 失格 |
| `RAKUBA_SAIKIJO` | `str` | `"落馬再騎乗"` | 落馬再騎乗 |
| `KOCHAKU` | `str` | `"降着"` | 降着 |

---

## `IJO_KUBUN_CODE_TO_NAME`

異常区分コード（"1"〜"7"）→異常区分のマッピング。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `str` | `"1"` | `IjoKubun` | `IjoKubun.SHUSSO_TORIKESHI` | 出走取消 |
| `str` | `"2"` | `IjoKubun` | `IjoKubun.HASSO_JOGAI` | 発走除外 |
| `str` | `"3"` | `IjoKubun` | `IjoKubun.KYOSO_JOGAI` | 競走除外 |
| `str` | `"4"` | `IjoKubun` | `IjoKubun.KYOSO_CHUSHI` | 競走中止 |
| `str` | `"5"` | `IjoKubun` | `IjoKubun.SHIKKAKU` | 失格 |
| `str` | `"6"` | `IjoKubun` | `IjoKubun.RAKUBA_SAIKIJO` | 落馬再騎乗 |
| `str` | `"7"` | `IjoKubun` | `IjoKubun.KOCHAKU` | 降着 |

---

## `NOT_STARTED_IJO_KUBUN_CODES`

出走しなかった馬の異常区分コードの集合。

| 型 | 値 | 説明 |
|---|---|---|
| `frozenset[str]` | `{"1", "2", "3"}` | 出走取消・発走除外・競走除外 |

---

## `NOT_FINISHED_IJO_KUBUN_CODES`

完走しなかった馬の異常区分コードの集合。

| 型 | 値 | 説明 |
|---|---|---|
| `frozenset[str]` | `{"1", "2", "3", "4"}` | 出走しなかった馬（出走取消・発走除外・競走除外）と競走中止 |

失格（`"5"`）は含めない。
走り切った上で着順を取り消される区分であるためである。

---

## `ijo_kubun_from_code()`

### 概要

異常区分コードから異常区分を取得する。

### 引数

| 引数 | 型 | デフォルト値 | 説明 |
|---|---|---|---|
| `code` | `str` | - | 異常区分コード（`"0"`〜`"7"`） |

### 返り値

| 型 | 説明 |
|---|---|
| `IjoKubun \| None` | 異常区分。`code` が `"0"`（異常なし）の場合は `None` |

### 例外

| 例外 | 条件 |
|---|---|
| `KeibaDomainError` | `code` が `"0"`〜`"7"` のいずれでもない場合 |
