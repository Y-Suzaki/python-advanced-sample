"""
Python 3.12 新機能: @override デコレータ (PEP 698)

概要:
- Python 3.12では、@override デコレータが typing モジュールに追加されました
- メソッドが親クラスのメソッドを意図的にオーバーライドしていることを明示
- 型チェッカー（mypy, pyright等）がオーバーライドの正確性を検証可能

主な特徴:
1. 継承関係でのメソッドオーバーライドを明示的に示す
2. 型チェッカーによる静的解析の向上
3. コードの意図を明確にし、保守性を向上
4. 誤ったメソッド名やシグネチャの検出が可能

利点:
- バグの早期発見（タイポやシグネチャの不一致）
- コードの意図が明確になる
- リファクタリング時の安全性向上
- チーム開発での意思疎通の改善
"""

from typing import override
from abc import ABC, abstractmethod
import math

print("=" * 60)
print("@override デコレータ (PEP 698) のサンプル")
print("=" * 60)

# 1. 基本的な@overrideの使用例
class Animal:
    """動物の基底クラス"""
    
    def make_sound(self) -> str:
        return "何らかの動物の鳴き声"
    
    def move(self) -> str:
        return "何らかの方法で移動"
    
    def sleep(self) -> str:
        return "眠っています"

class Dog(Animal):
    """犬クラス - @overrideを使用した例"""
    
    @override
    def make_sound(self) -> str:
        return "ワンワン!"
    
    @override
    def move(self) -> str:
        return "4本足で走ります"
    
    # sleep メソッドは意図的にオーバーライドしない

class Cat(Animal):
    """猫クラス - @overrideを使用した例"""
    
    @override
    def make_sound(self) -> str:
        return "ニャーニャー"
    
    @override
    def move(self) -> str:
        return "静かに忍び足で移動"
    
    @override
    def sleep(self) -> str:
        return "日向ぼっこしながら眠っています"

# 2. 抽象基底クラスとの組み合わせ
class Shape(ABC):
    """図形の抽象基底クラス"""
    
    @abstractmethod
    def area(self) -> float:
        """面積を計算する抽象メソッド"""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """周囲長を計算する抽象メソッド"""
        pass
    
    def description(self) -> str:
        """図形の説明を返す"""
        return f"面積: {self.area():.2f}, 周囲長: {self.perimeter():.2f}"

class Rectangle(Shape):
    """長方形クラス"""
    
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    @override
    def area(self) -> float:
        return self.width * self.height
    
    @override
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    @override
    def description(self) -> str:
        return f"長方形 - 幅: {self.width}, 高さ: {self.height}, {super().description()}"

class Circle(Shape):
    """円クラス"""
    
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    @override
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    @override
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    @override
    def description(self) -> str:
        return f"円 - 半径: {self.radius}, {super().description()}"

# 3. 複雑な継承階層での@override使用例
class Vehicle:
    """乗り物の基底クラス"""
    
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model
    
    def start_engine(self) -> str:
        return "エンジンを始動しました"
    
    def stop_engine(self) -> str:
        return "エンジンを停止しました"
    
    def get_info(self) -> str:
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    """自動車クラス"""
    
    def __init__(self, brand: str, model: str, doors: int) -> None:
        super().__init__(brand, model)
        self.doors = doors
    
    @override
    def start_engine(self) -> str:
        return f"{self.get_info()}のエンジンを始動（キーを回します）"
    
    @override
    def get_info(self) -> str:
        return f"{super().get_info()} ({self.doors}ドア)"

class ElectricCar(Car):
    """電気自動車クラス"""
    
    def __init__(self, brand: str, model: str, doors: int, battery_capacity: float) -> None:
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity
    
    @override
    def start_engine(self) -> str:
        return f"{self.get_info()}のモーターを始動（静かに始動）"
    
    @override
    def stop_engine(self) -> str:
        return f"{self.get_info()}のモーターを停止（無音で停止）"
    
    @override
    def get_info(self) -> str:
        return f"{super().get_info()}, バッテリー容量: {self.battery_capacity}kWh"

