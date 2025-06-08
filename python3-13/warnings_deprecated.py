# Python 3.13 新機能: warnings.deprecated() デコレータ
# - 非推奨機能の警告を簡単に発出する新しいデコレータ
# - 関数、クラス、メソッドに適用可能
# - カスタムメッセージとバージョン情報の指定

import warnings
from typing import Any, Callable, TypeVar
from functools import wraps


# Python 3.13 の warnings.deprecated() デコレータの使用例
# 注意: 実際のPython 3.13では warnings.deprecated が標準で利用可能

def deprecated(message: str = "", *, category: type[Warning] = DeprecationWarning, 
               stacklevel: int = 2) -> Callable[[Callable], Callable]:
    """
    非推奨警告デコレータ（Python 3.13の warnings.deprecated() の実装例）
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            warnings.warn(
                message or f"{func.__name__} is deprecated",
                category=category,
                stacklevel=stacklevel
            )
            return func(*args, **kwargs)
        return wrapper
    return decorator


# 関数の非推奨化
@deprecated("old_function は非推奨です。new_function を使用してください。")
def old_function(x: int, y: int) -> int:
    """古い関数（非推奨）"""
    return x + y


def new_function(x: int, y: int) -> int:
    """新しい関数（推奨）"""
    return x + y


# クラスメソッドの非推奨化
class Calculator:
    """計算機クラス"""
    
    @deprecated("add_old は非推奨です。add を使用してください。")
    def add_old(self, a: int, b: int) -> int:
        """古い加算メソッド（非推奨）"""
        return a + b
    
    def add(self, a: int, b: int) -> int:
        """新しい加算メソッド（推奨）"""
        return a + b
    
    @deprecated(
        "calculate_legacy は v2.0 で削除予定です。calculate を使用してください。",
        category=FutureWarning
    )
    def calculate_legacy(self, operation: str, a: int, b: int) -> int:
        """レガシー計算メソッド（将来削除予定）"""
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        else:
            raise ValueError("サポートされていない操作")
    
    def calculate(self, operation: str, a: int, b: int) -> int:
        """新しい計算メソッド（推奨）"""
        operations = {
            "add": lambda x, y: x + y,
            "subtract": lambda x, y: x - y,
            "multiply": lambda x, y: x * y,
            "divide": lambda x, y: x / y if y != 0 else float('inf')
        }
        
        if operation not in operations:
            raise ValueError(f"サポートされていない操作: {operation}")
        
        return operations[operation](a, b)


# クラス全体の非推奨化
@deprecated("OldDataProcessor は非推奨です。DataProcessor を使用してください。")
class OldDataProcessor:
    """古いデータプロセッサクラス（非推奨）"""
    
    def __init__(self, data: list[int]):
        self.data = data
    
    def process(self) -> int:
        return sum(self.data)


class DataProcessor:
    """新しいデータプロセッサクラス（推奨）"""
    
    def __init__(self, data: list[int]):
        self.data = data
    
    def process(self) -> dict[str, Any]:
        return {
            "sum": sum(self.data),
            "average": sum(self.data) / len(self.data) if self.data else 0,
            "count": len(self.data)
        }


# 段階的な非推奨化の例
class APIClient:
    """APIクライアントクラス"""
    
    @deprecated("get_data_v1 は非推奨です。get_data_v2 を使用してください。")
    def get_data_v1(self, endpoint: str) -> dict[str, Any]:
        """API v1 データ取得（非推奨）"""
        return {"data": f"v1 data from {endpoint}", "version": "1.0"}
    
    @deprecated(
        "get_data_v2 は v3.0 で削除予定です。get_data を使用してください。",
        category=PendingDeprecationWarning
    )
    def get_data_v2(self, endpoint: str) -> dict[str, Any]:
        """API v2 データ取得（将来非推奨）"""
        return {"data": f"v2 data from {endpoint}", "version": "2.0"}
    
    def get_data(self, endpoint: str, *, include_metadata: bool = True) -> dict[str, Any]:
        """最新の API データ取得（推奨）"""
        result = {"data": f"v3 data from {endpoint}", "version": "3.0"}
        if include_metadata:
            result["metadata"] = {"timestamp": "2024-01-01T00:00:00Z"}
        return result


# カスタム警告カテゴリ
class SecurityDeprecationWarning(DeprecationWarning):
    """セキュリティ関連の非推奨警告"""
    pass


class SecurityUtils:
    """セキュリティユーティリティクラス"""
    
    @deprecated(
        "weak_hash は安全ではありません。secure_hash を使用してください。",
        category=SecurityDeprecationWarning
    )
    def weak_hash(self, data: str) -> str:
        """弱いハッシュ関数（セキュリティ上非推奨）"""
        return str(hash(data))
    
    def secure_hash(self, data: str) -> str:
        """安全なハッシュ関数（推奨）"""
        import hashlib
        return hashlib.sha256(data.encode()).hexdigest()


# 警告フィルターの設定例
def configure_deprecation_warnings():
    """非推奨警告の設定"""
    
    # すべての非推奨警告を表示
    warnings.filterwarnings("always", category=DeprecationWarning)
    
    # セキュリティ関連の警告はエラーとして扱う
    warnings.filterwarnings("error", category=SecurityDeprecationWarning)
    
    # 特定のモジュールの警告を無視
    warnings.filterwarnings("ignore", category=DeprecationWarning, 
                          module="some_third_party_module")


def demonstrate_deprecated_usage():
    """非推奨機能の使用例とテスト"""
    
    print("=== warnings.deprecated() デコレータのデモ ===")
    print()
    
    # 警告設定
    configure_deprecation_warnings()
    
    # 非推奨関数の使用
    print("1. 非推奨関数の使用:")
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = old_function(5, 3)
        if w:
            print(f"   警告: {w[0].message}")
        print(f"   結果: {result}")
    print()
    
    # 非推奨メソッドの使用
    print("2. 非推奨メソッドの使用:")
    calc = Calculator()
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = calc.add_old(10, 5)
        if w:
            print(f"   警告: {w[0].message}")
        print(f"   結果: {result}")
    print()
    
    # 非推奨クラスの使用
    print("3. 非推奨クラスの使用:")
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        processor = OldDataProcessor([1, 2, 3, 4, 5])
        if w:
            print(f"   警告: {w[0].message}")
        result = processor.process()
        print(f"   結果: {result}")
    print()
    
    # 段階的非推奨の例
    print("4. 段階的非推奨の例:")
    client = APIClient()
    
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        
        # v1 (非推奨)
        data_v1 = client.get_data_v1("/users")
        if w:
            print(f"   v1 警告: {w[-1].message}")
        
        # v2 (将来非推奨)
        data_v2 = client.get_data_v2("/users")
        if len(w) > 1:
            print(f"   v2 警告: {w[-1].message}")
        
        # v3 (推奨)
        data_v3 = client.get_data("/users")
        
        print(f"   v1 結果: {data_v1}")
        print(f"   v2 結果: {data_v2}")
        print(f"   v3 結果: {data_v3}")
    print()
    
    # セキュリティ関連の非推奨警告
    print("5. セキュリティ関連の非推奨警告:")
    security = SecurityUtils()
    
    try:
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("error", category=SecurityDeprecationWarning)
            weak_result = security.weak_hash("password123")
    except SecurityDeprecationWarning as e:
        print(f"   セキュリティ警告がエラーに: {e}")
    
    secure_result = security.secure_hash("password123")
    print(f"   安全なハッシュ結果: {secure_result[:16]}...")
    print()


def main():
    """メイン関数"""
    demonstrate_deprecated_usage()
    
    print("注意:")
    print("- Python 3.13では warnings.deprecated() が標準で利用可能")
    print("- 実際の使用時は適切な警告フィルターを設定")
    print("- 段階的な移行計画を立てて非推奨化を実施")


if __name__ == "__main__":
    main()