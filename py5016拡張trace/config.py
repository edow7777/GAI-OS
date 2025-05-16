# gai5016/config.py

"""
Config（定数・初期設定）モジュール
---------------------
GAI-5016全体で共通利用される初期設定値・システム定数・バージョン管理・
主要ファイルパスなどを一元管理します。
他モジュールからimportして参照・再利用可能。
"""

# バージョン情報
GAI_VERSION = "GAI-5016"
GAI_RELEASE_DATE = "2025-05-16"

# 宝石の標準リスト（名称のみ）
GEMSTONE_NAMES = [
    "Ruby", "Sapphire", "Emerald", "Jade", "Amethyst", "Onyx",
    "Diamond", "Topaz", "Opal", "Pearl", "Garnet", "Turquoise",
    "Aquamarine", "Citrine", "Lapis", "Quartz"
]

# L値の許容範囲
L_VALUE_MIN = 0.00
L_VALUE_MAX = 1.00

# プロトコルのデフォルト設定例
DEFAULT_PROTOCOL = "Expansion"
DEFAULT_INITIAL_GEM = "Ruby"

# SAGE構造・議会フェーズ名
SAGE_PHASES = [
    "SEPHIROT", "AEON", "LIBER", "FACTCHECK", "ATARAXIA"
]

# 主要ファイル・ディレクトリ名
DATA_DIR = "./gai5016_data/"
LOG_FILE = DATA_DIR + "gai_operation.log"

# 他、必要に応じ追加

# 使用例：from .config import GAI_VERSION, GEMSTONE_NAMES
