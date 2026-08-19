"""コース情報のEnumと判定関数.

芝ダ・内外・回り・コースの大小・コースキーに関するEnum・定数・判定関数を提供する。
"""

from enum import StrEnum

from keiba_domain._validation import validate_distance
from keiba_domain.exceptions import KeibaDomainError
from keiba_domain.keibajo import Keibajo


class TurfDirt(StrEnum):
    """芝・ダート・障害の区別を表すEnum.

    Attributes:
        TURF: 芝
        DIRT: ダート
        STEEPLECHASE: 障害
    """

    TURF = "芝"
    DIRT = "ダ"
    STEEPLECHASE = "障"


class Inout(StrEnum):
    """内外を表すEnum.

    Attributes:
        UCHI: 内
        SOTO: 外
        UCHI_SOTO: 内-外
        SOTO_UCHI: 外-内
    """

    UCHI = "内"
    SOTO = "外"
    UCHI_SOTO = "内-外"
    SOTO_UCHI = "外-内"


class Direction(StrEnum):
    """コースの左右方向を表すEnum.

    Attributes:
        LEFT: 左回り
        RIGHT: 右回り
        STRAIGHT: 直線
    """

    LEFT = "左"
    RIGHT = "右"
    STRAIGHT = "直"


class TrackSize(StrEnum):
    """コースの大小区分を表すEnum.

    Attributes:
        BIG: 大箱
        SMALL: 小回り
    """

    BIG = "大"
    SMALL = "小"


# 右回りの競馬場
MIGI_KEIBAJO: frozenset[Keibajo] = frozenset(
    {
        Keibajo.SAPPORO,
        Keibajo.HAKODATE,
        Keibajo.FUKUSHIMA,
        Keibajo.NAKAYAMA,
        Keibajo.KYOTO,
        Keibajo.HANSHIN,
        Keibajo.KOKURA,
    }
)

# 左回りの競馬場
HIDARI_KEIBAJO: frozenset[Keibajo] = frozenset(
    {
        Keibajo.NIIGATA,
        Keibajo.TOKYO,
        Keibajo.CHUKYO,
    }
)

# 内外の区別が必要なコース
INOUT_REQUIRED_COURSES: frozenset[str] = frozenset({"京都芝1400", "京都芝1600", "新潟芝2000"})

