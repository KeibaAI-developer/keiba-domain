"""keiba-domain: 競馬ドメインのマスタ定義と判定処理を集約する最下層ライブラリ.

競馬場・馬場状態・芝ダ・内外・回り・距離区分・コースの大小・枠の定義と判定処理を提供する。
"""

try:
    from importlib.metadata import PackageNotFoundError, version

    __version__ = version("keiba-domain")
except (PackageNotFoundError, ImportError):
    __version__ = "unknown"

from keiba_domain.baba import BABA_CODE_TO_NAME, Baba, baba_from_code
from keiba_domain.course import (
    COURSE_TRACK_SIZE,
    HIDARI_KEIBAJO,
    INOUT_REQUIRED_COURSES,
    MIGI_KEIBAJO,
    Direction,
    Inout,
    TrackSize,
    TurfDirt,
    build_course_key,
    get_course_key_inout,
    get_track_size,
    is_straight_course,
    judge_direction,
    parse_inout,
    parse_turf_dirt,
)
from keiba_domain.distance import (
    ChakudosuKyoriKubun,
    DistanceClass,
    judge_chakudosu_kyori_kubun,
    judge_distance_class,
)
from keiba_domain.exceptions import KeibaDomainError
from keiba_domain.keibajo import (
    CENTRAL_KEIBAJO_CODES,
    KEIBAJO_CODE_TO_LOCAL_NAME,
    KEIBAJO_CODE_TO_NAME,
    Keibajo,
    is_central_keibajo,
    keibajo_from_code,
)
from keiba_domain.waku import (
    WAKU_NUM_TO_WAKU,
    WAKU_TO_WAKU_CLASS,
    Waku,
    WakuClass,
)

__all__ = [
    "BABA_CODE_TO_NAME",
    "CENTRAL_KEIBAJO_CODES",
    "COURSE_TRACK_SIZE",
    "HIDARI_KEIBAJO",
    "INOUT_REQUIRED_COURSES",
    "KEIBAJO_CODE_TO_LOCAL_NAME",
    "KEIBAJO_CODE_TO_NAME",
    "MIGI_KEIBAJO",
    "WAKU_NUM_TO_WAKU",
    "WAKU_TO_WAKU_CLASS",
    "Baba",
    "ChakudosuKyoriKubun",
    "Direction",
    "DistanceClass",
    "Inout",
    "KeibaDomainError",
    "Keibajo",
    "TrackSize",
    "TurfDirt",
    "Waku",
    "WakuClass",
    "baba_from_code",
    "build_course_key",
    "get_course_key_inout",
    "get_track_size",
    "is_central_keibajo",
    "is_straight_course",
    "judge_chakudosu_kyori_kubun",
    "judge_direction",
    "judge_distance_class",
    "keibajo_from_code",
    "parse_inout",
    "parse_turf_dirt",
]
