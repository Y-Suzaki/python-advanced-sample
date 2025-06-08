# Python 3.13 新機能: 改善されたREPL（対話型シェル）
# - PyPyプロジェクトからの新しい対話型シェル
# - マルチライン編集とヒストリー保持
# - カラー表示とF1/F2/F3キーサポート
# - REPLコマンドの直接サポート

import sys
import os
from typing import List, Dict, Any


def demonstrate_repl_features():
    """
    Python 3.13の新しいREPL機能の説明
    （実際の対話型機能は対話モードでのみ利用可能）
    """
    
    print("=== Python 3.13 改善されたREPL機能 ===")
    print()
    
    print("1. マルチライン編集の改善:")
    print("   - 複数行のコードを自然に編集可能")
    print("   - ヒストリーが複数行にわたって保持される")
    print("   - インデントの自動調整")
    print()
    
    print("2. 新しいキーボードショートカット:")
    print("   - F1: インタラクティブヘルプブラウジング")
    print("   - F2: ヒストリーブラウジング（出力とプロンプトをスキップ）")
    print("   - F3: ペーストモード（大きなコードブロックの貼り付けが簡単）")
    print()
    
    print("3. カラー表示:")
    print("   - プロンプトとトレースバックがデフォルトでカラー表示")
    print("   - シンタックスハイライト")
    print("   - エラーメッセージの視認性向上")
    print()
    
    print("4. REPLコマンドの直接サポート:")
    print("   - help, exit, quit が関数呼び出しなしで使用可能")
    print("   - help() ではなく help で十分")
    print("   - exit() ではなく exit で十分")
    print()


def repl_command_examples():
    """REPLコマンドの使用例（説明）"""
    
    print("=== REPLコマンドの使用例 ===")
    print()
    
    commands = {
        "help": "一般的なヘルプを表示",
        "help(object)": "特定のオブジェクトのヘルプを表示",
        "exit": "Pythonインタープリターを終了",
        "quit": "Pythonインタープリターを終了",
        "copyright": "著作権情報を表示",
        "credits": "クレジット情報を表示",
        "license": "ライセンス情報を表示"
    }
    
    print("Python 3.13で直接使用可能なREPLコマンド:")
    for command, description in commands.items():
        print(f"  {command:<15} - {description}")
    print()
    
    print("使用例（対話モードで実行）:")
    print(">>> help          # ヘルプを表示（Python 3.13では括弧不要）")
    print(">>> help(list)    # listクラスのヘルプ")
    print(">>> exit          # 終了（Python 3.13では括弧不要）")
    print()


def demonstrate_multiline_support():
    """マルチライン編集のサポート例"""
    
    print("=== マルチライン編集のサポート ===")
    print()
    
    print("Python 3.13では以下のような複数行コードの編集が改善されています:")
    print()
    
    # 複数行関数の例
    multiline_function = '''
def calculate_statistics(numbers):
    if not numbers:
        return {"count": 0, "sum": 0, "average": 0}
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    return {
        "count": count,
        "sum": total,
        "average": average,
        "min": min(numbers),
        "max": max(numbers)
    }
'''
    
    print("例: 複数行関数の定義")
    print(multiline_function)
    
    # 複数行クラスの例
    multiline_class = '''
class DataProcessor:
    def __init__(self, data):
        self.data = data
        self.processed = False
    
    def process(self):
        if self.processed:
            return self.data
        
        # データ処理ロジック
        self.data = [x * 2 for x in self.data if x > 0]
        self.processed = True
        return self.data
'''
    
    print("例: 複数行クラスの定義")
    print(multiline_class)
    
    print("改善点:")
    print("- 各行の編集が容易")
    print("- インデントの自動調整")
    print("- ヒストリーが複数行単位で保存")
    print("- 部分的な編集と再実行が可能")
    print()


def color_display_examples():
    """カラー表示機能の例"""
    
    print("=== カラー表示機能 ===")
    print()
    
    print("Python 3.13では以下がカラー表示されます:")
    print()
    
    # ANSI カラーコードの例（実際の端末でのみ表示される）
    colors = {
        "プロンプト": "緑色で >>> や ... が表示",
        "文字列": "文字列リテラルが特定の色で表示",
        "キーワード": "def, class, if, for などが強調表示",
        "エラー": "エラーメッセージが赤色で表示",
        "警告": "警告メッセージが黄色で表示",
        "トレースバック": "スタックトレースが色分けされて表示"
    }
    
    for item, description in colors.items():
        print(f"  {item:<12} - {description}")
    
    print()
    print("カラー表示のメリット:")
    print("- コードの可読性向上")
    print("- エラーの早期発見")
    print("- デバッグ効率の向上")
    print("- 開発体験の向上")
    print()


