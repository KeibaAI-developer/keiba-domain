"""KeibaDomainErrorのテスト."""

import pytest

from keiba_domain.exceptions import KeibaDomainError


# 正常系
def test_keiba_domain_error_is_exception_subclass() -> None:
    """KeibaDomainErrorがExceptionのサブクラスである"""
    assert issubclass(KeibaDomainError, Exception)


def test_keiba_domain_error_raises_with_message() -> None:
    """KeibaDomainErrorがメッセージを保持して送出できる

    Raises:
        KeibaDomainError: メッセージを保持した状態で意図的に送出する
    """
    with pytest.raises(KeibaDomainError, match="テストエラー"):
        raise KeibaDomainError("テストエラー")
