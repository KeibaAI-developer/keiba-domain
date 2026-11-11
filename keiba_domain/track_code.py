"""トラックコードと芝ダ・レース種別の対応.

JRA-VANのトラックコードから芝ダ（TurfDirt）とレース種別（RaceShubetsu）を引く対応表と
判定関数を提供する。
"""

from keiba_domain.course import RaceShubetsu, TurfDirt
from keiba_domain.exceptions import KeibaDomainError

# 未設定を表すトラックコード
_UNSET_TRACK_CODE = "00"

# トラックコード→芝ダ。"10"〜"22"は平地の芝、"23"〜"29"は平地のダート（サンドを含む）、
# "51"〜"59"は障害。障害コースの芝ダは芝として扱う
TRACK_CODE_TO_TURF_DIRT: dict[str, TurfDirt] = {
    **{str(code): TurfDirt.TURF for code in range(10, 23)},
    **{str(code): TurfDirt.DIRT for code in range(23, 30)},
    **{str(code): TurfDirt.TURF for code in range(51, 60)},
}

# トラックコード→レース種別。"10"〜"29"は平地、"51"〜"59"は障害
TRACK_CODE_TO_RACE_SHUBETSU: dict[str, RaceShubetsu] = {
    **{str(code): RaceShubetsu.HEICHI for code in range(10, 30)},
    **{str(code): RaceShubetsu.SHOGAI for code in range(51, 60)},
}


def turf_dirt_from_track_code(code: str) -> TurfDirt | None:
    """トラックコードから芝ダを取得する.

    Args:
        code (str): トラックコード（例: "17"）

    Returns:
        TurfDirt | None: 芝ダ。コードが"00"（未設定）の場合はNone

    Raises:
        KeibaDomainError: codeが"00"でも定義済みのトラックコードでもない場合
    """
    if code == _UNSET_TRACK_CODE:
        return None
    if code not in TRACK_CODE_TO_TURF_DIRT:
        raise KeibaDomainError(f"トラックコードが不正です: {code}")
    return TRACK_CODE_TO_TURF_DIRT[code]


def race_shubetsu_from_track_code(code: str) -> RaceShubetsu | None:
    """トラックコードからレース種別（平地・障害）を取得する.

    Args:
        code (str): トラックコード（例: "17"）

    Returns:
        RaceShubetsu | None: レース種別。コードが"00"（未設定）の場合はNone

    Raises:
        KeibaDomainError: codeが"00"でも定義済みのトラックコードでもない場合
    """
    if code == _UNSET_TRACK_CODE:
        return None
    if code not in TRACK_CODE_TO_RACE_SHUBETSU:
        raise KeibaDomainError(f"トラックコードが不正です: {code}")
    return TRACK_CODE_TO_RACE_SHUBETSU[code]


def get_track_codes(
    turf_dirt: TurfDirt | None = None, race_shubetsu: RaceShubetsu | None = None
) -> tuple[str, ...]:
    """芝ダとレース種別に該当するトラックコードを昇順で取得する.

    Noneを指定した条件では絞り込まない。

    Args:
        turf_dirt (TurfDirt | None): 芝ダ
        race_shubetsu (RaceShubetsu | None): レース種別

    Returns:
        tuple[str, ...]: 該当するトラックコード（昇順）
    """
    return tuple(
        code
        for code in sorted(TRACK_CODE_TO_TURF_DIRT)
        if (turf_dirt is None or TRACK_CODE_TO_TURF_DIRT[code] == turf_dirt)
        and (race_shubetsu is None or TRACK_CODE_TO_RACE_SHUBETSU[code] == race_shubetsu)
    )
