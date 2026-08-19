"""距離区分に関するEnum・関数のテスト."""

import pytest

from keiba_domain import (
    ChakudosuKyoriKubun,
    DistanceClass,
    KeibaDomainError,
    judge_chakudosu_kyori_kubun,
    judge_distance_class,
)


# 正常系
@pytest.mark.parametrize(
    "distance, expected",
    [
        # 短距離とマイルの境界（≤1400が短距離）
        (1399, DistanceClass.SHORT),
        (1400, DistanceClass.SHORT),
        (1401, DistanceClass.MILE),
        # マイルと中距離の境界（マイルの上限だけ<1800）
        (1799, DistanceClass.MILE),
        (1800, DistanceClass.MIDDLE),
        # 中距離と中長距離の境界（≤2200が中距離）
        (2199, DistanceClass.MIDDLE),
        (2200, DistanceClass.MIDDLE),
        (2201, DistanceClass.LONG_MIDDLE),
        # 中長距離と長距離の境界（≤2600が中長距離）
        (2599, DistanceClass.LONG_MIDDLE),
        (2600, DistanceClass.LONG_MIDDLE),
        (2601, DistanceClass.LONG),
        # 極端な短距離・長距離
        (1000, DistanceClass.SHORT),
        (3600, DistanceClass.LONG),
    ],
)
def test_judge_distance_class_returns_expected_class(
    distance: int, expected: DistanceClass
) -> None:
    """距離から学習用の距離区分を正しく判定できる."""
    assert judge_distance_class(distance) == expected


@pytest.mark.parametrize(
    "distance, expected",
    [
        # 1200以下の境界
        (1199, ChakudosuKyoriKubun.TO_1200),
        (1200, ChakudosuKyoriKubun.TO_1200),
        (1201, ChakudosuKyoriKubun.FROM_1201_TO_1400),
        # 1201-1400の境界
        (1400, ChakudosuKyoriKubun.FROM_1201_TO_1400),
        (1401, ChakudosuKyoriKubun.FROM_1401_TO_1600),
        # 1401-1600の境界
        (1600, ChakudosuKyoriKubun.FROM_1401_TO_1600),
        (1601, ChakudosuKyoriKubun.FROM_1601_TO_1800),
        # 1601-1800の境界
        (1800, ChakudosuKyoriKubun.FROM_1601_TO_1800),
        (1801, ChakudosuKyoriKubun.FROM_1801_TO_2000),
        # 1801-2000の境界
        (2000, ChakudosuKyoriKubun.FROM_1801_TO_2000),
        (2001, ChakudosuKyoriKubun.FROM_2001_TO_2200),
        # 2001-2200の境界
        (2200, ChakudosuKyoriKubun.FROM_2001_TO_2200),
        (2201, ChakudosuKyoriKubun.FROM_2201_TO_2400),
        # 2201-2400の境界
        (2400, ChakudosuKyoriKubun.FROM_2201_TO_2400),
        (2401, ChakudosuKyoriKubun.FROM_2401_TO_2800),
        # 2401-2800と2801以上の境界
        (2800, ChakudosuKyoriKubun.FROM_2401_TO_2800),
        (2801, ChakudosuKyoriKubun.FROM_2801),
        (3600, ChakudosuKyoriKubun.FROM_2801),
    ],
)
def test_judge_chakudosu_kyori_kubun_returns_expected_kubun(
    distance: int, expected: ChakudosuKyoriKubun
) -> None:
    """距離からJV-VAN出走別着度数の距離区分を正しく判定できる."""
    assert judge_chakudosu_kyori_kubun(distance) == expected


# 準正常系
@pytest.mark.parametrize("distance", [0, -1, -1400])
def test_judge_distance_class_raises_for_non_positive_distance(distance: int) -> None:
    """距離が0以下の場合はKeibaDomainErrorが発生する."""
    with pytest.raises(KeibaDomainError, match="距離が不正です"):
        judge_distance_class(distance)


@pytest.mark.parametrize("distance", [0, -1, -1200])
def test_judge_chakudosu_kyori_kubun_raises_for_non_positive_distance(distance: int) -> None:
    """距離が0以下の場合はKeibaDomainErrorが発生する."""
    with pytest.raises(KeibaDomainError, match="距離が不正です"):
        judge_chakudosu_kyori_kubun(distance)
