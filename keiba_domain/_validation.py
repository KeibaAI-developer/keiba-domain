"""ドメイン定義モジュール間で共有する検証関数.

`keiba_domain` の内部でのみ使用する。公開APIには含めない。
"""

from keiba_domain.exceptions import KeibaDomainError


def validate_distance(distance: int) -> None:
    """距離が正であることを検証する.

    Args:
        distance (int): 距離（メートル）

    Raises:
        KeibaDomainError: 距離が0以下の場合
    """
    if distance <= 0:
        raise KeibaDomainError(f"距離が不正です: {distance}")
