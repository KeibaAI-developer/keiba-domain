"""keiba-domain: 競馬ドメインのマスタ定義と判定処理を集約する最下層ライブラリ.

このライブラリは、競馬ドメインのマスタ定義と判定処理を集約する最下層ライブラリを提供します。
"""

try:
    from importlib.metadata import PackageNotFoundError, version

    __version__ = version("keiba-domain")
except (PackageNotFoundError, ImportError):
    __version__ = "unknown"

from keiba_domain.exceptions import KeibaDomainError

__all__ = [
    "KeibaDomainError",
]
