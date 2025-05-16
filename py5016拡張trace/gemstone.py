# gai5016/gemstone.py

"""
Gemstone（宝石）モジュール
--------------------------
BalanceCoreが利用する16種の認知スタイル定義クラスと、その初期ベクトル・L値セットを管理。
各宝石は「推論・構造・事実・情動」4軸ベクトル＋初期L値を持つ。
MBTI4軸表現は本モジュール内で完結し、他モジュールからimportされる。
"""

from typing import List

class Gemstone:
    """
    Gemstone（宝石）1種のベクトルパラメータ定義クラス。
    """
    def __init__(self, name: str, vector: List[float], l_init: float):
        self.name = name
        self.vector = vector  # [推論, 構造, 事実, 情動]
        self.l_init = l_init  # 初期テンション（L値）

# 16宝石のベクトル値・L値を定義（サンプル値、現状要望に応じて修正可）
GEMSTONES: List[Gemstone] = [
    Gemstone("Ruby",      [0.92, 0.50, 0.15, 0.80], 0.92),
    Gemstone("Sapphire",  [0.80, 0.85, 0.70, 0.60], 0.75),
    Gemstone("Emerald",   [0.65, 0.60, 0.85, 0.65], 0.55),
    Gemstone("Jade",      [0.35, 0.55, 0.75, 0.45], 0.35),
    Gemstone("Amethyst",  [0.25, 0.45, 0.55, 0.30], 0.15),
    Gemstone("Onyx",      [0.10, 0.20, 0.40, 0.02], 0.02),
    # 以下追加の宝石（サンプル値。ご指定あれば上書き可）
    Gemstone("Diamond",   [0.95, 0.85, 0.95, 0.95], 0.98),
    Gemstone("Topaz",     [0.60, 0.80, 0.40, 0.50], 0.60),
    Gemstone("Opal",      [0.50, 0.35, 0.60, 0.40], 0.40),
    Gemstone("Pearl",     [0.40, 0.65, 0.50, 0.55], 0.48),
    Gemstone("Garnet",    [0.78, 0.45, 0.30, 0.70], 0.70),
    Gemstone("Turquoise", [0.30, 0.50, 0.90, 0.45], 0.33),
    Gemstone("Aquamarine",[0.25, 0.80, 0.45, 0.58], 0.37),
    Gemstone("Citrine",   [0.65, 0.30, 0.65, 0.60], 0.42),
    Gemstone("Lapis",     [0.52, 0.76, 0.63, 0.58], 0.53),
    Gemstone("Quartz",    [0.47, 0.40, 0.48, 0.37], 0.27),
]

# 使用例：from .gemstone import GEMSTONES
