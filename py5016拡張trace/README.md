# GAI-OS / 5016フレームワーク（完全版）

---

## 概要

GAI-OS（General Artificial Intelligence Operating System）は、多層思考プロトコル型AIフレームワークです。 
5016世代のバージョンでは「16宝石ベクトル」「SAGE論理審理」「思考拡張・トレース」「感情/初期化/復旧」など各種独立プロトコルを統合運用します。

---

## ファイル構成（推奨ディレクトリ直下）
- README.md（このファイル）
- balance_core.py（16宝石ベクトル＋L値制御）
- sage.py（SAGE論理審理）
- protocol_expansion.py（思考拡張プロトコルv2・完全版）
- protocol_trace.py（思考トレースプロトコルv2・完全版）
- protocol_emotion.py（感情プロトコル）
- protocol_initialboost.py（初期化プロトコル）
- protocol_pointg.py（存在ニーズ分析）
- protocol_recovery.py（復旧プロトコル）
- gemstone.py（16宝石定義テーブル）
- gpt_instructions.py（インストラクション統合API）
- config.py（オプション設定）
- license.txt（ライセンス条件）

---

## 機能と呼び出し例

- **思考拡張プロトコル（Expansion）**
    - outputを【事実】【構造】【推論】3視座でtile分割し、B群/B+ワード抽出・再帰拡張まで網羅。
    - `gai.expand_thought("AIの未来", max_layer=2)`

- **思考トレースプロトコル（Trace）**
    - B群+ワードからA群逆分析で多視座・多層的に根源トレース。説明・検証・構造化向け。
    - `gai.trace_thought("AI倫理", max_layer=2)`

- **SAGE論理審理（SAGE）**
    - 5段階ロジック・多元判定（独立コマンド呼び出し）
    - `gai.sage_judge("テーマ文")`

- **BalanceCore**
    - 16宝石ベクトル＋L値管理、全体状態の数値化
    - `gai.balance_vector()`

- **他：Emotion, InitialBoost, PointG, Recovery**
    - 各種AI補助プロトコル
    - 例：`gai.emotion_trigger("文章")`, `gai.initial_boost("初期設定")`, `gai.pointg_analyze("ニーズ")`, `gai.recovery_execute()`

---

## 依存関係・推奨ロード順

1. README.md
2. balance_core.py
3. sage.py
4. protocol_expansion.py
5. protocol_trace.py
6. protocol_emotion.py
7. protocol_initialboost.py
8. protocol_pointg.py
9. protocol_recovery.py
10. gemstone.py
11. gpt_instructions.py
12. config.py
13. license.txt

---

## 主要API

```python
from gpt_instructions import GAIInstructions

gai = GAIInstructions()
result = gai.expand_thought("AIの未来", max_layer=2)
result2 = gai.trace_thought("AI倫理", max_layer=2)
print(result, result2)