# 4. データクラスと@overrideの組み合わせ
from dataclasses import dataclass

@dataclass
class Person:
    """人物の基本クラス"""
    name: str
    age: int
    
    def introduce(self) -> str:
        return f"私は{self.name}です。{self.age}歳です。"
    
    def work(self) -> str:
        return "仕事をしています"

@dataclass
class Developer(Person):
    """開発者クラス"""
    programming_language: str
    experience_years: int
    
    @override
    def introduce(self) -> str:
        base_intro = super().introduce()
        return f"{base_intro} {self.programming_language}の開発者で、{self.experience_years}年の経験があります。"
    
    @override
    def work(self) -> str:
        return f"{self.programming_language}でプログラミングをしています"

@dataclass
class Designer(Person):
    """デザイナークラス"""
    design_tool: str
    portfolio_url: str
    
    @override
    def introduce(self) -> str:
        base_intro = super().introduce()
        return f"{base_intro} デザイナーで、主に{self.design_tool}を使用しています。"
    
    @override
    def work(self) -> str:
        return f"{self.design_tool}を使ってデザインを作成しています"

# 5. プロパティのオーバーライド例
class Temperature:
    """温度の基底クラス"""
    
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

class PreciseTemperature(Temperature):
    """高精度温度クラス"""
    
    def __init__(self, celsius: float) -> None:
        super().__init__(celsius)
        self._precision = 3
    
    @property
    @override
    def celsius(self) -> float:
        return round(self._celsius, self._precision)
    
    @property
    @override
    def fahrenheit(self) -> float:
        return round(super().fahrenheit, self._precision)

# デモンストレーション関数群
def demonstrate_basic_override():
    print("1. 基本的な@overrideの使用例")
    print("-" * 30)
    
    animals = [Dog(), Cat()]
    
    for animal in animals:
        print(f"{type(animal).__name__}:")
        print(f"  鳴き声: {animal.make_sound()}")
        print(f"  移動方法: {animal.move()}")
        print(f"  睡眠: {animal.sleep()}")
        print()

def demonstrate_abstract_override():
    print("2. 抽象基底クラスとの組み合わせ")
    print("-" * 30)
    
    shapes = [
        Rectangle(5.0, 3.0),
        Circle(2.5)
    ]
    
    for shape in shapes:
        print(shape.description())

def demonstrate_inheritance_hierarchy():
    print("\n3. 複雑な継承階層での使用例")
    print("-" * 30)
    
    vehicles = [
        Car("Toyota", "Prius", 4),
        ElectricCar("Tesla", "Model 3", 4, 75.0)
    ]
    
    for vehicle in vehicles:
        print(f"車両: {vehicle.get_info()}")
        print(f"  始動: {vehicle.start_engine()}")
        print(f"  停止: {vehicle.stop_engine()}")
        print()

def demonstrate_dataclass_override():
    print("4. データクラスとの組み合わせ")
    print("-" * 30)
    
    people = [
        Developer("田中太郎", 28, "Python", 5),
        Designer("佐藤花子", 25, "Figma", "https://portfolio.example.com")
    ]
    
    for person in people:
        print(person.introduce())
        print(f"  作業内容: {person.work()}")
        print()

def demonstrate_property_override():
    print("5. プロパティのオーバーライド例")
    print("-" * 30)
    
    temps = [
        Temperature(23.456789),
        PreciseTemperature(23.456789)
    ]
    
    for temp in temps:
        class_name = type(temp).__name__
        print(f"{class_name}:")
        print(f"  摂氏: {temp.celsius}°C")
        print(f"  華氏: {temp.fahrenheit}°F")
        print()

# メイン実行部分
def main():
    demonstrate_basic_override()
    demonstrate_abstract_override()
    demonstrate_inheritance_hierarchy()
    demonstrate_dataclass_override()
    demonstrate_property_override()
    
    print("=" * 60)
    print("@override デコレータのサンプル実行完了!")
    print("注意: @overrideの効果を完全に体験するには、")
    print("型チェッカー（mypy, pyright等）を使用してください。")

if __name__ == "__main__":
    main()