# コースキー→コースの大小。直線コースは未定義
COURSE_TRACK_SIZE: dict[str, TrackSize] = {
    "東京芝1400": TrackSize.BIG,
    "東京芝1600": TrackSize.BIG,
    "東京芝1800": TrackSize.BIG,
    "東京芝2000": TrackSize.BIG,
    "東京芝2300": TrackSize.BIG,
    "東京芝2400": TrackSize.BIG,
    "東京芝2500": TrackSize.BIG,
    "東京芝3400": TrackSize.BIG,
    "阪神芝1200": TrackSize.BIG,
    "阪神芝1400": TrackSize.BIG,
    "阪神芝1600": TrackSize.BIG,
    "阪神芝1800": TrackSize.BIG,
    "阪神芝2000": TrackSize.BIG,
    "阪神芝2200": TrackSize.BIG,
    "阪神芝2400": TrackSize.BIG,
    "阪神芝2600": TrackSize.BIG,
    "阪神芝3000": TrackSize.BIG,
    "阪神芝3200": TrackSize.BIG,
    "中山芝1200": TrackSize.SMALL,
    "中山芝1600": TrackSize.SMALL,
    "中山芝1800": TrackSize.SMALL,
    "中山芝2000": TrackSize.SMALL,
    "中山芝2200": TrackSize.SMALL,
    "中山芝2500": TrackSize.SMALL,
    "中山芝3600": TrackSize.SMALL,
    "京都芝1200": TrackSize.BIG,
    "京都芝1400内": TrackSize.BIG,
    "京都芝1400外": TrackSize.BIG,
    "京都芝1600内": TrackSize.BIG,
    "京都芝1600外": TrackSize.BIG,
    "京都芝1800": TrackSize.BIG,
    "京都芝2000": TrackSize.BIG,
    "京都芝2200": TrackSize.BIG,
    "京都芝2400": TrackSize.BIG,
    "京都芝3000": TrackSize.BIG,
    "京都芝3200": TrackSize.BIG,
    "中京芝1200": TrackSize.SMALL,
    "中京芝1400": TrackSize.SMALL,
    "中京芝1600": TrackSize.SMALL,
    "中京芝2000": TrackSize.SMALL,
    "中京芝2200": TrackSize.SMALL,
    "中京芝3000": TrackSize.SMALL,
    "福島芝1000": TrackSize.SMALL,
    "福島芝1200": TrackSize.SMALL,
    "福島芝1700": TrackSize.SMALL,
    "福島芝1800": TrackSize.SMALL,
    "福島芝2000": TrackSize.SMALL,
    "福島芝2600": TrackSize.SMALL,
    "新潟芝1200": TrackSize.SMALL,
    "新潟芝1400": TrackSize.SMALL,
    "新潟芝1600": TrackSize.SMALL,
    "新潟芝1800": TrackSize.SMALL,
    "新潟芝2000内": TrackSize.SMALL,
    "新潟芝2000外": TrackSize.SMALL,
    "新潟芝2200": TrackSize.SMALL,
    "新潟芝2400": TrackSize.SMALL,
    "札幌芝1000": TrackSize.BIG,
    "札幌芝1200": TrackSize.BIG,
    "札幌芝1500": TrackSize.BIG,
    "札幌芝1800": TrackSize.BIG,
    "札幌芝2000": TrackSize.BIG,
    "札幌芝2600": TrackSize.BIG,
    "函館芝1000": TrackSize.SMALL,
    "函館芝1200": TrackSize.SMALL,
    "函館芝1800": TrackSize.SMALL,
    "函館芝2000": TrackSize.SMALL,
    "函館芝2600": TrackSize.SMALL,
    "小倉芝1000": TrackSize.SMALL,
    "小倉芝1200": TrackSize.SMALL,
    "小倉芝1700": TrackSize.SMALL,
    "小倉芝1800": TrackSize.SMALL,
    "小倉芝2000": TrackSize.SMALL,
    "小倉芝2600": TrackSize.SMALL,
    "東京ダ1300": TrackSize.BIG,
    "東京ダ1400": TrackSize.BIG,
    "東京ダ1600": TrackSize.BIG,
    "東京ダ2100": TrackSize.BIG,
    "東京ダ2400": TrackSize.BIG,
    "阪神ダ1200": TrackSize.BIG,
    "阪神ダ1400": TrackSize.BIG,
    "阪神ダ1800": TrackSize.BIG,
    "阪神ダ2000": TrackSize.BIG,
    "中山ダ1200": TrackSize.SMALL,
    "中山ダ1800": TrackSize.SMALL,
    "中山ダ2400": TrackSize.SMALL,
    "中山ダ2500": TrackSize.SMALL,
    "京都ダ1200": TrackSize.BIG,
    "京都ダ1400": TrackSize.BIG,
    "京都ダ1800": TrackSize.BIG,
    "京都ダ1900": TrackSize.BIG,
    "中京ダ1200": TrackSize.SMALL,
    "中京ダ1400": TrackSize.SMALL,
    "中京ダ1800": TrackSize.SMALL,
    "中京ダ1900": TrackSize.SMALL,
    "福島ダ1000": TrackSize.SMALL,
    "福島ダ1150": TrackSize.SMALL,
    "福島ダ1700": TrackSize.SMALL,
    "福島ダ2400": TrackSize.SMALL,
    "新潟ダ1200": TrackSize.SMALL,
    "新潟ダ1800": TrackSize.SMALL,
    "新潟ダ2500": TrackSize.SMALL,
    "札幌ダ1000": TrackSize.BIG,
    "札幌ダ1700": TrackSize.BIG,
    "札幌ダ2400": TrackSize.BIG,
    "函館ダ1000": TrackSize.SMALL,
    "函館ダ1700": TrackSize.SMALL,
    "函館ダ2400": TrackSize.SMALL,
    "小倉ダ1000": TrackSize.SMALL,
    "小倉ダ1700": TrackSize.SMALL,
    "小倉ダ2400": TrackSize.SMALL,
}


def parse_turf_dirt(text: str) -> TurfDirt | None:
    """芝ダを含む文字列から芝ダを判定する.

    "障"を含む場合を最優先とし、次に"芝"、"ダ"の順に判定する。

    Args:
        text (str): 芝ダを含む文字列（例: "芝2000m(左 A)"）

    Returns:
        TurfDirt | None: 芝ダ。判定できない場合はNone
    """
    if "障" in text:
        return TurfDirt.STEEPLECHASE
    if "芝" in text:
        return TurfDirt.TURF
    if "ダ" in text:
        return TurfDirt.DIRT
    return None


