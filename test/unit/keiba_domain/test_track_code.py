"""トラックコードに関する定数・関数のテスト."""

import pytest

from keiba_domain import (
    TRACK_CODE_TO_RACE_SHUBETSU,
    TRACK_CODE_TO_TURF_DIRT,
    KeibaDomainError,
    RaceShubetsu,
    TurfDirt,
    get_track_codes,
    race_shubetsu_from_track_code,
    turf_dirt_from_track_code,
)

HEICHI_TURF_CODES = tuple(str(code) for code in range(10, 23))
DIRT_CODES = tuple(str(code) for code in range(23, 30))
SHOGAI_CODES = tuple(str(code) for code in range(51, 60))


# 正常系
@pytest.mark.parametrize(
    "code, expected",
    [
        ("10", TurfDirt.TURF),
        ("22", TurfDirt.TURF),
        ("23", TurfDirt.DIRT),
        ("27", TurfDirt.DIRT),
        ("29", TurfDirt.DIRT),
        ("51", TurfDirt.TURF),
        ("52", TurfDirt.TURF),
        ("59", TurfDirt.TURF),
    ],
)
def test_turf_dirt_from_track_code_returns_turf_dirt(code: str, expected: TurfDirt) -> None:
    """トラックコードから芝ダを取得できる。サンドはダート、障害は芝になる."""
    assert turf_dirt_from_track_code(code) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ("10", RaceShubetsu.HEICHI),
        ("22", RaceShubetsu.HEICHI),
        ("23", RaceShubetsu.HEICHI),
        ("29", RaceShubetsu.HEICHI),
        ("51", RaceShubetsu.SHOGAI),
        ("59", RaceShubetsu.SHOGAI),
    ],
)
def test_race_shubetsu_from_track_code_returns_race_shubetsu(
    code: str, expected: RaceShubetsu
) -> None:
    """トラックコードからレース種別を取得できる."""
    assert race_shubetsu_from_track_code(code) == expected


def test_turf_dirt_from_track_code_with_unset_code_returns_none() -> None:
    """コード"00"（未設定）の場合はNoneを返す."""
    assert turf_dirt_from_track_code("00") is None


def test_race_shubetsu_from_track_code_with_unset_code_returns_none() -> None:
    """コード"00"（未設定）の場合はNoneを返す."""
    assert race_shubetsu_from_track_code("00") is None


def test_track_code_tables_have_same_codes() -> None:
    """芝ダとレース種別の対応表が同じ29個のトラックコードを持つ."""
    expected = set(HEICHI_TURF_CODES + DIRT_CODES + SHOGAI_CODES)
    assert set(TRACK_CODE_TO_TURF_DIRT) == expected
    assert set(TRACK_CODE_TO_RACE_SHUBETSU) == expected


@pytest.mark.parametrize(
    "turf_dirt, race_shubetsu, expected",
    [
        (TurfDirt.TURF, RaceShubetsu.HEICHI, HEICHI_TURF_CODES),
        (TurfDirt.DIRT, RaceShubetsu.HEICHI, DIRT_CODES),
        (TurfDirt.TURF, RaceShubetsu.SHOGAI, SHOGAI_CODES),
        (TurfDirt.DIRT, RaceShubetsu.SHOGAI, ()),
        (TurfDirt.TURF, None, HEICHI_TURF_CODES + SHOGAI_CODES),
        (TurfDirt.DIRT, None, DIRT_CODES),
        (None, RaceShubetsu.HEICHI, HEICHI_TURF_CODES + DIRT_CODES),
        (None, RaceShubetsu.SHOGAI, SHOGAI_CODES),
        (None, None, HEICHI_TURF_CODES + DIRT_CODES + SHOGAI_CODES),
    ],
)
def test_get_track_codes_returns_matching_codes_in_ascending_order(
    turf_dirt: TurfDirt | None,
    race_shubetsu: RaceShubetsu | None,
    expected: tuple[str, ...],
) -> None:
    """芝ダとレース種別に該当するトラックコードを昇順で取得できる。Noneの条件では絞り込まない."""
    assert get_track_codes(turf_dirt, race_shubetsu) == expected


# 準正常系
@pytest.mark.parametrize("code", ["09", "30", "50", "60", "1", "", "芝"])
def test_turf_dirt_from_track_code_with_undefined_code_raises_error(code: str) -> None:
    """定義に無いトラックコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        turf_dirt_from_track_code(code)


@pytest.mark.parametrize("code", ["09", "30", "50", "60", "1", "", "芝"])
def test_race_shubetsu_from_track_code_with_undefined_code_raises_error(code: str) -> None:
    """定義に無いトラックコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        race_shubetsu_from_track_code(code)
