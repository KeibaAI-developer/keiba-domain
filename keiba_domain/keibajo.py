"""競馬場のEnumと判定関数.

中央競馬場を表すEnum・競馬場コードとの対応表・判定関数を提供する。
"""

from enum import StrEnum

from keiba_domain.exceptions import KeibaDomainError


class Keibajo(StrEnum):
    """中央競馬場を表すEnum.

    Attributes:
        SAPPORO: 札幌
        HAKODATE: 函館
        FUKUSHIMA: 福島
        NIIGATA: 新潟
        TOKYO: 東京
        NAKAYAMA: 中山
        CHUKYO: 中京
        KYOTO: 京都
        HANSHIN: 阪神
        KOKURA: 小倉
    """

    SAPPORO = "札幌"
    HAKODATE = "函館"
    FUKUSHIMA = "福島"
    NIIGATA = "新潟"
    TOKYO = "東京"
    NAKAYAMA = "中山"
    CHUKYO = "中京"
    KYOTO = "京都"
    HANSHIN = "阪神"
    KOKURA = "小倉"


# 競馬場コード→競馬場名（中央10場）
KEIBAJO_CODE_TO_NAME: dict[str, Keibajo] = {
    "01": Keibajo.SAPPORO,
    "02": Keibajo.HAKODATE,
    "03": Keibajo.FUKUSHIMA,
    "04": Keibajo.NIIGATA,
    "05": Keibajo.TOKYO,
    "06": Keibajo.NAKAYAMA,
    "07": Keibajo.CHUKYO,
    "08": Keibajo.KYOTO,
    "09": Keibajo.HANSHIN,
    "10": Keibajo.KOKURA,
}

# 中央競馬場のコード
CENTRAL_KEIBAJO_CODES: frozenset[str] = frozenset(KEIBAJO_CODE_TO_NAME.keys())

# 中央以外の競馬場コード→名称
_NON_CENTRAL_KEIBAJO_CODE_TO_NAME: dict[str, str] = {
    "30": "門別",
    "35": "盛岡",
    "36": "水沢",
    "42": "浦和",
    "43": "船橋",
    "44": "大井",
    "45": "川崎",
    "46": "金沢",
    "47": "笠松",
    "48": "名古屋",
    "50": "園田",
    "51": "姫路",
    "54": "高知",
    "55": "佐賀",
    "65": "帯広",
}

# 地方・海外を含む競馬場コード→名称（中央10場も含む）
KEIBAJO_CODE_TO_LOCAL_NAME: dict[str, str] = {
    **{code: keibajo.value for code, keibajo in KEIBAJO_CODE_TO_NAME.items()},
    **_NON_CENTRAL_KEIBAJO_CODE_TO_NAME,
}


def keibajo_from_code(code: str) -> Keibajo:
    """競馬場コードから中央競馬場を取得する.

    Args:
        code (str): 競馬場コード（例: "05"）

    Returns:
        Keibajo: 中央競馬場

    Raises:
        KeibaDomainError: codeが中央10場のコードでない場合
    """
    if code not in KEIBAJO_CODE_TO_NAME:
        raise KeibaDomainError(f"競馬場コードが不正です: {code}")
    return KEIBAJO_CODE_TO_NAME[code]


def is_central_keibajo(code: str) -> bool:
    """中央競馬場のコードかどうかを判定する.

    地方競馬場のコードと未知のコードはいずれもFalseを返す。過去成績から中央のレースだけを
    抽出する用途を想定しており、想定外のコードが1件混ざっただけで処理全体が止まらないよう
    例外は送出しない。コードそのものの妥当性を検証したい場合は keibajo_from_code を使う。

    Args:
        code (str): 競馬場コード

    Returns:
        bool: 中央競馬場のコードであればTrue
    """
    return code in CENTRAL_KEIBAJO_CODES