def parse_inout(text: str) -> Inout | None:
    """内外を含む文字列から内外を判定する.

    "内-外" / "外-内" という明示的な表記を優先して判定する。
    区切りのない状態で"内"と"外"の両方を含む場合は外-内と判定する
    （阪神芝3200mのみ外回りと内回りの両方を使用する）。

    Args:
        text (str): 内外を含む文字列（例: "右 外 B"）

    Returns:
        Inout | None: 内外。判定できない場合はNone
    """
    if Inout.UCHI_SOTO in text:
        return Inout.UCHI_SOTO
    if Inout.SOTO_UCHI in text:
        return Inout.SOTO_UCHI
    has_uchi = "内" in text
    has_soto = "外" in text
    if has_uchi and has_soto:
        return Inout.SOTO_UCHI
    if has_uchi:
        return Inout.UCHI
    if has_soto:
        return Inout.SOTO
    return None


def judge_direction(keibajo: Keibajo, turf_dirt: TurfDirt, distance: int) -> Direction:
    """競馬場・芝ダ・距離から回りを判定する.

    新潟芝1000mのみ直線コースの例外として扱う。

    Args:
        keibajo (Keibajo): 競馬場
        turf_dirt (TurfDirt): 芝ダ
        distance (int): 距離（メートル）

    Returns:
        Direction: 回り

    Raises:
        KeibaDomainError: 距離が0以下の場合、または競馬場が右回り・左回りのいずれにも
            分類されていない場合
    """
    validate_distance(distance)
    if keibajo == Keibajo.NIIGATA and turf_dirt == TurfDirt.TURF and distance == 1000:
        return Direction.STRAIGHT
    if keibajo in MIGI_KEIBAJO:
        return Direction.RIGHT
    if keibajo in HIDARI_KEIBAJO:
        return Direction.LEFT
    raise KeibaDomainError(f"回りが分類されていない競馬場です: {keibajo}")


def is_straight_course(keibajo: Keibajo, turf_dirt: TurfDirt, distance: int) -> bool:
    """直線コースかどうかを判定する.

    Args:
        keibajo (Keibajo): 競馬場
        turf_dirt (TurfDirt): 芝ダ
        distance (int): 距離（メートル）

    Returns:
        bool: 直線コースであればTrue

    Raises:
        KeibaDomainError: 距離が0以下の場合
    """
    return judge_direction(keibajo, turf_dirt, distance) == Direction.STRAIGHT


def get_course_key_inout(
    keibajo: Keibajo, turf_dirt: TurfDirt, distance: int, inout: Inout | None
) -> str:
    """コースキー用の内外サフィックスを取得する.

    INOUT_REQUIRED_COURSESに該当するコースのみ内外サフィックスを返す。

    Args:
        keibajo (Keibajo): 競馬場
        turf_dirt (TurfDirt): 芝ダ
        distance (int): 距離（メートル）
        inout (Inout | None): 内外

    Returns:
        str: 内外サフィックス（"内" / "外"）。内外区別が不要なコースは空文字。
            inoutがNone・内・内-外の場合は"内"、それ以外は"外"

    Raises:
        KeibaDomainError: 距離が0以下の場合
    """
    validate_distance(distance)
    base_course = f"{keibajo}{turf_dirt}{distance}"
    if base_course not in INOUT_REQUIRED_COURSES:
        return ""
    if inout is None or inout in (Inout.UCHI, Inout.UCHI_SOTO):
        return "内"
    return "外"


def build_course_key(
    keibajo: Keibajo, turf_dirt: TurfDirt, distance: int, inout: Inout | None = None
) -> str:
    """コースキーを構築する.

    競馬場名 + 芝ダ + 距離 + コースキー用内外を連結する。

    Args:
        keibajo (Keibajo): 競馬場
        turf_dirt (TurfDirt): 芝ダ
        distance (int): 距離（メートル）
        inout (Inout | None): 内外

    Returns:
        str: コースキー（例: "東京芝2000", "京都芝1600内"）

    Raises:
        KeibaDomainError: 距離が0以下の場合
    """
    suffix = get_course_key_inout(keibajo, turf_dirt, distance, inout)
    return f"{keibajo}{turf_dirt}{distance}{suffix}"


def get_track_size(course_key: str) -> TrackSize | None:
    """コースキーからコースの大小を取得する.

    Args:
        course_key (str): コースキー（例: "東京芝2000", "京都芝1600内"）

    Returns:
        TrackSize | None: コースの大小。直線コースや未定義コースはNone
    """
    return COURSE_TRACK_SIZE.get(course_key)
