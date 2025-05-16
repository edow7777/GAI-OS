"""
GAI-5016 Expansion Protocol v2（思考拡張・完全版）
-----------------------------------------------
A群（事実・構造・推論）でoutputを多視座・多層分析し、B群/B群+/B+抽出、tile分割、
追記・再帰拡張など全プロセスを網羅的に実装。
"""

class ExpansionProtocol:
    def __init__(self, bc=None):
        """
        :param bc: BalanceCore等の連携モジュールインスタンス（未使用可）
        """
        self.bc = bc

    def expand_thought(self, input_text, max_layer=1):
        """
        階層思考拡張プロセス（ラベル付・tile分割・追記再帰すべて含む）

        :param input_text: 拡張対象テキスト
        :param max_layer: 最大拡張階層（デフォルト1、任意深度で再帰可能）
        :return: 全tile情報を含むリスト
        """
        results = []
        layer_input = input_text
        for layer in range(max_layer):
            # 1. A群分析
            a_group_analysis = self.analyze_a_group(layer_input)

            # 2. B群＋抽出＋タグ付与
            b_group, counter_words, tags = self.extract_b_group(a_group_analysis)

            # 3. B+選出＋理由付与
            b_plus, reason = self.select_b_plus(b_group, tags)

            # 4. tile生成
            tile = {
                "layer": layer,
                "input": layer_input,
                "A_group": a_group_analysis,
                "B_group": b_group,
                "B_group_tags": tags,
                "Counter_words": counter_words,
                "B+": b_plus,
                "B+_reason": reason,
                "追記": f"【追記：{','.join(b_group + counter_words)}】"
            }
            results.append(tile)

            # 5. 次階層入力はB+ワード（拡張連鎖）
            layer_input = b_plus
        return results

    def analyze_a_group(self, text):
        """
        A群＝事実・構造・推論の多視座ラベル付き分析
        実際にはAIプロンプト等での分析を想定（ダミー実装）
        """
        return {
            "事実": f"「{text}」の事実視座分析",
            "構造": f"「{text}」の構造視座分析",
            "推論": f"「{text}」の推論視座分析"
        }

    def extract_b_group(self, a_group_analysis):
        """
        B群＝分析結果から2ワード抽出＋カウンターワード（便宜上固定値。AIなら分析結果で動的抽出）
        それぞれ優勢/劣勢タグを付与
        """
        b_group = ["応用範囲", "限定性"]
        counter_words = ["新規発展性"]
        tags = ["優勢", "劣勢"]
        return b_group, counter_words, tags

    def select_b_plus(self, b_group, tags):
        """
        B+（最長射程ワード）の判定。優勢タグのうち最も射程が広いものをB+に選出
        """
        for b, tag in zip(b_group, tags):
            if tag == "優勢":
                reason = f"{b}は応用範囲が広いためB+（最長射程）"
                return b, reason
        # デフォルト
        return b_group[0], f"{b_group[0]}（デフォルトB+）"

    def explain_full_process(self, input_text):
        """
        拡張プロセス全体の説明＋出力例（説明用。API運用時は不要）
        """
        print("【思考拡張プロトコル v2 フルプロセス実行例】")
        results = self.expand_thought(input_text, max_layer=2)
        for tile in results:
            print(f"--- レイヤー{tile['layer']} ---")
            print(f"入力: {tile['input']}")
            print(f"A群分析: {tile['A_group']}")
            print(f"B群: {tile['B_group']}（タグ: {tile['B_group_tags']}）")
            print(f"カウンターワード: {tile['Counter_words']}")
            print(f"B+: {tile['B+']}（理由: {tile['B+_reason']}）")
            print(tile["追記"])
        print("--- END ---")
# （usage例はusage_examples.pyやREADMEに記載予定）
