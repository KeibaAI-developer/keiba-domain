"""Keibajoに関するEnum・定数・関数のテスト."""

import pytest

from keiba_domain import (
    CENTRAL_KEIBAJO_CODES,
    KEIBAJO_CODE_TO_LOCAL_NAME,
    KEIBAJO_CODE_TO_NAME,
    KeibaDomainError,
    Keibajo,
    is_central_keibajo,
    keibajo_from_code,
)


# 正常系
@pytest.mark.parametrize(
    "code, expected",
    [
        ("01", Keibajo.SAPPORO),
        ("02", Keibajo.HAKODATE),
        ("03", Keibajo.FUKUSHIMA),
        ("04", Keibajo.NIIGATA),
        ("05", Keibajo.TOKYO),
        ("06", Keibajo.NAKAYAMA),
        ("07", Keibajo.CHUKYO),
        ("08", Keibajo.KYOTO),
        ("09", Keibajo.HANSHIN),
        ("10", Keibajo.KOKURA),
    ],
)
def test_keibajo_from_code_returns_central_keibajo(code: str, expected: Keibajo) -> None:
    """中央10場のコードから対応する中央競馬場を取得できる."""
    assert keibajo_from_code(code) == expected


@pytest.mark.parametrize(
    "code, expected",
    [
        ("05", True),
        ("10", True),
        ("30", False),
        ("99", False),
    ],
)
def test_is_central_keibajo_judges_central_code(code: str, expected: bool) -> None:
    """中央競馬場のコードかどうかを正しく判定できる."""
    assert is_central_keibajo(code) == expected


@pytest.mark.parametrize(
    "code, expected_name",
    [
        ("05", "東京"),
        ("30", "門別"),
        ("35", "盛岡"),
        ("44", "大井"),
        ("65", "帯広"),
    ],
)
def test_keibajo_code_to_local_name_contains_local_keibajo(code: str, expected_name: str) -> None:
    """KEIBAJO_CODE_TO_LOCAL_NAMEから中央・地方の競馬場名を引ける."""
    assert KEIBAJO_CODE_TO_LOCAL_NAME[code] == expected_name


def test_central_keibajo_codes_matches_keibajo_code_to_name_keys() -> None:
    """CENTRAL_KEIBAJO_CODESがKEIBAJO_CODE_TO_NAMEのキー集合と一致する."""
    assert CENTRAL_KEIBAJO_CODES == frozenset(KEIBAJO_CODE_TO_NAME.keys())


# 準正常系
@pytest.mark.parametrize("code", ["30", "35", "00", "99"])
def test_keibajo_from_code_with_non_central_code_raises_error(code: str) -> None:
    """中央10場以外のコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        keibajo_from_code(code)