def paste_mode_explanation():
    """ペーストモード（F3）の説明"""
    
    print("=== ペーストモード（F3キー） ===")
    print()
    
    print("ペーストモードの特徴:")
    print("- 大きなコードブロックの貼り付けが簡単")
    print("- インデントの自動調整")
    print("- コメントと空行の適切な処理")
    print("- 複数の関数やクラスの一括貼り付け")
    print()
    
    print("使用場面:")
    print("- 外部エディタで作成したコードのテスト")
    print("- ドキュメントからのサンプルコードの実行")
    print("- 複数ファイルからのコード断片の統合")
    print("- チュートリアルやガイドの実践")
    print()
    
    # 大きなコードブロックの例
    large_code_block = '''
# 複雑なデータ処理の例
import json
from datetime import datetime
from typing import List, Dict, Any

class AdvancedDataProcessor:
    """高度なデータ処理クラス"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.processed_count = 0
        self.errors = []
    
    def process_records(self, records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """レコードを処理"""
        results = []
        
        for record in records:
            try:
                processed_record = self._process_single_record(record)
                results.append(processed_record)
                self.processed_count += 1
            except Exception as e:
                self.errors.append({
                    "record": record,
                    "error": str(e),
                    "timestamp": datetime.now().isoformat()
                })
        
        return results
    
    def _process_single_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """単一レコードの処理"""
        # データ変換ロジック
        processed = {
            "id": record.get("id"),
            "timestamp": datetime.now().isoformat(),
            "data": record.get("data", {}),
            "status": "processed"
        }
        
        # 設定に基づく追加処理
        if self.config.get("add_metadata", False):
            processed["metadata"] = {
                "processor_version": "1.0.0",
                "processing_time": datetime.now().isoformat()
            }
        
        return processed

# 使用例
config = {"add_metadata": True}
processor = AdvancedDataProcessor(config)

sample_data = [
    {"id": 1, "data": {"name": "Alice", "value": 100}},
    {"id": 2, "data": {"name": "Bob", "value": 200}},
    {"id": 3, "data": {"name": "Charlie", "value": 300}}
]

results = processor.process_records(sample_data)
print(f"処理済みレコード数: {processor.processed_count}")
print(f"エラー数: {len(processor.errors)}")
'''
    
    print("このような大きなコードブロックがF3でスムーズに貼り付け可能:")
    print(large_code_block[:500] + "...")
    print()


def history_browsing_explanation():
    """ヒストリーブラウジング（F2）の説明"""
    
    print("=== ヒストリーブラウジング（F2キー） ===")
    print()
    
    print("F2キーによるヒストリーブラウジングの特徴:")
    print("- 出力結果をスキップしてコマンドのみ表示")
    print("- >>> や ... プロンプトも除去")
    print("- 実行したコードのみに集中できる")
    print("- 長い出力結果に邪魔されない")
    print()
    
    print("従来のヒストリー表示例:")
    print(">>> x = 10")
    print(">>> y = 20")
    print(">>> result = x + y")
    print(">>> print(result)")
    print("30")
    print(">>> print('Hello, World!')")
    print("Hello, World!")
    print()
    
    print("F2によるヒストリー表示例（改善版）:")
    print("x = 10")
    print("y = 20")
    print("result = x + y")
    print("print(result)")
    print("print('Hello, World!')")
    print()
    
    print("メリット:")
    print("- コマンドの再利用が簡単")
    print("- 過去のコードの見つけやすさ")
    print("- クリーンな表示")
    print()


def interactive_help_explanation():
    """インタラクティブヘルプ（F1）の説明"""
    
    print("=== インタラクティブヘルプ（F1キー） ===")
    print()
    
    print("F1キーによるインタラクティブヘルプの特徴:")
    print("- 独立したコマンドヒストリー")
    print("- ヘルプコンテンツの効率的なブラウジング")
    print("- メインREPLセッションを中断しない")
    print("- 検索とナビゲーション機能")
    print()
    
    print("利用可能なヘルプコンテンツ:")
    help_topics = [
        "MODULES - 利用可能なモジュール一覧",
        "KEYWORDS - Pythonキーワード",
        "SYMBOLS - 特殊記号",
        "TOPICS - 言語機能のトピック",
        "FUNCTIONS - 組み込み関数",
        "CLASSES - 組み込みクラス"
    ]
    
    for topic in help_topics:
        print(f"  - {topic}")
    
    print()
    print("使用例:")
    print("F1 → 'list' と入力 → リスト型のヘルプを表示")
    print("F1 → 'TOPICS' → 利用可能なトピック一覧")
    print("F1 → 'KEYWORDS' → Pythonキーワード一覧")
    print()


def compatibility_notes():
    """互換性に関する注意事項"""
    
    print("=== 互換性と設定に関する注意事項 ===")
    print()
    
    print("環境設定:")
    print("- カラー表示は対応端末でのみ有効")
    print("- 一部の機能は環境変数で制御可能")
    print("- 古いREPLも必要に応じて使用可能")
    print()
    
    print("環境変数:")
    env_vars = {
        "PYTHON_COLORS": "カラー表示の有効/無効",
        "PYTHONSTARTUP": "REPL起動時のスクリプト",
        "PYTHONPATH": "モジュール検索パス"
    }
    
    for var, description in env_vars.items():
        print(f"  {var:<15} - {description}")
    
    print()
    print("旧バージョンとの互換性:")
    print("- 既存のREPLスクリプトは引き続き動作")
    print("- 新機能は段階的に有効化")
    print("- カスタマイズ設定は保持される")
    print()


def main():
    """メイン関数"""
    print("Python 3.13 改善されたREPL（対話型シェル）の説明")
    print("=" * 60)
    print()
    
    demonstrate_repl_features()
    repl_command_examples()
    demonstrate_multiline_support()
    color_display_examples()
    paste_mode_explanation()
    history_browsing_explanation()
    interactive_help_explanation()
    compatibility_notes()
    
    print("まとめ:")
    print("Python 3.13のREPL改善により、対話型開発体験が大幅に向上しています。")
    print("これらの機能を活用することで、より効率的なPython開発が可能になります。")


if __name__ == "__main__":
    main()