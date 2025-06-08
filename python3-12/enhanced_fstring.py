"""
Python 3.12 新機能: 拡張されたf-string構文 (PEP 701)

概要:
- Python 3.12では、f-stringの制限が大幅に緩和されました
- より柔軟で表現力豊かなf-string記法が可能になりました
- PEGパーサーによる改善により、以前は不可能だった記法が利用可能

主な改善点:
1. ネストしたクォートの制限緩和
2. バックスラッシュエスケープの改善
3. より複雑な式の埋め込みが可能
4. デバッグ表示の改善
5. 辞書アクセスの制限緩和

利点:
- より読みやすい文字列フォーマット
- 複雑なデータ構造の表示が簡単
- デバッグ時の可読性向上
- コードの簡潔性向上
"""

import json
import datetime
from dataclasses import dataclass
from typing import Dict, List, Any

print("=" * 60)
print("拡張されたf-string構文 (PEP 701) のサンプル")
print("=" * 60)

# 1. ネストしたクォートの改善
def demonstrate_nested_quotes():
    print("1. ネストしたクォートの使用例")
    print("-" * 30)
    
    name = "Alice"
    data = {"language": "Python", "version": "3.12", "status": "stable"}
    
    # 辞書のキーにシングルクォートを使用
    result1 = f"Hello {name}, you're using {data['language']} {data['version']}"
    print(f"辞書アクセス: {result1}")
    
    # より複雑なネストしたクォート
    quotes = {
        "famous": "To be or not to be, that's the question",
        "simple": "Hello world"
    }
    formatted = f"Famous quote: \"{quotes['famous']}\""
    print(f"ネストクォート: {formatted}")
    
    # JSONライクな文字列生成
    json_like = f"{{'name': '{name}', 'language': '{data['language']}'}}"
    print(f"JSON風文字列: {json_like}")

# 2. 複雑な式の埋め込み
def demonstrate_complex_expressions():
    print("\n2. 複雑な式の埋め込み例")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # リスト内包表記の使用
    even_numbers = f"偶数: {[n for n in numbers if n % 2 == 0]}"
    print(even_numbers)
    
    # 関数呼び出しの埋め込み
    sum_result = f"合計: {sum(n for n in numbers if n % 2 == 0)}"
    print(sum_result)
    
    # 条件式の使用
    status = "large" if len(numbers) > 5 else "small"
    conditional = f"リストのサイズは{status}です ({len(numbers)}個の要素)"
    print(conditional)
    
    # 辞書内包表記
    squared_dict = {n: n**2 for n in range(1, 6)}
    dict_display = f"平方数: {', '.join(f'{k}²={v}' for k, v in squared_dict.items())}"
    print(dict_display)

# 3. デバッグ表示の改善
def demonstrate_debug_formatting():
    print("\n3. デバッグ表示機能")
    print("-" * 30)
    
    x = 42
    y = 3.14159
    name = "Python"
    
    # デバッグ表示（変数名と値を同時に表示）
    print(f"{x=}")
    print(f"{y=:.2f}")
    print(f"{name=}")
    
    # 複雑な式のデバッグ表示
    numbers = [1, 2, 3, 4, 5]
    print(f"{len(numbers)=}")
    print(f"{sum(numbers)=}")
    print(f"{max(numbers)=}")
    
    # 関数呼び出しのデバッグ表示
    result = sum(n**2 for n in numbers)
    print(f"{sum(n**2 for n in numbers)=}")

# 4. データクラスとf-stringの組み合わせ
@dataclass
class Person:
    name: str
    age: int
    city: str
    hobbies: List[str]

