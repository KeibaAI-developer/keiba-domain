"""Keibajoに関するEnum・定数・関数のテスト."""

import pytest

from keiba_domain import (
    CENTRAL_KEIBAJO_CODES,
    KEIBAJO_CODE_TO_LOCAL_NAME,
    KEIBAJO_CODE_TO_NAME,
    KEIBAJO_TO_CODE,
    KeibaDomainError,
    Keibajo,
    is_central_keibajo,
    keibajo_from_code,
    keibajo_from_name,
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


@pytest.mark.parametrize("keibajo", list(Keibajo))
def test_keibajo_from_name_returns_central_keibajo(keibajo: Keibajo) -> None:
    """中央10場の名称から対応する中央競馬場を取得できる."""
    assert keibajo_from_name(keibajo.value) == keibajo


@pytest.mark.parametrize("code, keibajo", list(KEIBAJO_CODE_TO_NAME.items()))
def test_keibajo_to_code_is_inverse_of_keibajo_code_to_name(code: str, keibajo: Keibajo) -> None:
    """KEIBAJO_TO_CODEから中央競馬場のコードを引ける."""
    assert KEIBAJO_TO_CODE[keibajo] == code


# 準正常系
@pytest.mark.parametrize("name", ["大井", "門別", "香港", "東京競馬場", "", "05"])
def test_keibajo_from_name_with_non_central_name_raises_error(name: str) -> None:
    """中央10場以外の名称を渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        keibajo_from_name(name)


@pytest.mark.parametrize("code", ["30", "35", "00", "99"])
def test_keibajo_from_code_with_non_central_code_raises_error(code: str) -> None:
    """中央10場以外のコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        keibajo_from_code(code)
