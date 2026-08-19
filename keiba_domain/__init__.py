"""keiba-domain: 競馬ドメインのマスタ定義と判定処理を集約する最下層ライブラリ.

競馬場・馬場状態・芝ダ・内外・回り・距離区分・コースの大小・枠の定義と判定処理を提供する。
"""

try:
    from importlib.metadata import PackageNotFoundError, version

    __version__ = version("keiba-domain")
except (PackageNotFoundError, ImportError):
    __version__ = "unknown"

from keiba_domain.baba import BABA_CODE_TO_NAME, Baba, baba_from_code
from keiba_domain.exceptions import KeibaDomainError
from keiba_domain.keibajo import (
    CENTRAL_KEIBAJO_CODES,
    KEIBAJO_CODE_TO_LOCAL_NAME,
    KEIBAJO_CODE_TO_NAME,
    Keibajo,
    is_central_keibajo,
    keibajo_from_code,
)

__all__ = [
    "KeibaDomainError",
    "Baba",
    "BABA_CODE_TO_NAME",
    "baba_from_code",
    "Keibajo",
    "KEIBAJO_CODE_TO_NAME",
    "CENTRAL_KEIBAJO_CODES",
    "KEIBAJO_CODE_TO_LOCAL_NAME",
    "keibajo_from_code",
    "is_central_keibajo",
]
