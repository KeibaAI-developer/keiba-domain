"""keiba-domain: 競馬ドメインのマスタ定義と判定処理を集約する最下層ライブラリ.

競馬場・馬場状態・芝ダ・内外・回り・距離区分・コースの大小・枠の定義と判定処理を提供する。
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
