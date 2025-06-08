"""
Python 3.12 新機能: TypedDict with Unpack

概要:
- Python 3.12では、TypedDict と Unpack の組み合わせが改善されました
- 関数の引数にTypeдDictの構造を直接適用可能
- 型安全なキーワード引数の処理が可能
- **kwargs の型を明確に指定できる

主な特徴:
1. TypedDict の構造を関数引数の型として使用
2. Unpack[TypedDict] による型安全なキーワード引数
3. 部分的な TypedDict の使用（Required, NotRequired）
4. ネストした TypedDict の処理
5. 動的な引数検証の改善

利点:
- 型安全性の向上
- APIの明確な定義
- 自動補完の改善
- ランタイムエラーの削減
"""

from typing import TypedDict, Unpack, Required, NotRequired, Any, Dict, List
from dataclasses import dataclass
import json

print("=" * 60)
print("TypedDict with Unpack のサンプル")
print("=" * 60)

# 1. 基本的なTypedDictとUnpackの使用例
class PersonInfo(TypedDict):
    name: str
    age: int
    email: str

class AddressInfo(TypedDict):
    street: str
    city: str
    postal_code: str
    country: str

def create_person(**kwargs: Unpack[PersonInfo]) -> PersonInfo:
    """型安全な人物情報作成関数"""
    # 型チェッカーがキーワード引数を検証
    return kwargs

def create_address(**kwargs: Unpack[AddressInfo]) -> AddressInfo:
    """型安全な住所情報作成関数"""
    return kwargs

# 2. Required と NotRequired を使用した柔軟なTypedDict
class UserProfile(TypedDict):
    username: Required[str]  # 必須フィールド
    email: Required[str]     # 必須フィールド
    age: NotRequired[int]    # オプションフィールド
    bio: NotRequired[str]    # オプションフィールド
    avatar_url: NotRequired[str]  # オプションフィールド

def create_user_profile(**kwargs: Unpack[UserProfile]) -> UserProfile:
    """ユーザープロファイル作成（必須・オプション項目混在）"""
    # デフォルト値の設定
    profile: UserProfile = {
        'username': kwargs['username'],
        'email': kwargs['email']
    }
    
    # オプション項目の追加
    if 'age' in kwargs:
        profile['age'] = kwargs['age']
    if 'bio' in kwargs:
        profile['bio'] = kwargs['bio']
    if 'avatar_url' in kwargs:
        profile['avatar_url'] = kwargs['avatar_url']
    
    return profile

# 3. ネストしたTypedDictの例
class ContactInfo(TypedDict):
    phone: str
    email: str

class CompanyInfo(TypedDict):
    name: str
    department: str
    contact: ContactInfo

class EmployeeData(TypedDict):
    employee_id: int
    personal: PersonInfo
    company: CompanyInfo

def create_employee(**kwargs: Unpack[EmployeeData]) -> EmployeeData:
    """従業員データ作成（ネストした構造）"""
    return kwargs

# 4. 複数のTypedDictを組み合わせる例
class ProductBasicInfo(TypedDict):
    name: str
    price: float
    category: str

class ProductDetails(TypedDict):
    description: str
    specifications: Dict[str, Any]
    in_stock: bool

class ProductFull(ProductBasicInfo, ProductDetails):
    """継承によるTypedDictの結合"""
    product_id: str
    created_at: str

def create_product(**kwargs: Unpack[ProductFull]) -> ProductFull:
    """完全な商品情報作成"""
    return kwargs

# 5. 動的な設定管理の例
class DatabaseConfig(TypedDict):
    host: str
    port: int
    database: str
    username: str
    password: str

class CacheConfig(TypedDict):
    redis_url: str
    ttl: int
    max_connections: int

class AppConfig(TypedDict):
    debug: bool
    secret_key: str
    database: DatabaseConfig
    cache: CacheConfig

def configure_database(**kwargs: Unpack[DatabaseConfig]) -> str:
    """データベース接続文字列生成"""
    return f"postgresql://{kwargs['username']}:{kwargs['password']}@{kwargs['host']}:{kwargs['port']}/{kwargs['database']}"

def configure_cache(**kwargs: Unpack[CacheConfig]) -> Dict[str, Any]:
    """キャッシュ設定生成"""
    return {
        'url': kwargs['redis_url'],
        'ttl': kwargs['ttl'],
        'pool_size': kwargs['max_connections']
    }

# 6. APIレスポンス処理の例
class ApiResponse(TypedDict):
    status: str
    message: str
    data: Any

class UserApiResponse(ApiResponse):
    data: PersonInfo

class ErrorResponse(TypedDict):
    error_code: str
    error_message: str
    details: NotRequired[Dict[str, Any]]

def handle_api_response(**kwargs: Unpack[ApiResponse]) -> str:
    """API レスポンス処理"""
    if kwargs['status'] == 'success':
        return f"成功: {kwargs['message']}"
    else:
        return f"エラー: {kwargs['message']}"

