"""馬場状態のEnumと判定関数.

馬場状態を表すEnum・馬場状態コードとの対応表・判定関数を提供する。
"""

from enum import StrEnum

from keiba_domain.exceptions import KeibaDomainError


class Baba(StrEnum):
    """馬場状態を表すEnum.

    Attributes:
        GOOD: 良
        SLIGHTLY_HEAVY: 稍
        HEAVY: 重
        VERY_HEAVY: 不
    """

    GOOD = "良"
    SLIGHTLY_HEAVY = "稍"
    HEAVY = "重"
    VERY_HEAVY = "不"


# 馬場状態コード→馬場状態
BABA_CODE_TO_NAME: dict[str, Baba] = {
    "1": Baba.GOOD,
    "2": Baba.SLIGHTLY_HEAVY,
    "3": Baba.HEAVY,
    "4": Baba.VERY_HEAVY,
}


def baba_from_code(code: str) -> Baba | None:
    """馬場状態コードから馬場状態を取得する.

    Args:
        code (str): 馬場状態コード（"0"〜"4"）

    Returns:
        Baba | None: 馬場状態。コードが"0"（未設定）の場合はNone

    Raises:
        KeibaDomainError: codeが"0"〜"4"のいずれでもない場合
    """
    if code == "0":
        return None
    if code not in BABA_CODE_TO_NAME:
        raise KeibaDomainError(f"馬場状態コードが不正です: {code}")
    return BABA_CODE_TO_NAME[code]
