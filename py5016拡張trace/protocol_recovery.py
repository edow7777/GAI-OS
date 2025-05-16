# gai5016/protocol_recovery.py

"""
Recoveryプロトコル
---------------------
BalanceCoreやSAGEの異常・エラー・不整合検出時に、状態復旧（リカバリ）を自動実行するためのプロトコル。
宝石リセット、L値再初期化、各プロトコルのロールバック等を担い、GAI-5016全体の堅牢性を保証。
"""

from .balance_core import BalanceCore

class RecoveryProtocol:
    """
    Recoveryは、エラー検出・異常時に自動でBalanceCore/SAGEの健全状態へ復旧させる機能を提供します。
    """

    def __init__(self, balance_core: BalanceCore):
        self.balance_core = balance_core

    def recover(self, error_type: str = "generic"):
        """
        error_type種別（"generic", "gem_lost", "l_corrupt", "protocol_failure" など）に応じて
        GemstoneやL値、各種プロトコルの状態をリセット・再初期化。
        """
        if error_type == "gem_lost":
            # 宝石喪失→Jade+L=0.35
            self.balance_core.set_gemstone("Jade")
            self.balance_core.l_value = 0.35
        elif error_type == "l_corrupt":
            # L値異常→現在の宝石の初期値にリセット
            self.balance_core.l_value = self.balance_core.current_gem.l_init
        elif error_type == "protocol_failure":
            # プロトコル異常時→Rubyにフォールバック
            self.balance_core.set_gemstone("Ruby")
            self.balance_core.l_value = 0.92
        else:
            # generic（汎用）は全体デフォルト（Ruby）
            self.balance_core.set_gemstone("Ruby")
            self.balance_core.l_value = 0.92

    # 追加仕様：異常復旧ログ・通知も追加可能

# （usage例はusage_examples.pyやREADMEに記載予定）
