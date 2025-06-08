# Python 3.13 新機能: 型ヒント機能の拡張
# - TypeVar, ParamSpec, TypeVarTuple のデフォルト値指定
# - typing.ReadOnly による TypedDict の読み取り専用属性
# - typing.TypeIs による型絞り込み

from typing import TypeVar, ParamSpec, TypeVarTuple, TypedDict, Generic, Any
from typing import ReadOnly, TypeIs, Union
from collections.abc import Callable


# TypeVar のデフォルト値指定 (Python 3.13)
T = TypeVar('T', default=str)
K = TypeVar('K', default=str)
V = TypeVar('V', default=int)

class Container(Generic[T]):
    def __init__(self, item: T) -> None:
        self.item = item
    
    def get(self) -> T:
        return self.item


# ParamSpec のデフォルト値指定
P = ParamSpec('P', default=...)

def decorator(func: Callable[P, T]) -> Callable[P, T]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# TypeVarTuple のデフォルト値指定
Ts = TypeVarTuple('Ts', default=tuple[int, str])

class MultiContainer(Generic[*Ts]):
    def __init__(self, *items: *Ts) -> None:
        self.items = items


# ReadOnly による TypedDict の読み取り専用属性
class PersonData(TypedDict):
    name: ReadOnly[str]      # 読み取り専用
    age: ReadOnly[int]       # 読み取り専用
    email: str               # 変更可能


# TypeIs による型絞り込み
def is_string_list(obj: Any) -> TypeIs[list[str]]:
    """オブジェクトが文字列のリストかどうかを判定"""
    return (isinstance(obj, list) and 
            all(isinstance(item, str) for item in obj))


def is_non_empty_string(obj: Any) -> TypeIs[str]:
    """オブジェクトが空でない文字列かどうかを判定"""
    return isinstance(obj, str) and len(obj) > 0


# 使用例
def main():
    # TypeVar デフォルト値の例
    container1 = Container("hello")  # T は str として推論
    container2: Container[int] = Container(42)  # T を明示的に int に指定
    
    print(f"Container1: {container1.get()}")
    print(f"Container2: {container2.get()}")
    
    # TypeVarTuple デフォルト値の例
    multi1 = MultiContainer(1, "hello")  # デフォルトの tuple[int, str]
    multi2: MultiContainer[str, float, bool] = MultiContainer("test", 3.14, True)
    
    print(f"Multi1: {multi1.items}")
    print(f"Multi2: {multi2.items}")
    
    # ReadOnly の例
    person: PersonData = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com"
    }
    
    # 変更可能な属性
    person["email"] = "alice.new@example.com"
    
    # 読み取り専用属性への代入は型チェッカーでエラーになる
    # person["name"] = "Bob"  # Type error
    # person["age"] = 31      # Type error
    
    print(f"Person: {person}")
    
    # TypeIs の例
    data: Any = ["apple", "banana", "cherry"]
    
    if is_string_list(data):
        # この時点で data は list[str] として扱われる
        for item in data:
            print(f"String item: {item.upper()}")
    
    text: Any = "Hello World"
    if is_non_empty_string(text):
        # この時点で text は str として扱われる
        print(f"Non-empty string: {text.strip()}")
    
    # Union 型での TypeIs の活用
    def process_value(value: Union[str, int, None]) -> None:
        if is_non_empty_string(value):
            print(f"Processing string: {value}")
        elif isinstance(value, int):
            print(f"Processing int: {value}")
        else:
            print("Processing None or empty string")
    
    process_value("test")
    process_value(42)
    process_value("")
    process_value(None)


if __name__ == "__main__":
    main()