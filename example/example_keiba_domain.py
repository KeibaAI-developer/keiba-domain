"""keiba-domain の主要な公開APIを一通り呼び出すサンプルスクリプト.

競馬場・馬場状態・距離区分・枠・コース・レースコード・トラックコード・異常区分・グレードの
ドメイン定義と判定関数を呼び出し、
結果と例外が送出されるケースを表示する。外部データ（DB・ネットワーク・ファイル）には依存しない。
"""

from keiba_domain import (
    KEIBAJO_TO_CODE,
    NOT_FINISHED_IJO_KUBUN_CODES,
    NOT_STARTED_IJO_KUBUN_CODES,
    WAKU_NUM_TO_WAKU,
    WAKU_TO_WAKU_CLASS,
    Baba,
    ChakudosuKyoriKubun,
    Direction,
    DistanceClass,
    Grade,
    IjoKubun,
    Inout,
    KeibaDomainError,
    Keibajo,
    RaceShubetsu,
    TrackSize,
    TurfDirt,
    Waku,
    baba_from_code,
    build_course_key,
    extract_race_code_parts,
    get_course_key_inout,
    get_track_codes,
    get_track_size,
    grade_from_code,
    ijo_kubun_from_code,
    is_central_keibajo,
    is_straight_course,
    judge_chakudosu_kyori_kubun,
    judge_direction,
    judge_distance_class,
    keibajo_from_code,
    keibajo_from_name,
    parse_inout,
    parse_turf_dirt,
    race_shubetsu_from_track_code,
    turf_dirt_from_track_code,
    validate_race_code,
)


def show_keibajo() -> None:
    """競馬場（keibajo）モジュールの使用例を表示する.

    keibajo_from_code は中央10場以外のコードで KeibaDomainError を送出する一方、
    is_central_keibajo は地方・未知のコードでも例外を送出せず False を返すことを示す。
    """
    _print_section("競馬場")

    keibajo = keibajo_from_code("05")
    print(f"keibajo_from_code('05') = {keibajo}")

    try:
        keibajo_from_code("42")  # 地方（浦和）のコード
    except KeibaDomainError as e:
        print(f"keibajo_from_code('42') は例外を送出: {e}")

    print(f"is_central_keibajo('05') = {is_central_keibajo('05')}")
    print(f"is_central_keibajo('42') = {is_central_keibajo('42')}（地方でも例外は送出しない）")
    print(f"is_central_keibajo('99') = {is_central_keibajo('99')}（未知のコードでも同様）")

    kyoto = keibajo_from_name("京都")
    print(f"keibajo_from_name('京都') = {kyoto}（コード: {KEIBAJO_TO_CODE[kyoto]}）")

    try:
        keibajo_from_name("大井")
    except KeibaDomainError as e:
        print(f"keibajo_from_name('大井') は例外を送出: {e}")


def show_baba() -> None:
    """馬場状態（baba）モジュールの使用例を表示する.

    baba_from_code はコード"0"（未設定）を None として返し、
    範囲外のコードは KeibaDomainError を送出することで「値なし」と「値の不正」を区別する。
    """
    _print_section("馬場状態")

    good = baba_from_code("1")
    print(f"baba_from_code('1') = {good}")

    unset = baba_from_code("0")
    print(f"baba_from_code('0') = {unset}（未設定を表すNone）")

    try:
        baba_from_code("9")
    except KeibaDomainError as e:
        print(f"baba_from_code('9') は例外を送出: {e}")

    print(f"Baba.HEAVY = {Baba.HEAVY}")


def show_distance() -> None:
    """距離区分（distance）モジュールの使用例を表示する.

    学習用のDistanceClassとJV-VAN出走別着度数のChakudosuKyoriKubunは
    境界が異なる別概念であることを示す。
    """
    _print_section("距離区分")

    distance_class = judge_distance_class(2000)
    print(f"judge_distance_class(2000) = {distance_class}")
    print(f"judge_distance_class(1400) = {judge_distance_class(1400)}")

    kyori_kubun = judge_chakudosu_kyori_kubun(2000)
    print(f"judge_chakudosu_kyori_kubun(2000) = {kyori_kubun}")

    try:
        judge_distance_class(0)
    except KeibaDomainError as e:
        print(f"judge_distance_class(0) は例外を送出: {e}")

    print(f"DistanceClass一覧: {[member.value for member in DistanceClass]}")
    print(f"ChakudosuKyoriKubun一覧: {[member.value for member in ChakudosuKyoriKubun]}")


def show_waku() -> None:
    """枠（waku）モジュールの使用例を表示する."""
    _print_section("枠")

    waku = WAKU_NUM_TO_WAKU[1]
    print(f"WAKU_NUM_TO_WAKU[1] = {waku}")

    waku_class = WAKU_TO_WAKU_CLASS[Waku.WAKU1]
    print(f"WAKU_TO_WAKU_CLASS[Waku.WAKU1] = {waku_class}")
    print(f"WAKU_TO_WAKU_CLASS[Waku.WAKU8] = {WAKU_TO_WAKU_CLASS[Waku.WAKU8]}")


