"""枠のEnumと変換辞書."""

from enum import StrEnum


class Waku(StrEnum):
    """枠番（1〜8枠）を表すEnum.

    Attributes:
        WAKU1〜WAKU8: 1枠〜8枠
    """

    WAKU1 = "1枠"
    WAKU2 = "2枠"
    WAKU3 = "3枠"
    WAKU4 = "4枠"
    WAKU5 = "5枠"
    WAKU6 = "6枠"
    WAKU7 = "7枠"
    WAKU8 = "8枠"


class WakuClass(StrEnum):
    """枠区分（内枠/中枠/外枠）を表すEnum.

    Attributes:
        INNER: 内枠（1〜3枠）
        MIDDLE: 中枠（4〜5枠）
        OUTER: 外枠（6〜8枠）
    """

    INNER = "内枠"
    MIDDLE = "中枠"
    OUTER = "外枠"


# 枠番（1〜8）→枠Enum
WAKU_NUM_TO_WAKU: dict[int, Waku] = {
    1: Waku.WAKU1,
    2: Waku.WAKU2,
    3: Waku.WAKU3,
    4: Waku.WAKU4,
    5: Waku.WAKU5,
    6: Waku.WAKU6,
    7: Waku.WAKU7,
    8: Waku.WAKU8,
}

# 枠Enum→枠区分
WAKU_TO_WAKU_CLASS: dict[Waku, WakuClass] = {
    Waku.WAKU1: WakuClass.INNER,
    Waku.WAKU2: WakuClass.INNER,
    Waku.WAKU3: WakuClass.INNER,
    Waku.WAKU4: WakuClass.MIDDLE,
    Waku.WAKU5: WakuClass.MIDDLE,
    Waku.WAKU6: WakuClass.OUTER,
    Waku.WAKU7: WakuClass.OUTER,
    Waku.WAKU8: WakuClass.OUTER,
}
