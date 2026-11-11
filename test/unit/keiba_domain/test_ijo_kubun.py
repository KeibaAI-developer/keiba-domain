"""IjoKubunに関するEnum・定数・関数のテスト."""

import pytest

from keiba_domain import (
    NOT_FINISHED_IJO_KUBUN_CODES,
    NOT_STARTED_IJO_KUBUN_CODES,
    IjoKubun,
    KeibaDomainError,
    ijo_kubun_from_code,
)


# 正常系
@pytest.mark.parametrize(
    "code, expected",
    [
        ("1", IjoKubun.SHUSSO_TORIKESHI),
        ("2", IjoKubun.HASSO_JOGAI),
        ("3", IjoKubun.KYOSO_JOGAI),
        ("4", IjoKubun.KYOSO_CHUSHI),
        ("5", IjoKubun.SHIKKAKU),
        ("6", IjoKubun.RAKUBA_SAIKIJO),
        ("7", IjoKubun.KOCHAKU),
    ],
)
def test_ijo_kubun_from_code_returns_ijo_kubun(code: str, expected: IjoKubun) -> None:
    """コード1〜7から対応する異常区分を取得できる."""
    assert ijo_kubun_from_code(code) == expected


def test_ijo_kubun_from_code_with_zero_returns_none() -> None:
    """コード"0"（異常なし）の場合はNoneを返す."""
    assert ijo_kubun_from_code("0") is None


def test_not_started_ijo_kubun_codes_are_torikeshi_and_jogai() -> None:
    """出走しなかった馬のコードが出走取消・発走除外・競走除外の3つである."""
    assert NOT_STARTED_IJO_KUBUN_CODES == frozenset({"1", "2", "3"})


def test_not_finished_ijo_kubun_codes_add_chushi_to_not_started() -> None:
    """完走しなかった馬のコードが、出走しなかった馬のコードと競走中止である."""
    assert NOT_FINISHED_IJO_KUBUN_CODES == frozenset({"1", "2", "3", "4"})


# 準正常系
@pytest.mark.parametrize("code", ["8", "9", "a", "", "01"])
def test_ijo_kubun_from_code_with_invalid_code_raises_error(code: str) -> None:
    """0〜7以外のコードを渡すとKeibaDomainErrorが送出される."""
    with pytest.raises(KeibaDomainError):
        ijo_kubun_from_code(code)
