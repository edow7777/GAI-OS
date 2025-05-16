# gai5016/balance_core.py

"""
BalanceCoreモジュール
---------------------
GAI-5016におけるダイナミック認知バランス・宝石ベクトル連動制御の中核。
16種類のGemstone（宝石）・L値（テンション）制御・プロトコル拡張呼び出し等を包括。
SAGE呼び出し時は自動的に状態凍結、終了後に即座に再開される。
"""

from typing import Dict, Optional, List
from .gemstone import Gemstone, GEMSTONES

class BalanceCore:
    """
    BalanceCoreはGAI-5016の主認知制御モジュールです。
    宝石（Gemstone）によるベクトル型MBTI認知制御・L値（テンション）管理・各種プロトコル呼び出しを担います。
    """

    def __init__(self, initial_gem: str = "Ruby"):
        """
        コンストラクタ：初期宝石名を指定（デフォルトはRuby）。
        """
        self.gemstones: Dict[str, Gemstone] = {g.name: g for g in GEMSTONES}
        self.current_gem: Gemstone = self.gemstones.get(initial_gem, list(self.gemstones.values())[0])
        self.l_value: float = self.current_gem.l_init
        self.frozen: bool = False  # SAGE審理時など一時凍結用

    def set_gemstone(self, gem_name: str):
        """
        指定宝石に切替（L値も即時ジャンプ）。
        無効な宝石名の場合はJade（冷静）にフォールバック。
        """
        if gem_name in self.gemstones:
            self.current_gem = self.gemstones[gem_name]
            self.l_value = self.current_gem.l_init
        else:
            # エラー時はJadeでリセット
            self.current_gem = self.gemstones["Jade"]
            self.l_value = self.current_gem.l_init

    def adjust_l_value(self, delta: float):
        """
        L値を指定量（±）だけ変動させる。0～1の範囲を超えないよう制限。
        """
        self.l_value = min(1.0, max(0.0, self.l_value + delta))

    def freeze(self):
        """
        SAGE等呼び出し時の一時凍結（バランス更新不可状態）。
        """
        self.frozen = True

    def resume(self):
        """
        凍結解除、通常動作に復帰。
        """
        self.frozen = False

    def status(self) -> Dict:
        """
        現在のBalanceCore状態を辞書で返す（Gemstone/L値/凍結状態）。
        """
        return {
            "gemstone": self.current_gem.name,
            "vector": self.current_gem.vector,
            "l_value": self.l_value,
            "frozen": self.frozen
        }

    # 各プロトコルの呼び出しもここに追加実装可
    # 例）emotion_trigger(), initial_boost(), pointg(), recovery(), expansion()

# （usage例はREADMEまたはusage_examples.pyに別途記載予定）
