# gai5016/protocol_pointg.py

"""
PointGプロトコル
---------------------
BalanceCoreにおける「着眼点・認知焦点の自動シフト」を担うプロトコル。
ユーザーやAIの対話中、「視点の切替」「新たな注目軸へのジャンプ」を実装し、GemstoneやL値ベクトルを動的に移行する。
"""

from .balance_core import BalanceCore

class PointGProtocol:
    """
    PointGは、BalanceCoreの「着眼点＝Gemstoneやベクトルの主軸」を動的に切替えるためのモジュール。
    """

    def __init__(self, balance_core: BalanceCore):
        self.balance_core = balance_core

    def shift_focus(self, new_focus: str):
        """
        着眼点名（例："logic", "emotion", "intuition", "fact", "harmony" など）でGemstoneを切替。
        """
        focus_map = {
            "logic": "Sapphire",
            "emotion": "Ruby",
            "intuition": "Amethyst",
            "fact": "Emerald",
            "harmony": "Emerald",
            "calm": "Jade",
            # ...他必要に応じ拡張
        }
        if new_focus in focus_map:
            self.balance_core.set_gemstone(focus_map[new_focus])
        else:
            # 未知の着眼点→Jadeへ
            self.balance_core.set_gemstone("Jade")

    # 追加仕様：着眼点履歴・変化のログも実装可

# （usage例はusage_examples.pyやREADMEに記載予定）
