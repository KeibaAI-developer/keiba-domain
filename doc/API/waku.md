# waku.py

枠のEnumと変換辞書を提供する。

## `Waku`

枠番（1〜8枠）を表すEnum。

| 属性 | 型 | 値 | 説明 |
|---|---|---|---|
| `WAKU1` | `str` | `"1枠"` | 1枠 |
| `WAKU2` | `str` | `"2枠"` | 2枠 |
| `WAKU3` | `str` | `"3枠"` | 3枠 |
| `WAKU4` | `str` | `"4枠"` | 4枠 |
| `WAKU5` | `str` | `"5枠"` | 5枠 |
| `WAKU6` | `str` | `"6枠"` | 6枠 |
| `WAKU7` | `str` | `"7枠"` | 7枠 |
| `WAKU8` | `str` | `"8枠"` | 8枠 |

---

## `WakuClass`

枠区分（内枠/中枠/外枠）を表すEnum。

| 属性 | 型 | 値 | 説明 |
|---|---|---|---|
| `INNER` | `str` | `"内枠"` | 内枠（1〜3枠） |
| `MIDDLE` | `str` | `"中枠"` | 中枠（4〜5枠） |
| `OUTER` | `str` | `"外枠"` | 外枠（6〜8枠） |

---

## `WAKU_NUM_TO_WAKU`

枠番（1〜8の`int`）→`Waku` Enumのマッピング。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `int` | `1` | `Waku` | `Waku.WAKU1` | 1枠 |
| `int` | `2` | `Waku` | `Waku.WAKU2` | 2枠 |
| `int` | `3` | `Waku` | `Waku.WAKU3` | 3枠 |
| `int` | `4` | `Waku` | `Waku.WAKU4` | 4枠 |
| `int` | `5` | `Waku` | `Waku.WAKU5` | 5枠 |
| `int` | `6` | `Waku` | `Waku.WAKU6` | 6枠 |
| `int` | `7` | `Waku` | `Waku.WAKU7` | 7枠 |
| `int` | `8` | `Waku` | `Waku.WAKU8` | 8枠 |

---

## `WAKU_TO_WAKU_CLASS`

`Waku` Enum→`WakuClass` Enumのマッピング。

| キーの型 | キー | 値の型 | 値 | 説明 |
|---|---|---|---|---|
| `Waku` | `Waku.WAKU1` | `WakuClass` | `WakuClass.INNER` | 内枠 |
| `Waku` | `Waku.WAKU2` | `WakuClass` | `WakuClass.INNER` | 内枠 |
| `Waku` | `Waku.WAKU3` | `WakuClass` | `WakuClass.INNER` | 内枠 |
| `Waku` | `Waku.WAKU4` | `WakuClass` | `WakuClass.MIDDLE` | 中枠 |
| `Waku` | `Waku.WAKU5` | `WakuClass` | `WakuClass.MIDDLE` | 中枠 |
| `Waku` | `Waku.WAKU6` | `WakuClass` | `WakuClass.OUTER` | 外枠 |
| `Waku` | `Waku.WAKU7` | `WakuClass` | `WakuClass.OUTER` | 外枠 |
| `Waku` | `Waku.WAKU8` | `WakuClass` | `WakuClass.OUTER` | 外枠 |
