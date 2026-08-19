"""距離区分のEnumと判定関数.

学習用の距離区分（DistanceClass）とJV-VAN出走別着度数の距離区分（ChakudosuKyoriKubun）の
2種類のEnum・判定関数を提供する。両者は境界が異なる別概念のため型を分けている。
"""

from enum import StrEnum


class DistanceClass(StrEnum):
    """学習用の距離区分を表すEnum.

    Attributes:
        SHORT: 短距離（1400m以下）
        MILE: マイル（1400m超1800m未満）
        MIDDLE: 中距離（1800m以上2200m以下）
        LONG_MIDDLE: 中長距離（2200m超2600m以下）
        LONG: 長距離（2600m超）
    """

    SHORT = "短距離"
    MILE = "マイル"
    MIDDLE = "中距離"
    LONG_MIDDLE = "中長距離"
    LONG = "長距離"


class ChakudosuKyoriKubun(StrEnum):
    """JV-VAN出走別着度数の距離区分を表すEnum.

    Attributes:
        UNDER_1200: 1200m以下
        FROM_1201_TO_1400: 1201m〜1400m
        FROM_1401_TO_1600: 1401m〜1600m
        FROM_1601_TO_1800: 1601m〜1800m
        FROM_1801_TO_2000: 1801m〜2000m
        FROM_2001_TO_2200: 2001m〜2200m
        FROM_2201_TO_2400: 2201m〜2400m
        FROM_2401_TO_2800: 2401m〜2800m
        OVER_2801: 2801m以上
    """

    UNDER_1200 = "1200以下"
    FROM_1201_TO_1400 = "1201-1400"
    FROM_1401_TO_1600 = "1401-1600"
    FROM_1601_TO_1800 = "1601-1800"
    FROM_1801_TO_2000 = "1801-2000"
    FROM_2001_TO_2200 = "2001-2200"
    FROM_2201_TO_2400 = "2201-2400"
    FROM_2401_TO_2800 = "2401-2800"
    OVER_2801 = "2801以上"


def judge_distance_class(distance: int) -> DistanceClass:
    """距離から学習用の距離区分を判定する.

    Args:
        distance (int): 距離（メートル）

    Returns:
        DistanceClass: 距離区分（短距離 ≤1400 / マイル <1800 / 中距離 ≤2200 /
            中長距離 ≤2600 / 長距離）
    """
    if distance <= 1400:
        return DistanceClass.SHORT
    if distance < 1800:
        return DistanceClass.MILE
    if distance <= 2200:
        return DistanceClass.MIDDLE
    if distance <= 2600:
        return DistanceClass.LONG_MIDDLE
    return DistanceClass.LONG


# 距離の昇順に並んだ (上限距離, 区分) のペア。すべての上限を超えた場合はOVER_2801とする
_KYORI_KUBUN_BOUNDARIES: list[tuple[int, ChakudosuKyoriKubun]] = [
    (1200, ChakudosuKyoriKubun.UNDER_1200),
    (1400, ChakudosuKyoriKubun.FROM_1201_TO_1400),
    (1600, ChakudosuKyoriKubun.FROM_1401_TO_1600),
    (1800, ChakudosuKyoriKubun.FROM_1601_TO_1800),
    (2000, ChakudosuKyoriKubun.FROM_1801_TO_2000),
    (2200, ChakudosuKyoriKubun.FROM_2001_TO_2200),
    (2400, ChakudosuKyoriKubun.FROM_2201_TO_2400),
    (2800, ChakudosuKyoriKubun.FROM_2401_TO_2800),
]


def judge_chakudosu_kyori_kubun(distance: int) -> ChakudosuKyoriKubun:
    """距離からJV-VAN出走別着度数の距離区分を判定する.

    Args:
        distance (int): 距離（メートル）

    Returns:
        ChakudosuKyoriKubun: 距離区分。境界値以下の区分を採用し、
            2800mを超える場合は"2801以上"とする
    """
    for boundary, kubun in _KYORI_KUBUN_BOUNDARIES:
        if distance <= boundary:
            return kubun
    return ChakudosuKyoriKubun.OVER_2801
