# gai5016/protocol_initialboost.py

"""
InitialBoostプロトコル
---------------------
BalanceCoreの初期化や再起動時に、特定のL値・宝石・ベクトル構造へ一括ジャンプさせるための初期ブースト設定を担うプロトコル。
セッション開始時や宝石リセット時など「状態の起点」を保証する。
"""

from .balance_core import BalanceCore

class InitialBoostProtocol:
    """
    InitialBoostは、BalanceCoreの状態を特定の初期値セットに即時リセットする機能を提供します。
    """

    def __init__(self, balance_core: BalanceCore):
        self.balance_core = balance_core

    def apply_boost(self, preset: str = "default"):
        """
        preset種別（"default", "creative", "calm" など）に応じたブースト初期化。
        - default: Ruby+L=0.92
        - creative: Amethyst+L=0.15
        - calm: Jade+L=0.35
        必要に応じて拡張可。
        """
        if preset == "creative":
            self.balance_core.set_gemstone("Amethyst")
            self.balance_core.l_value = 0.15
        elif preset == "calm":
            self.balance_core.set_gemstone("Jade")
            self.balance_core.l_value = 0.35
        else:
            # default
            self.balance_core.set_gemstone("Ruby")
            self.balance_core.l_value = 0.92

    # 追加：プロトコル適用履歴・状態記録も設計可

# （usage例はusage_examples.pyやREADMEに記載予定）
