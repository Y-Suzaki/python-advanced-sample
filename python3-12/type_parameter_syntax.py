"""
Python 3.12 新機能: 新しい型パラメータ構文 (PEP 695)

概要:
- Python 3.12では、ジェネリック型の定義がより簡潔で直感的になりました
- 従来のTypeVar, Genericを使った冗長な書き方から、[]を使った新しい構文に変更
- 型パラメータのスコープがより明確になり、型安全性が向上

主な変更点:
1. クラスの型パラメータ: class MyClass[T]: の書き方
2. 関数の型パラメータ: def my_func[T](...) -> T: の書き方
3. 型エイリアスの改善: type NewType[T] = list[T] の書き方

利点:
- より読みやすく、理解しやすいコード
- 型パラメータのスコープが明確
- 型チェッカーでの精度向上
"""

from collections.abc import Iterable, Callable
import sys

print(f"Python version: {sys.version}")
print("=" * 60)
print("新しい型パラメータ構文 (PEP 695) のサンプル")
print("=" * 60)

# 1. ジェネリッククラスの新しい書き方
class Stack[T]:
    """型安全なスタック実装"""
    
    def __init__(self) -> None:
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        """要素をスタックにプッシュ"""
        self._items.append(item)
    
    def pop(self) -> T | None:
        """要素をスタックからポップ"""
        if not self._items:
            return None
        return self._items.pop()
    
    def peek(self) -> T | None:
        """スタックのトップ要素を確認（削除しない）"""
        if not self._items:
            return None
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """スタックが空かどうか確認"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """スタックのサイズを取得"""
        return len(self._items)

# 2. ジェネリック関数の新しい書き方
def find_first[T](items: Iterable[T], predicate: Callable[[T], bool]) -> T | None:
    """条件を満たす最初の要素を検索"""
    for item in items:
        if predicate(item):
            return item
    return None

def map_items[T, U](items: Iterable[T], mapper: Callable[[T], U]) -> list[U]:
    """要素を変換してリストで返す"""
    return [mapper(item) for item in items]

def filter_items[T](items: Iterable[T], predicate: Callable[[T], bool]) -> list[T]:
    """条件を満たす要素のみをフィルタリング"""
    return [item for item in items if predicate(item)]

# 3. 複数の型パラメータを持つクラス
class Pair[T, U]:
    """2つの異なる型の値を保持するペア"""
    
    def __init__(self, first: T, second: U) -> None:
        self.first = first
        self.second = second
    
    def get_first(self) -> T:
        return self.first
    
    def get_second(self) -> U:
        return self.second
    
    def swap(self) -> 'Pair[U, T]':
        """要素を入れ替えた新しいペアを返す"""
        return Pair(self.second, self.first)
    
    def __str__(self) -> str:
        return f"Pair({self.first}, {self.second})"

# 4. 制約付き型パラメータ
class NumberContainer[T: (int, float)]:
    """数値型のみを扱うコンテナ"""
    
    def __init__(self, value: T) -> None:
        self.value = value
    
    def add(self, other: T) -> T:
        return self.value + other
    
    def multiply(self, factor: T) -> T:
        return self.value * factor

# 使用例とデモンストレーション
def demonstrate_type_parameters():
    print("1. スタックの使用例")
    print("-" * 30)
    
    # 文字列スタック
    string_stack = Stack[str]()
    string_stack.push("Hello")
    string_stack.push("World")
    string_stack.push("Python 3.12")
    
    print(f"文字列スタックのサイズ: {string_stack.size()}")
    print(f"トップ要素: {string_stack.peek()}")
    print(f"ポップした要素: {string_stack.pop()}")
    print(f"ポップ後のサイズ: {string_stack.size()}")
    
    # 数値スタック
    int_stack = Stack[int]()
    for i in range(1, 6):
        int_stack.push(i * 10)
        # NG: int_stack.push("abc)

    print(f"\n数値スタックの内容:")
    while not int_stack.is_empty():
        print(f"  {int_stack.pop()}")
    
    print("\n2. ジェネリック関数の使用例")
    print("-" * 30)
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 偶数を検索
    first_even = find_first(numbers, lambda x: x % 2 == 0)
    print(f"最初の偶数: {first_even}")
    
    # 数値を文字列にマップ
    string_numbers = map_items(numbers, lambda x: f"Number: {x}")
    print(f"マップされた文字列: {string_numbers[:3]}...")
    
    # 奇数をフィルタリング
    odd_numbers = filter_items(numbers, lambda x: x % 2 == 1)
    print(f"奇数のみ: {odd_numbers}")
    
    print("\n3. ペアクラスの使用例")
    print("-" * 30)
    
    # 異なる型のペア
    name_age_pair = Pair("Alice", 30)
    print(f"名前と年齢のペア: {name_age_pair}")
    
    city_population_pair = Pair("Tokyo", 14000000)
    print(f"都市と人口のペア: {city_population_pair}")
    
    # ペアの入れ替え
    swapped = name_age_pair.swap()
    print(f"入れ替え後: {swapped}")
    
    print("\n4. 制約付き型パラメータの使用例")
    print("-" * 30)
    
    # 整数コンテナ
    int_container = NumberContainer(42)
    print(f"整数値: {int_container.value}")
    print(f"10を加算: {int_container.add(10)}")
    print(f"3倍: {int_container.multiply(3)}")
    
    # 浮動小数点コンテナ
    float_container = NumberContainer(3.14)
    print(f"浮動小数点値: {float_container.value}")
    print(f"2.86を加算: {float_container.add(2.86)}")
    print(f"2倍: {float_container.multiply(2.0)}")

if __name__ == "__main__":
    demonstrate_type_parameters()
    print("\n" + "=" * 60)
    print("型パラメータ構文のサンプル実行完了!")