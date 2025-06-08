# Python 3.13 新機能: locals() の新しいセマンティクス
# - locals() の戻り値に対する変更が関数のローカル変数に反映される
# - デバッグやメタプログラミングでより柔軟な操作が可能
# - 動的な変数操作の改善

import sys
from typing import Any, Dict


def demonstrate_old_vs_new_locals():
    """Python 3.13以前と以降での locals() の動作の違い"""
    
    print("=== locals() の新しいセマンティクス ===")
    print()
    
    # ローカル変数の定義
    x = 10
    y = 20
    
    print(f"変更前: x={x}, y={y}")
    
    # locals() を取得
    local_vars = locals()
    print(f"locals()の内容: {local_vars}")
    
    # Python 3.13では、locals()の辞書を変更すると実際の変数に反映される
    local_vars['x'] = 100
    local_vars['y'] = 200
    local_vars['z'] = 300  # 新しい変数の追加
    
    print(f"locals()変更後: x={x}, y={y}")
    
    # Python 3.13では z が利用可能になる（以前のバージョンでは NameError）
    try:
        print(f"新しい変数 z: {z}")
    except NameError:
        print("z は定義されていません（Python 3.12以前の動作）")
    
    print()


def dynamic_variable_creation():
    """動的な変数作成の例"""
    
    print("=== 動的な変数作成 ===")
    
    # 変数名と値のペア
    variables = {
        'name': 'Alice',
        'age': 30,
        'email': 'alice@example.com'
    }
    
    # locals() を使って動的に変数を作成
    local_vars = locals()
    for var_name, value in variables.items():
        local_vars[var_name] = value
    
    # Python 3.13では、動的に作成された変数が使用可能
    try:
        print(f"名前: {name}")
        print(f"年齢: {age}")
        print(f"メール: {email}")
    except NameError as e:
        print(f"変数が定義されていません: {e}")
    
    print()


def debug_variable_inspector():
    """デバッグ用の変数インスペクター"""
    
    def inspect_and_modify_locals():
        """ローカル変数を検査し、必要に応じて変更する"""
        
        # サンプル変数
        username = "john_doe"
        user_id = 12345
        is_active = True
        balance = 1500.75
        
        print("デバッグ前の変数:")
        for var_name, value in locals().items():
            if not var_name.startswith('_'):
                print(f"  {var_name}: {value} ({type(value).__name__})")
        
        # デバッグ用の変数操作
        local_vars = locals()
        
        # 条件に基づく変数の変更
        if local_vars.get('balance', 0) < 1000:
            local_vars['balance'] = 1000.0
            local_vars['balance_adjusted'] = True
        
        # デバッグフラグの追加
        local_vars['debug_timestamp'] = "2024-01-01T12:00:00"
        local_vars['debug_session'] = True
        
        print("\nデバッグ後の変数:")
        for var_name, value in locals().items():
            if not var_name.startswith('_'):
                print(f"  {var_name}: {value} ({type(value).__name__})")
        
        # Python 3.13では新しく追加された変数が使用可能
        try:
            if debug_session:
                print(f"\nデバッグセッション開始時刻: {debug_timestamp}")
                if 'balance_adjusted' in locals():
                    print("残高が調整されました")
        except NameError:
            print("デバッグ変数にアクセスできません")
    
    print("=== デバッグ用変数インスペクター ===")
    inspect_and_modify_locals()
    print()


def template_engine_example():
    """テンプレートエンジンでの locals() 活用例"""
    
    print("=== テンプレートエンジンの例 ===")
    
    def render_template(template: str, **context):
        """簡単なテンプレート描画関数"""
        
        # コンテキスト変数をローカル変数として設定
        local_vars = locals()
        local_vars.update(context)
        
        # テンプレート変数の置換（簡単な例）
        import re
        
        def replace_var(match):
            var_name = match.group(1)
            return str(local_vars.get(var_name, f"{{{{ {var_name} }}}}"))
        
        # {{ variable_name }} 形式の変数を置換
        result = re.sub(r'\{\{\s*(\w+)\s*\}\}', replace_var, template)
        
        # Python 3.13では、locals()に追加された変数が利用可能
        try:
            # 追加されたコンテキスト変数をチェック
            for key, value in context.items():
                if key in locals():
                    print(f"コンテキスト変数 {key} が利用可能: {value}")
        except NameError:
            print("一部のコンテキスト変数にアクセスできません")
        
        return result
    
    # テンプレートの使用例
    template = "Hello {{ name }}! You have {{ count }} messages."
    result = render_template(template, name="Alice", count=5)
    print(f"描画結果: {result}")
    print()


