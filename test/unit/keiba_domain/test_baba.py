"""Babaに関するEnum・定数・関数のテスト."""

import pytest

from keiba_domain import Baba, KeibaDomainError, baba_from_code


# 正常系
@pytest.mark.parametrize(
    "code, expected",
    [
        ("1", Baba.GOOD),
        ("2", Baba.SLIGHTLY_HEAVY),
        ("3", Baba.HEAVY),
        ("4", Baba.VERY_HEAVY),
    ],
)
def test_baba_from_code_returns_baba(code: str, expected: Baba) -> None:
    """"1"〜"4"のコードから対応する馬場状態を取得できる."""
    assert baba_from_code(code) == expected


def test_baba_from_code_with_zero_returns_none() -> None:
    """コード"0"（未設定）の場合はNoneを返す."""
    assert baba_from_code("0") is None


# 準正常系
@pytest.mark.parametrize("code", ["5", "9", "a", ""])
def test_baba_from_code_with_invalid_code_raises_error(code: str) -> None:
    """"0"〜"4"以外のコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        baba_from_code(code)
