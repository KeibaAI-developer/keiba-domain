"""Gradeに関するEnum・定数・関数のテスト."""

import pytest

from keiba_domain import Grade, KeibaDomainError, grade_from_code


# 正常系
@pytest.mark.parametrize(
    "code, expected",
    [
        ("A", Grade.G1),
        ("B", Grade.G2),
        ("C", Grade.G3),
        ("D", Grade.JUSHO),
        ("E", Grade.TOKUBETSU),
        ("F", Grade.J_G1),
        ("G", Grade.J_G2),
        ("H", Grade.J_G3),
        ("L", Grade.LISTED),
    ],
)
def test_grade_from_code_returns_grade(code: str, expected: Grade) -> None:
    """グレードコードから対応するグレードを取得できる."""
    assert grade_from_code(code) == expected


@pytest.mark.parametrize("code", [" ", "", "  ", "_", " _ "])
def test_grade_from_code_with_general_race_code_returns_none(code: str) -> None:
    """空白だけ・空・"_"のコード（一般競走）の場合はNoneを返す."""
    assert grade_from_code(code) is None


def test_grade_from_code_ignores_surrounding_whitespace() -> None:
    """前後に空白が付いたコードは、空白を除いて判定する."""
    assert grade_from_code(" A ") == Grade.G1


# 準正常系
@pytest.mark.parametrize("code", ["I", "K", "M", "a", "1", "G1", "__", "-"])
def test_grade_from_code_with_undefined_code_raises_error(code: str) -> None:
    """定義に無いグレードコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        grade_from_code(code)
