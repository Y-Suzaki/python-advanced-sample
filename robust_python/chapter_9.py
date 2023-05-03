from dataclasses import dataclass


@dataclass(eq=True)
class Recipe:
    name: str
    cost: int


# eq=Trueを付与することで、eq()が実装される。
# デフォルトの挙動は、全てのフィールドを一致するか比較する。

recipe1 = Recipe("juice", 300)
recipe2 = Recipe("juice", 300)
recipe3 = Recipe("juice", 350)

print(recipe1 == recipe2)
print(recipe1 == recipe3)