def handle_error_response(**kwargs: Unpack[ErrorResponse]) -> str:
    """エラーレスポンス処理"""
    error_msg = f"エラーコード: {kwargs['error_code']}, メッセージ: {kwargs['error_message']}"
    if 'details' in kwargs:
        error_msg += f", 詳細: {kwargs['details']}"
    return error_msg

# 7. バリデーション機能付きの例
class FormData(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: int

def validate_and_create_form(**kwargs: Unpack[FormData]) -> FormData | str:
    """フォームデータのバリデーションと作成"""
    # 基本的なバリデーション
    if not kwargs['first_name'].strip():
        return "名前が入力されていません"
    
    if not kwargs['last_name'].strip():
        return "姓が入力されていません"
    
    if '@' not in kwargs['email']:
        return "有効なメールアドレスを入力してください"
    
    if kwargs['age'] < 0 or kwargs['age'] > 150:
        return "年齢は0-150の範囲で入力してください"
    
    return kwargs

# デモンストレーション関数群
def demonstrate_basic_usage():
    print("1. 基本的な使用例")
    print("-" * 30)
    
    # 正しい引数で人物情報を作成
    person = create_person(
        name="田中太郎",
        age=30,
        email="tanaka@example.com"
    )
    print(f"人物情報: {person}")
    
    # 住所情報を作成
    address = create_address(
        street="1-2-3 Example Street",
        city="Tokyo",
        postal_code="100-0001",
        country="Japan"
    )
    print(f"住所情報: {address}")

def demonstrate_required_not_required():
    print("\n2. Required/NotRequired の使用例")
    print("-" * 30)
    
    # 必須項目のみ
    user1 = create_user_profile(
        username="alice",
        email="alice@example.com"
    )
    print(f"基本ユーザー: {user1}")
    
    # オプション項目も含む
    user2 = create_user_profile(
        username="bob",
        email="bob@example.com",
        age=25,
        bio="Python developer"
    )
    print(f"詳細ユーザー: {user2}")

def demonstrate_nested_typeddict():
    print("\n3. ネストしたTypedDictの使用例")
    print("-" * 30)
    
    employee = create_employee(
        employee_id=12345,
        personal={
            'name': '佐藤花子',
            'age': 28,
            'email': 'sato@company.com'
        },
        company={
            'name': 'テクノロジー株式会社',
            'department': '開発部',
            'contact': {
                'phone': '03-1234-5678',
                'email': 'dev@company.com'
            }
        }
    )
    print(f"従業員データ: {json.dumps(employee, ensure_ascii=False, indent=2)}")

def demonstrate_product_management():
    print("\n4. 商品管理システムの例")
    print("-" * 30)
    
    product = create_product(
        product_id="PROD-001",
        name="ノートパソコン",
        price=89800.00,
        category="Electronics",
        description="高性能なノートパソコン",
        specifications={
            "CPU": "Intel Core i7",
            "RAM": "16GB",
            "Storage": "512GB SSD"
        },
        in_stock=True,
        created_at="2024-01-01T00:00:00Z"
    )
    print(f"商品情報: {json.dumps(product, ensure_ascii=False, indent=2)}")

def demonstrate_configuration():
    print("\n5. 設定管理の例")
    print("-" * 30)
    
    # データベース設定
    db_connection = configure_database(
        host="localhost",
        port=5432,
        database="myapp",
        username="user",
        password="password"
    )
    print(f"DB接続文字列: {db_connection}")
    
    # キャッシュ設定
    cache_config = configure_cache(
        redis_url="redis://localhost:6379",
        ttl=3600,
        max_connections=10
    )
    print(f"キャッシュ設定: {cache_config}")

def demonstrate_api_handling():
    print("\n6. API レスポンス処理の例")
    print("-" * 30)
    
    # 成功レスポンス
    success_response = handle_api_response(
        status="success",
        message="データが正常に取得されました",
        data={"id": 1, "name": "test"}
    )
    print(success_response)
    
    # エラーレスポンス
    error_response = handle_error_response(
        error_code="VALIDATION_ERROR",
        error_message="入力データが不正です",
        details={"field": "email", "issue": "invalid format"}
    )
    print(error_response)

def demonstrate_form_validation():
    print("\n7. フォームバリデーションの例")
    print("-" * 30)
    
    # 正しいデータ
    valid_form = validate_and_create_form(
        first_name="山田",
        last_name="太郎",
        email="yamada@example.com",
        age=25
    )
    print(f"有効なフォーム: {valid_form}")
    
    # 不正なデータ
    invalid_form = validate_and_create_form(
        first_name="",
        last_name="次郎",
        email="invalid-email",
        age=-5
    )
    print(f"無効なフォーム: {invalid_form}")

# メイン実行部分
def main():
    demonstrate_basic_usage()
    demonstrate_required_not_required()
    demonstrate_nested_typeddict()
    demonstrate_product_management()
    demonstrate_configuration()
    demonstrate_api_handling()
    demonstrate_form_validation()
    
    print("\n" + "=" * 60)
    print("TypedDict with Unpack のサンプル実行完了!")
    print("注意: 型チェックの恩恵を受けるには、mypy や pyright などの")
    print("型チェッカーを使用することを強く推奨します。")

if __name__ == "__main__":
    main()