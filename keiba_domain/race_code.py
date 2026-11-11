"""レースコードの検証と分解.

16桁レースコード（年 + 月日 + 競馬場コード + 回 + 日目 + R）の形式の検証と、
各要素への分解を提供する。
"""

import re

from keiba_domain.exceptions import KeibaDomainError

# レースコードの桁数
RACE_CODE_LENGTH: int = 16

# `$` は文字列末尾の改行の直前にも一致するため、アンカーを使わず fullmatch で判定する
_RACE_CODE_PATTERN = re.compile(rf"[0-9]{{{RACE_CODE_LENGTH}}}")


def validate_race_code(race_code: str) -> None:
    """16桁レースコードの形式を検証する.

    半角数字16桁だけを正しい形式とする。全角数字や前後の空白・改行を含むものは不正とする。

    Args:
        race_code (str): 16桁レースコード

    Raises:
        KeibaDomainError: 半角数字16桁でない場合
    """
    if not _RACE_CODE_PATTERN.fullmatch(race_code):
        raise KeibaDomainError(f"レースコードは半角数字16桁である必要があります: {race_code!r}")


def extract_race_code_parts(race_code: str) -> dict[str, str]:
    """レースコードから各要素を抽出する.

    Args:
        race_code (str): 16桁レースコード

    Returns:
        dict[str, str]: 各要素を含む辞書
            - 年: 開催年（4桁）
            - 月日: 開催月日（4桁）
            - 競馬場コード: 競馬場コード（2桁）
            - 回: 開催回（2桁）
            - 日目: 開催日目（2桁）
            - R: レース番号（2桁）

    Raises:
        KeibaDomainError: レースコードの形式が不正な場合
    """
    validate_race_code(race_code)
    return {
        "年": race_code[0:4],
        "月日": race_code[4:8],
        "競馬場コード": race_code[8:10],
        "回": race_code[10:12],
        "日目": race_code[12:14],
        "R": race_code[14:16],
    }