def demonstrate_dataclass_formatting():
    print("\n4. データクラスとの組み合わせ")
    print("-" * 30)
    
    person = Person(
        name="Bob",
        age=30,
        city="Tokyo",
        hobbies=["reading", "programming", "photography"]
    )
    
    # 基本的な情報表示
    basic_info = f"{person.name} ({person.age}歳) は {person.city} に住んでいます"
    print(basic_info)
    
    # 趣味の表示
    hobbies_info = f"{person.name}の趣味: {', '.join(person.hobbies)}"
    print(hobbies_info)
    
    # 条件付き表示
    age_category = "若い" if person.age < 30 else "大人"
    category_info = f"{person.name}は{age_category}人です"
    print(category_info)

# 5. 日時フォーマットの例
def demonstrate_datetime_formatting():
    print("\n5. 日時フォーマットの例")
    print("-" * 30)
    
    now = datetime.datetime.now()
    
    # 基本的な日時表示
    basic_date = f"現在時刻: {now:%Y-%m-%d %H:%M:%S}"
    print(basic_date)
    
    # 複雑な日時フォーマット
    japanese_date = f"今日は{now:%Y}年{now:%m}月{now:%d}日です"
    print(japanese_date)
    
    # 曜日の表示
    weekday = f"今日は{now:%A}です"
    print(weekday)
    
    # 相対時間の計算
    birthday = datetime.datetime(2024, 1, 1)
    days_diff = (now - birthday).days
    relative_time = f"2024年1月1日から{days_diff}日が経過しました"
    print(relative_time)

# 6. 多言語対応の例
def demonstrate_multilingual_formatting():
    print("\n6. 多言語対応の例")
    print("-" * 30)
    
    translations = {
        "ja": {"hello": "こんにちは", "world": "世界"},
        "en": {"hello": "Hello", "world": "World"},
        "es": {"hello": "Hola", "world": "Mundo"}
    }
    
    name = "Alice"
    
    for lang_code, trans in translations.items():
        greeting = f"{trans['hello']}, {name}! Welcome to {trans['world']}!"
        print(f"{lang_code.upper()}: {greeting}")

# 7. JSONとの組み合わせ
def demonstrate_json_formatting():
    print("\n7. JSONフォーマットとの組み合わせ")
    print("-" * 30)
    
    user_data = {
        "id": 12345,
        "name": "Charlie",
        "email": "charlie@example.com",
        "preferences": {
            "theme": "dark",
            "language": "ja"
        }
    }
    
    # JSON風表示
    json_str = json.dumps(user_data, indent=2, ensure_ascii=False)
    formatted = f"ユーザーデータ:\n{json_str}"
    print(formatted)
    
    # 特定の値を抽出して表示
    user_info = f"ユーザー: {user_data['name']} (ID: {user_data['id']})"
    print(f"\n{user_info}")
    
    # ネストした辞書の値を表示
    preferences = f"設定: テーマ={user_data['preferences']['theme']}, 言語={user_data['preferences']['language']}"
    print(preferences)

# 8. エラーハンドリングとf-string
def demonstrate_error_formatting():
    print("\n8. エラーハンドリングでの使用例")
    print("-" * 30)
    
    def divide(a: float, b: float) -> float:
        try:
            result = a / b
            success_msg = f"{a} ÷ {b} = {result:.2f}"
            print(success_msg)
            return result
        except ZeroDivisionError as e:
            error_msg = f"エラー: {a} を 0 で割ることはできません ({type(e).__name__})"
            print(error_msg)
            return 0.0
        except Exception as e:
            error_msg = f"予期しないエラー: {type(e).__name__}: {e}"
            print(error_msg)
            return 0.0
    
    # 正常ケース
    divide(10, 2)
    
    # エラーケース
    divide(10, 0)

# メイン実行部分
def main():
    demonstrate_nested_quotes()
    demonstrate_complex_expressions()
    demonstrate_debug_formatting()
    demonstrate_dataclass_formatting()
    demonstrate_datetime_formatting()
    demonstrate_multilingual_formatting()
    demonstrate_json_formatting()
    demonstrate_error_formatting()
    
    print("\n" + "=" * 60)
    print("拡張されたf-string構文のサンプル実行完了!")

if __name__ == "__main__":
    main()