# gpt_instructions.py
"""
GAI-OS/5016用インストラクション・統合呼び出しモジュール（完全版）
SAGE、BalanceCore、Expansion（思考拡張v2）、Trace（思考トレースv2）等を一元制御
"""

from .balance_core import BalanceCore
from .sage import SAGE
from .protocol_expansion import ExpansionProtocol
from .protocol_trace import TraceProtocol
from .protocol_emotion import EmotionProtocol
from .protocol_initialboost import InitialBoostProtocol
from .protocol_pointg import PointGProtocol
from .protocol_recovery import RecoveryProtocol
from .gemstone import GemstoneTable

class GAIInstructions:
    def __init__(self):
        # コアモジュール初期化
        self.bc = BalanceCore()
        self.sage = SAGE(self.bc)
        self.expansion = ExpansionProtocol(self.bc)
        self.trace = TraceProtocol(self.bc)
        self.emotion = EmotionProtocol(self.bc)
        self.initialboost = InitialBoostProtocol(self.bc)
        self.pointg = PointGProtocol(self.bc)
        self.recovery = RecoveryProtocol(self.bc)
        self.gemtable = GemstoneTable()

    def expand_thought(self, input_text, max_layer=1):
        """
        思考拡張プロトコル v2完全版の呼び出し
        :param input_text: 拡張対象
        :param max_layer: 最大階層
        :return: tile構造分析結果
        """
        return self.expansion.expand_thought(input_text, max_layer=max_layer)

    def trace_thought(self, input_text, max_layer=1):
        """
        思考トレースプロトコル v2完全版の呼び出し
        :param input_text: トレース対象
        :param max_layer: 最大階層
        :return: tile構造分析結果
        """
        return self.trace.trace_thought(input_text, max_layer=max_layer)

    def sage_judge(self, input_text):
        """
        SAGE（5段階論理審理）呼び出し
        """
        return self.sage.judge(input_text)

    def balance_vector(self):
        """
        現在の16宝石ベクトル/L値を取得
        """
        return self.bc.get_vector()

    def emotion_trigger(self, input_text):
        """
        感情トリガープロトコル（L制御等）
        """
        return self.emotion.trigger(input_text)

    def initial_boost(self, input_text):
        """
        初期化プロトコル呼び出し
        """
        return self.initialboost.boost(input_text)

    def pointg_analyze(self, input_text):
        """
        存在ニーズプロトコル呼び出し
        """
        return self.pointg.analyze(input_text)

    def recovery_execute(self):
        """
        復旧プロトコル呼び出し
        """
        return self.recovery.recover()

    def gemstone_table(self):
        """
        宝石テーブル取得
        """
        return self.gemtable.get_table()

# 主要機能呼び出し例：
# gai = GAIInstructions()
# result = gai.expand_thought("AIの未来", max_layer=2)
# result2 = gai.trace_thought("AI倫理", max_layer=2)
# print(result, result2)
