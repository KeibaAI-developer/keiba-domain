"""レースコードの検証と分解のテスト."""

import pytest

from keiba_domain import (
    RACE_CODE_LENGTH,
    KeibaDomainError,
    extract_race_code_parts,
    validate_race_code,
)


# 正常系
def test_validate_race_code_accepts_16_digits() -> None:
    """半角数字16桁のレースコードは例外を送出しない."""
    validate_race_code("2026111508050411")


def test_race_code_length_is_16() -> None:
    """RACE_CODE_LENGTHが16である."""
    assert RACE_CODE_LENGTH == 16


def test_extract_race_code_parts_returns_each_part() -> None:
    """レースコードを年・月日・競馬場コード・回・日目・Rに分解できる."""
    assert extract_race_code_parts("2026111508050411") == {
        "年": "2026",
        "月日": "1115",
        "競馬場コード": "08",
        "回": "05",
        "日目": "04",
        "R": "11",
    }


# 準正常系
@pytest.mark.parametrize(
    "race_code",
    [
        "",
        "202611150805041",
        "20261115080504111",
        "20261115080504ab",
        "２０２６１１１５０８０５０４１１",
        "2026111508050411\n",
        " 2026111508050411",
        "2026111508050411 ",
        "2026-11-15-08-05",
    ],
)
def test_validate_race_code_with_invalid_format_raises_error(race_code: str) -> None:
    """半角数字16桁でないレースコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        validate_race_code(race_code)


def test_extract_race_code_parts_with_invalid_format_raises_error() -> None:
    """形式が不正なレースコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        extract_race_code_parts("20261115080504")
