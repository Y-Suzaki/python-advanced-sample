# Python 3.13 新機能: 改善されたエラーハンドリング
# - カラフルなトレースバック表示
# - より詳細で有用なエラーメッセージ
# - インポートエラーの改善された診断
# - 関数呼び出し時の引数エラーメッセージの改善

import sys
import traceback
from typing import Any


def demonstrate_import_error_improvements():
    """インポートエラーの改善されたメッセージをデモ"""
    try:
        # 存在しないモジュールをインポート
        import nonexistent_module
    except ImportError as e:
        print("=== インポートエラーの改善 ===")
        print(f"エラー: {e}")
        print("Python 3.13では、より詳細な診断情報が表示されます")
        print()


def demonstrate_function_argument_errors():
    """関数引数エラーの改善されたメッセージをデモ"""
    
    def example_function(name: str, age: int, email: str, active: bool = True):
        return f"{name} is {age} years old"
    
    print("=== 関数引数エラーの改善 ===")
    
    try:
        # 間違ったキーワード引数
        example_function(name="Alice", age=30, emai="alice@example.com")  # typo: emai
    except TypeError as e:
        print(f"間違ったキーワード引数のエラー: {e}")
        print("Python 3.13では、正しい引数名の候補が提案されます")
        print()
    
    try:
        # 不足している必須引数
        example_function(name="Bob", age=25)  # email が不足
    except TypeError as e:
        print(f"不足している引数のエラー: {e}")
        print()


def demonstrate_colorful_traceback():
    """カラフルなトレースバックのデモ"""
    
    def level_3():
        raise ValueError("これは深いレベルでのエラーです")
    
    def level_2():
        level_3()
    
    def level_1():
        level_2()
    
    print("=== カラフルなトレースバック ===")
    try:
        level_1()
    except ValueError as e:
        print("Python 3.13では、トレースバックがカラー表示されます:")
        # 実際のカラー表示は端末環境に依存
        traceback.print_exc()
        print()


def demonstrate_better_attribute_errors():
    """属性エラーの改善されたメッセージをデモ"""
    
    class Person:
        def __init__(self, name: str, age: int):
            self.name = name
            self.age = age
        
        def get_info(self):
            return f"{self.name} is {self.age} years old"
    
    print("=== 属性エラーの改善 ===")
    
    person = Person("Alice", 30)
    
    try:
        # 存在しない属性にアクセス
        print(person.nam)  # typo: nam instead of name
    except AttributeError as e:
        print(f"属性エラー: {e}")
        print("Python 3.13では、類似した属性名が提案されます")
        print()
    
    try:
        # 存在しないメソッドを呼び出し
        person.get_information()  # typo: get_information instead of get_info
    except AttributeError as e:
        print(f"メソッドエラー: {e}")
        print("Python 3.13では、類似したメソッド名が提案されます")
        print()


def demonstrate_name_error_improvements():
    """NameError の改善されたメッセージをデモ"""
    
    print("=== NameError の改善 ===")
    
    # 正しい変数名
    message = "Hello, World!"
    
    try:
        # 変数名のタイプミス
        print(mesage)  # typo: mesage instead of message
    except NameError as e:
        print(f"変数名エラー: {e}")
        print("Python 3.13では、類似した変数名が提案されます")
        print()


def demonstrate_exception_group_improvements():
    """ExceptionGroup の改善されたメッセージをデモ"""
    
    print("=== ExceptionGroup の改善 ===")
    
    def create_multiple_errors():
        errors = []
        
        try:
            1 / 0
        except ZeroDivisionError as e:
            errors.append(e)
        
        try:
            int("invalid")
        except ValueError as e:
            errors.append(e)
        
        try:
            [][0]
        except IndexError as e:
            errors.append(e)
        
        if errors:
            raise ExceptionGroup("複数のエラーが発生しました", errors)
    
    try:
        create_multiple_errors()
    except* ZeroDivisionError as eg:
        print("ゼロ除算エラーを処理:")
        for error in eg.exceptions:
            print(f"  - {error}")
    except* ValueError as eg:
        print("値エラーを処理:")
        for error in eg.exceptions:
            print(f"  - {error}")
    except* IndexError as eg:
        print("インデックスエラーを処理:")
        for error in eg.exceptions:
            print(f"  - {error}")
    
    print()


class CustomErrorWithDetails(Exception):
    """詳細情報付きのカスタム例外クラス"""
    
    def __init__(self, message: str, error_code: int, context: dict[str, Any]):
        super().__init__(message)
        self.error_code = error_code
        self.context = context
    
    def __str__(self):
        context_str = ", ".join(f"{k}={v}" for k, v in self.context.items())
        return f"{super().__str__()} (Code: {self.error_code}, Context: {context_str})"


def demonstrate_enhanced_custom_exceptions():
    """カスタム例外の詳細表示デモ"""
    
    print("=== カスタム例外の詳細表示 ===")
    
    try:
        raise CustomErrorWithDetails(
            "データ処理中にエラーが発生しました",
            error_code=4001,
            context={"file": "data.csv", "line": 42, "user_id": "user123"}
        )
    except CustomErrorWithDetails as e:
        print(f"カスタムエラー: {e}")
        print(f"エラーコード: {e.error_code}")
        print(f"コンテキスト: {e.context}")
        print()


def main():
    """メイン関数 - すべてのエラーハンドリング改善をデモ"""
    
    print("Python 3.13 エラーハンドリング改善のデモ")
    print("=" * 50)
    print()
    
    demonstrate_import_error_improvements()
    demonstrate_function_argument_errors()
    demonstrate_colorful_traceback()
    demonstrate_better_attribute_errors()
    demonstrate_name_error_improvements()
    demonstrate_exception_group_improvements()
    demonstrate_enhanced_custom_exceptions()
    
    print("注意: 実際のカラー表示や詳細なエラーメッセージは")
    print("Python 3.13 の実行環境で確認できます。")


if __name__ == "__main__":
    main()