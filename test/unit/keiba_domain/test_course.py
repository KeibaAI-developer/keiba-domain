"""コース関連のEnum・定数・関数のテスト."""

import pytest

from keiba_domain import (
    HIDARI_KEIBAJO,
    MIGI_KEIBAJO,
    Direction,
    Inout,
    KeibaDomainError,
    Keibajo,
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


# 正常系
@pytest.mark.parametrize(
    "keibajo, turf_dirt, distance, expected",
    [
        # 新潟芝1000mのみ直線コースの例外
        (Keibajo.NIIGATA, TurfDirt.TURF, 1000, Direction.STRAIGHT),
        # 新潟芝1000m以外は例外なく左回り
        (Keibajo.NIIGATA, TurfDirt.TURF, 1200, Direction.LEFT),
        # 左回りの競馬場
        (Keibajo.TOKYO, TurfDirt.TURF, 2000, Direction.LEFT),
        (Keibajo.CHUKYO, TurfDirt.DIRT, 1800, Direction.LEFT),
        # 右回りの競馬場
        (Keibajo.NAKAYAMA, TurfDirt.TURF, 2000, Direction.RIGHT),
        (Keibajo.KYOTO, TurfDirt.DIRT, 1800, Direction.RIGHT),
        (Keibajo.HANSHIN, TurfDirt.TURF, 3200, Direction.RIGHT),
    ],
)
def test_judge_direction_returns_expected_direction(
    keibajo: Keibajo, turf_dirt: TurfDirt, distance: int, expected: Direction
) -> None:
    """競馬場・芝ダ・距離から回りを正しく判定できる."""
    assert judge_direction(keibajo, turf_dirt, distance) == expected


@pytest.mark.parametrize(
    "keibajo, turf_dirt, distance, expected",
    [
        (Keibajo.NIIGATA, TurfDirt.TURF, 1000, True),
        (Keibajo.NIIGATA, TurfDirt.TURF, 1200, False),
        (Keibajo.NIIGATA, TurfDirt.DIRT, 1000, False),
        (Keibajo.TOKYO, TurfDirt.TURF, 1000, False),
    ],
)
def test_is_straight_course_returns_expected_bool(
    keibajo: Keibajo, turf_dirt: TurfDirt, distance: int, expected: bool
) -> None:
    """直線コースかどうかを新潟芝1000mのみTrueと判定できる."""
    assert is_straight_course(keibajo, turf_dirt, distance) == expected


@pytest.mark.parametrize(
    "keibajo, turf_dirt, distance, inout, expected",
    [
        # 内外区別が不要なコースはサフィックスなし
        (Keibajo.TOKYO, TurfDirt.TURF, 2000, None, "東京芝2000"),
        # 内外区別が必要なコースかつ内外指定あり
        (Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.SOTO, "京都芝1600外"),
        (Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.UCHI, "京都芝1600内"),
        # 内外マークなし（None）は内扱い
        (Keibajo.KYOTO, TurfDirt.TURF, 1600, None, "京都芝1600内"),
        # 内-外／外-内もそれぞれ内／外として扱われる
        (Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.UCHI_SOTO, "京都芝1600内"),
        (Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.SOTO_UCHI, "京都芝1600外"),
        (Keibajo.NIIGATA, TurfDirt.TURF, 2000, Inout.SOTO, "新潟芝2000外"),
    ],
)
def test_build_course_key_returns_expected_key(
    keibajo: Keibajo, turf_dirt: TurfDirt, distance: int, inout: Inout | None, expected: str
) -> None:
    """コースキーを正しく構築できる."""
    assert build_course_key(keibajo, turf_dirt, distance, inout) == expected


@pytest.mark.parametrize(
    "course_key, expected",
    [
        ("東京芝2000", TrackSize.BIG),
        ("中山芝2000", TrackSize.SMALL),
        ("京都芝1600内", TrackSize.BIG),
        # 未定義のコースキーはNone
        ("存在しないコース", None),
    ],
)
def test_get_track_size_returns_expected_size(course_key: str, expected: TrackSize | None) -> None:
    """コースキーからコースの大小を正しく取得できる."""
    assert get_track_size(course_key) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        # 障害表記でも芝ダの記載があればそちらを判定する（平地障害は別概念）
        ("障芝3000", TurfDirt.TURF),
        ("芝2000m(左 A)", TurfDirt.TURF),
        ("ダ1800m(右 A)", TurfDirt.DIRT),
        # 判定できない場合はNone（netkeibaの障害表記は芝ダの記載がない）
        ("2000m(左 A)", None),
        ("障2880m", None),
    ],
)
def test_parse_turf_dirt_returns_expected_turf_dirt(text: str, expected: TurfDirt | None) -> None:
    """文字列から芝ダを正しく判定できる."""
    assert parse_turf_dirt(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("右 外 B", Inout.SOTO),
        ("左 内 A", Inout.UCHI),
        # 内外両方を含む場合は外-内（阪神芝3200mのみ外回りと内回りの両方を使用）
        ("右 外-内 A", Inout.SOTO_UCHI),
        # 内外どちらも含まない場合はNone
        ("右 B", None),
    ],
)
def test_parse_inout_returns_expected_inout(text: str, expected: Inout | None) -> None:
    """文字列から内外を正しく判定できる."""
    assert parse_inout(text) == expected


