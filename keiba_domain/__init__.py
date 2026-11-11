"""keiba-domain: 競馬ドメインのマスタ定義と判定処理を集約する最下層ライブラリ.

競馬場・馬場状態・芝ダ・内外・回り・距離区分・コースの大小・枠・レースコード・トラックコード・
異常区分・グレードの定義と判定処理を提供する。
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
    RaceShubetsu,
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
from keiba_domain.grade import GRADE_CODE_TO_NAME, Grade, grade_from_code
from keiba_domain.ijo_kubun import (
    IJO_KUBUN_CODE_TO_NAME,
    NOT_FINISHED_IJO_KUBUN_CODES,
    NOT_STARTED_IJO_KUBUN_CODES,
    IjoKubun,
    ijo_kubun_from_code,
)
from keiba_domain.keibajo import (
    CENTRAL_KEIBAJO_CODES,
    KEIBAJO_CODE_TO_LOCAL_NAME,
    KEIBAJO_CODE_TO_NAME,
    KEIBAJO_TO_CODE,
    Keibajo,
    is_central_keibajo,
    keibajo_from_code,
    keibajo_from_name,
)
from keiba_domain.race_code import (
    RACE_CODE_LENGTH,
    extract_race_code_parts,
    validate_race_code,
)
from keiba_domain.track_code import (
    TRACK_CODE_TO_RACE_SHUBETSU,
    TRACK_CODE_TO_TURF_DIRT,
    get_track_codes,
    race_shubetsu_from_track_code,
    turf_dirt_from_track_code,
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
    "GRADE_CODE_TO_NAME",
    "HIDARI_KEIBAJO",
    "IJO_KUBUN_CODE_TO_NAME",
    "INOUT_REQUIRED_COURSES",
    "KEIBAJO_CODE_TO_LOCAL_NAME",
    "KEIBAJO_CODE_TO_NAME",
    "KEIBAJO_TO_CODE",
    "MIGI_KEIBAJO",
    "NOT_FINISHED_IJO_KUBUN_CODES",
    "NOT_STARTED_IJO_KUBUN_CODES",
    "RACE_CODE_LENGTH",
    "TRACK_CODE_TO_RACE_SHUBETSU",
    "TRACK_CODE_TO_TURF_DIRT",
    "WAKU_NUM_TO_WAKU",
    "WAKU_TO_WAKU_CLASS",
    "Baba",
    "ChakudosuKyoriKubun",
    "Direction",
    "DistanceClass",
    "Grade",
    "IjoKubun",
    "Inout",
    "KeibaDomainError",
    "Keibajo",
    "RaceShubetsu",
    "TrackSize",
    "TurfDirt",
    "Waku",
    "WakuClass",
    "baba_from_code",
    "build_course_key",
    "extract_race_code_parts",
    "get_course_key_inout",
    "get_track_codes",
    "get_track_size",
    "grade_from_code",
    "ijo_kubun_from_code",
    "is_central_keibajo",
    "is_straight_course",
    "judge_chakudosu_kyori_kubun",
    "judge_direction",
    "judge_distance_class",
    "keibajo_from_code",
    "keibajo_from_name",
    "parse_inout",
    "parse_turf_dirt",
    "race_shubetsu_from_track_code",
    "turf_dirt_from_track_code",
    "validate_race_code",
]