def configuration_loader():
    """設定ローダーでの locals() 活用例"""
    
    print("=== 設定ローダーの例 ===")
    
    def load_config_as_variables(config_dict: Dict[str, Any]):
        """設定辞書をローカル変数として読み込む"""
        
        print("設定を変数として読み込み中...")
        
        # 既存のローカル変数
        default_timeout = 30
        default_retries = 3
        
        # 設定をローカル変数として追加
        local_vars = locals()
        for key, value in config_dict.items():
            local_vars[key] = value
        
        print("利用可能な設定変数:")
        for var_name, value in locals().items():
            if not var_name.startswith('_') and var_name not in ['config_dict', 'local_vars']:
                print(f"  {var_name}: {value}")
        
        # Python 3.13では動的に追加された設定変数が使用可能
        try:
            # 設定値を使った処理
            print(f"\nサーバー設定:")
            print(f"  ホスト: {host}")
            print(f"  ポート: {port}")
            print(f"  デバッグモード: {debug}")
            print(f"  タイムアウト: {timeout if 'timeout' in locals() else default_timeout}")
        except NameError as e:
            print(f"設定変数にアクセスできません: {e}")
    
    # 設定例
    config = {
        'host': 'localhost',
        'port': 8080,
        'debug': True,
        'timeout': 60,
        'max_connections': 100
    }
    
    load_config_as_variables(config)
    print()


def metaprogramming_example():
    """メタプログラミングでの locals() 活用例"""
    
    print("=== メタプログラミングの例 ===")
    
    def create_class_methods():
        """動的にクラスメソッドを作成"""
        
        # メソッド定義のテンプレート
        methods = {
            'get_name': lambda self: getattr(self, '_name', 'Unknown'),
            'set_name': lambda self, name: setattr(self, '_name', name),
            'get_age': lambda self: getattr(self, '_age', 0),
            'set_age': lambda self, age: setattr(self, '_age', age)
        }
        
        # ローカル変数としてメソッドを定義
        local_vars = locals()
        for method_name, method_func in methods.items():
            local_vars[method_name] = method_func
        
        # 動的クラス作成
        class DynamicPerson:
            def __init__(self, name: str = "", age: int = 0):
                self._name = name
                self._age = age
        
        # Python 3.13では、locals()に追加されたメソッドが利用可能
        try:
            # メソッドをクラスに追加
            for method_name in methods.keys():
                if method_name in locals():
                    setattr(DynamicPerson, method_name, locals()[method_name])
            
            # クラスのテスト
            person = DynamicPerson()
            person.set_name("Bob")
            person.set_age(25)
            
            print(f"動的クラスのテスト:")
            print(f"  名前: {person.get_name()}")
            print(f"  年齢: {person.get_age()}")
            
        except NameError as e:
            print(f"メソッドにアクセスできません: {e}")
    
    create_class_methods()
    print()


def main():
    """メイン関数"""
    print("Python 3.13 locals() の新しいセマンティクス デモ")
    print("=" * 60)
    print()
    
    demonstrate_old_vs_new_locals()
    dynamic_variable_creation()
    debug_variable_inspector()
    template_engine_example()
    configuration_loader()
    metaprogramming_example()
    
    print("注意:")
    print("- このコードはPython 3.13の新機能を示しています")
    print("- 古いバージョンでは一部の機能が動作しない可能性があります")
    print("- locals()の変更は関数スコープ内でのみ有効です")


if __name__ == "__main__":
    main()