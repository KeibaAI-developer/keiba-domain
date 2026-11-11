"""グレードのEnumと判定関数.

グレードを表すEnum・グレードコードとの対応表・判定関数を提供する。
"""

from enum import StrEnum

from keiba_domain.exceptions import KeibaDomainError


class Grade(StrEnum):
    """グレードを表すEnum.

    Attributes:
        G1: G1
        G2: G2
        G3: G3
        JUSHO: グレードの無い重賞
        TOKUBETSU: 特別競走
        J_G1: 障害のG1
        J_G2: 障害のG2
        J_G3: 障害のG3
        LISTED: リステッド競走
    """

    G1 = "G1"
    G2 = "G2"
    G3 = "G3"
    JUSHO = "重賞"
    TOKUBETSU = "特別"
    J_G1 = "J・G1"
    J_G2 = "J・G2"
    J_G3 = "J・G3"
    LISTED = "L"


# グレードコード→グレード
GRADE_CODE_TO_NAME: dict[str, Grade] = {
    "A": Grade.G1,
    "B": Grade.G2,
    "C": Grade.G3,
    "D": Grade.JUSHO,
    "E": Grade.TOKUBETSU,
    "F": Grade.J_G1,
    "G": Grade.J_G2,
    "H": Grade.J_G3,
    "L": Grade.LISTED,
}


def grade_from_code(code: str) -> Grade | None:
    """グレードコードからグレードを取得する.

    一般競走のグレードコードは半角空白で表されるため、前後の空白を除いてから判定する。

    Args:
        code (str): グレードコード（例: "A"）

    Returns:
        Grade | None: グレード。前後の空白を除いたcodeが空（一般競走）の場合はNone

    Raises:
        KeibaDomainError: codeが空でも定義済みのグレードコードでもない場合
    """
    stripped = code.strip()
    if not stripped:
        return None
    if stripped not in GRADE_CODE_TO_NAME:
        raise KeibaDomainError(f"グレードコードが不正です: {code}")
    return GRADE_CODE_TO_NAME[stripped]