# 準正常系
@pytest.mark.parametrize("distance", [0, -1, -2000])
def test_judge_direction_raises_for_non_positive_distance(distance: int) -> None:
    """距離が0以下の場合はKeibaDomainErrorが発生する."""
    with pytest.raises(KeibaDomainError, match="距離が不正です"):
        judge_direction(Keibajo.TOKYO, TurfDirt.TURF, distance)


@pytest.mark.parametrize("distance", [0, -1, -1600])
def test_get_course_key_inout_raises_for_non_positive_distance(distance: int) -> None:
    """距離が0以下の場合はKeibaDomainErrorが発生する."""
    with pytest.raises(KeibaDomainError, match="距離が不正です"):
        get_course_key_inout(Keibajo.KYOTO, TurfDirt.TURF, distance, None)


@pytest.mark.parametrize("distance", [0, -1, -2000])
def test_build_course_key_raises_for_non_positive_distance(distance: int) -> None:
    """距離が0以下の場合はKeibaDomainErrorが発生する."""
    with pytest.raises(KeibaDomainError, match="距離が不正です"):
        build_course_key(Keibajo.TOKYO, TurfDirt.TURF, distance)


def test_migi_and_hidari_keibajo_cover_all_keibajo() -> None:
    """右回りと左回りの集合が中央10場を重複なく網羅している."""
    assert MIGI_KEIBAJO | HIDARI_KEIBAJO == set(Keibajo)
    assert MIGI_KEIBAJO & HIDARI_KEIBAJO == set()


@pytest.mark.parametrize(
    "text, expected",
    [
        ("右 内-外 A", Inout.UCHI_SOTO),
        ("右 外-内 A", Inout.SOTO_UCHI),
        ("右 外 内 A", Inout.SOTO_UCHI),
    ],
)
def test_parse_inout_prefers_explicit_notation(text: str, expected: Inout) -> None:
    """内外を併記した表記から内外を判定できる."""
    assert parse_inout(text) == expected


# 準正常系
@pytest.mark.parametrize("distance", [0, -1, -2000])
def test_is_straight_course_raises_for_non_positive_distance(distance: int) -> None:
    """距離が0以下の場合はKeibaDomainErrorが発生する."""
    with pytest.raises(KeibaDomainError, match="距離が不正です"):
        is_straight_course(Keibajo.NIIGATA, TurfDirt.TURF, distance)


def test_race_shubetsu_values() -> None:
    """RaceShubetsuがレース種別カラムの値と一致する."""
    assert RaceShubetsu.HEICHI == "平地"
    assert RaceShubetsu.SHOGAI == "障害"
