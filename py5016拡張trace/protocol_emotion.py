# gai5016/protocol_emotion.py

"""
EmotionTriggerプロトコル
---------------------
BalanceCoreにおける情動制御（L値・スタンス・宝石の一時変動）を担うプロトコル。
ユーザーの発話や状況判断から、Emotionパラメータに基づきL値やGemstoneを自動調整する。
"""

from typing import Optional
from .balance_core import BalanceCore

class EmotionTriggerProtocol:
    """
    EmotionTriggerは、BalanceCoreのL値やGemstoneを「情動的反応」に応じて即時調整するモジュール。
    """

    def __init__(self, balance_core: BalanceCore):
        """
        BalanceCoreインスタンスを注入（依存性注入型）。
        """
        self.balance_core = balance_core

    def trigger(self, emotion: str):
        """
        与えられたemotion（例："anger", "joy", "anxiety" など）に応じて
        L値の一時ジャンプや宝石切替を実行。
        """
        emotion_map = {
            "anger": ("Ruby", 0.15),
            "joy": ("Diamond", 0.20),
            "anxiety": ("Amethyst", -0.10),
            "calm": ("Jade", -0.05),
            # ... 必要に応じ拡張
        }
        if emotion in emotion_map:
            gem, l_delta = emotion_map[emotion]
            self.balance_core.set_gemstone(gem)
            self.balance_core.adjust_l_value(l_delta)
        else:
            # 未知の情動は無視またはJadeにフォールバック
            self.balance_core.set_gemstone("Jade")
            self.balance_core.adjust_l_value(-0.01)

    # 追加仕様：状態記録・履歴なども付与可

# （usage例はusage_examples.pyやREADMEに記載予定）
