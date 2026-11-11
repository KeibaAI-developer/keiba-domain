"""異常区分のEnumと判定関数.

異常区分を表すEnum・異常区分コードとの対応表・判定関数を提供する。
"""

from enum import StrEnum

from keiba_domain.exceptions import KeibaDomainError


class IjoKubun(StrEnum):
    """異常区分を表すEnum.

    Attributes:
        SHUSSO_TORIKESHI: 出走取消
        HASSO_JOGAI: 発走除外
        KYOSO_JOGAI: 競走除外
        KYOSO_CHUSHI: 競走中止
        SHIKKAKU: 失格
        RAKUBA_SAIKIJO: 落馬再騎乗
        KOCHAKU: 降着
    """

    SHUSSO_TORIKESHI = "出走取消"
    HASSO_JOGAI = "発走除外"
    KYOSO_JOGAI = "競走除外"
    KYOSO_CHUSHI = "競走中止"
    SHIKKAKU = "失格"
    RAKUBA_SAIKIJO = "落馬再騎乗"
    KOCHAKU = "降着"


# 異常区分コード→異常区分
IJO_KUBUN_CODE_TO_NAME: dict[str, IjoKubun] = {
    "1": IjoKubun.SHUSSO_TORIKESHI,
    "2": IjoKubun.HASSO_JOGAI,
    "3": IjoKubun.KYOSO_JOGAI,
    "4": IjoKubun.KYOSO_CHUSHI,
    "5": IjoKubun.SHIKKAKU,
    "6": IjoKubun.RAKUBA_SAIKIJO,
    "7": IjoKubun.KOCHAKU,
}

# 出走しなかった馬の異常区分
_NOT_STARTED: frozenset[IjoKubun] = frozenset(
    {IjoKubun.SHUSSO_TORIKESHI, IjoKubun.HASSO_JOGAI, IjoKubun.KYOSO_JOGAI}
)

# 出走しなかった馬の異常区分コード（出走取消・発走除外・競走除外）
NOT_STARTED_IJO_KUBUN_CODES: frozenset[str] = frozenset(
    code for code, ijo_kubun in IJO_KUBUN_CODE_TO_NAME.items() if ijo_kubun in _NOT_STARTED
)

# 完走しなかった馬の異常区分コード（出走しなかった馬と競走中止）。
# 失格は走り切った上で着順を取り消される区分のため含めない
NOT_FINISHED_IJO_KUBUN_CODES: frozenset[str] = frozenset(
    code
    for code, ijo_kubun in IJO_KUBUN_CODE_TO_NAME.items()
    if ijo_kubun in _NOT_STARTED or ijo_kubun == IjoKubun.KYOSO_CHUSHI
)


def ijo_kubun_from_code(code: str) -> IjoKubun | None:
    """異常区分コードから異常区分を取得する.

    Args:
        code (str): 異常区分コード（"0"〜"7"）

    Returns:
        IjoKubun | None: 異常区分。コードが"0"（異常なし）の場合はNone

    Raises:
        KeibaDomainError: codeが"0"〜"7"のいずれでもない場合
    """
    if code == "0":
        return None
    if code not in IJO_KUBUN_CODE_TO_NAME:
        raise KeibaDomainError(f"異常区分コードが不正です: {code}")
    return IJO_KUBUN_CODE_TO_NAME[code]
