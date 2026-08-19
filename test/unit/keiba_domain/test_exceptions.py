"""KeibaDomainErrorのテスト."""

from keiba_domain import KeibaDomainError


# 正常系
def test_keiba_domain_error_is_exception_subclass() -> None:
    """KeibaDomainErrorがExceptionのサブクラスである."""
    assert issubclass(KeibaDomainError, Exception)


def test_keiba_domain_error_holds_message() -> None:
    """KeibaDomainErrorが送出時のメッセージを保持する."""
    error = KeibaDomainError("テストエラー")

    assert str(error) == "テストエラー"
