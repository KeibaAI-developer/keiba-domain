"""枠に関するEnum・定数のテスト."""

import pytest

from keiba_domain import WAKU_NUM_TO_WAKU, WAKU_TO_WAKU_CLASS, Waku, WakuClass


# 正常系
@pytest.mark.parametrize(
    "waku_num, expected",
    [
        (1, Waku.WAKU1),
        (2, Waku.WAKU2),
        (3, Waku.WAKU3),
        (4, Waku.WAKU4),
        (5, Waku.WAKU5),
        (6, Waku.WAKU6),
        (7, Waku.WAKU7),
        (8, Waku.WAKU8),
    ],
)
def test_waku_num_to_waku_contains_all_waku(waku_num: int, expected: Waku) -> None:
    """1〜8の枠番から対応する枠Enumを引ける."""
    assert WAKU_NUM_TO_WAKU[waku_num] == expected


@pytest.mark.parametrize(
    "waku, expected",
    [
        (Waku.WAKU1, WakuClass.INNER),
        (Waku.WAKU2, WakuClass.INNER),
        (Waku.WAKU3, WakuClass.INNER),
        (Waku.WAKU4, WakuClass.MIDDLE),
        (Waku.WAKU5, WakuClass.MIDDLE),
        (Waku.WAKU6, WakuClass.OUTER),
        (Waku.WAKU7, WakuClass.OUTER),
        (Waku.WAKU8, WakuClass.OUTER),
    ],
)
def test_waku_to_waku_class_contains_all_waku(waku: Waku, expected: WakuClass) -> None:
    """全ての枠から対応する枠区分を引ける."""
    assert WAKU_TO_WAKU_CLASS[waku] == expected


def test_waku_num_to_waku_has_eight_entries() -> None:
    """WAKU_NUM_TO_WAKUは1〜8枠の8件を持つ."""
    assert set(WAKU_NUM_TO_WAKU.keys()) == set(range(1, 9))