def show_course() -> None:
    """コース（course）モジュールの使用例を表示する.

    芝ダ・内外の判定、回りの判定、コースキーの構築、コースの大小の取得を示す。
    """
    _print_section("コース")

    turf_dirt = parse_turf_dirt("芝2000m(左 A)")
    print(f"parse_turf_dirt('芝2000m(左 A)') = {turf_dirt}")
    no_turf_dirt = parse_turf_dirt("障2880m")
    print(f"parse_turf_dirt('障2880m') = {no_turf_dirt}（芝ダの記載がない文字列はNone）")
    print(f"RaceShubetsu.SHOGAI = {RaceShubetsu.SHOGAI}（平地か障害かは芝ダとは別概念）")

    inout = parse_inout("右 外 B")
    print(f"parse_inout('右 外 B') = {inout}")

    direction = judge_direction(Keibajo.NIIGATA, TurfDirt.TURF, 1000)
    print(f"judge_direction(新潟, 芝, 1000) = {direction}（新潟芝1000mのみ直線の例外）")
    is_straight = is_straight_course(Keibajo.NIIGATA, TurfDirt.TURF, 1000)
    print(f"is_straight_course(新潟, 芝, 1000) = {is_straight}")

    direction_tokyo = judge_direction(Keibajo.TOKYO, TurfDirt.TURF, 2000)
    print(f"judge_direction(東京, 芝, 2000) = {direction_tokyo}")

    inout_suffix = get_course_key_inout(Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.SOTO)
    print(f"get_course_key_inout(京都, 芝, 1600, 外) = '{inout_suffix}'")

    course_key = build_course_key(Keibajo.KYOTO, TurfDirt.TURF, 1600, Inout.SOTO)
    print(f"build_course_key(京都, 芝, 1600, 外) = {course_key}")

    track_size = get_track_size("東京芝2000")
    print(f"get_track_size('東京芝2000') = {track_size}")

    unknown_track_size = get_track_size("未定義コース")
    print(f"get_track_size('未定義コース') = {unknown_track_size}（未定義コースはNone）")

    print(f"Direction一覧: {[member.value for member in Direction]}")
    print(f"TrackSize一覧: {[member.value for member in TrackSize]}")


def show_race_code() -> None:
    """レースコード（race_code）モジュールの使用例を表示する.

    validate_race_code は半角数字16桁でないレースコードで KeibaDomainError を送出することを示す。
    """
    _print_section("レースコード")

    race_code = "2026111508050411"
    validate_race_code(race_code)
    print(f"extract_race_code_parts('{race_code}') = {extract_race_code_parts(race_code)}")

    try:
        validate_race_code("20261115")
    except KeibaDomainError as e:
        print(f"validate_race_code('20261115') は例外を送出: {e}")


def show_track_code() -> None:
    """トラックコード（track_code）モジュールの使用例を表示する.

    コード"00"（未設定）は None を返し、定義に無いコードでは KeibaDomainError を送出することを示す。
    """
    _print_section("トラックコード")

    print(f"turf_dirt_from_track_code('24') = {turf_dirt_from_track_code('24')}")
    print(f"race_shubetsu_from_track_code('52') = {race_shubetsu_from_track_code('52')}")
    print(f"turf_dirt_from_track_code('00') = {turf_dirt_from_track_code('00')}（未設定はNone）")

    try:
        turf_dirt_from_track_code("99")
    except KeibaDomainError as e:
        print(f"turf_dirt_from_track_code('99') は例外を送出: {e}")

    heichi_turf = get_track_codes(TurfDirt.TURF, RaceShubetsu.HEICHI)
    print(f"get_track_codes(TurfDirt.TURF, RaceShubetsu.HEICHI) = {heichi_turf}")
    print(f"get_track_codes(TurfDirt.DIRT) = {get_track_codes(TurfDirt.DIRT)}")


def show_ijo_kubun() -> None:
    """異常区分（ijo_kubun）モジュールの使用例を表示する.

    コード"0"（異常なし）は None を返し、範囲外のコードでは KeibaDomainError を送出することを示す。
    """
    _print_section("異常区分")

    print(f"ijo_kubun_from_code('4') = {ijo_kubun_from_code('4')}")
    print(f"ijo_kubun_from_code('0') = {ijo_kubun_from_code('0')}（異常なしはNone）")

    try:
        ijo_kubun_from_code("9")
    except KeibaDomainError as e:
        print(f"ijo_kubun_from_code('9') は例外を送出: {e}")

    print(f"NOT_STARTED_IJO_KUBUN_CODES = {sorted(NOT_STARTED_IJO_KUBUN_CODES)}")
    print(f"NOT_FINISHED_IJO_KUBUN_CODES = {sorted(NOT_FINISHED_IJO_KUBUN_CODES)}")
    print(f"IjoKubun一覧: {[member.value for member in IjoKubun]}")


def show_grade() -> None:
    """グレード（grade）モジュールの使用例を表示する.

    空白と"_"のコード（一般競走）は None を返し、定義に無いコードでは KeibaDomainError を
    送出することを示す。
    """
    _print_section("グレード")

    print(f"grade_from_code('A') = {grade_from_code('A')}")
    print(f"grade_from_code(' ') = {grade_from_code(' ')}（一般競走はNone）")
    print(f"grade_from_code('_') = {grade_from_code('_')}（統一スキーマの一般競走もNone）")

    try:
        grade_from_code("Z")
    except KeibaDomainError as e:
        print(f"grade_from_code('Z') は例外を送出: {e}")

    print(f"Grade一覧: {[member.value for member in Grade]}")


def main() -> None:
    """メイン処理.

    競馬場・馬場状態・距離区分・枠・コース・レースコード・トラックコード・異常区分・グレードの
    各モジュールの使用例を順に表示する。
    """
    show_keibajo()
    show_baba()
    show_distance()
    show_waku()
    show_course()
    show_race_code()
    show_track_code()
    show_ijo_kubun()
    show_grade()


def _print_section(title: str) -> None:
    """セクション見出しを表示する.

    Args:
        title (str): セクション名
    """
    print(f"\n【{title}】")


if __name__ == "__main__":
    main()
