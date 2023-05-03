from __future__ import annotations


# オブジェクトの加算を、+=をOverrideして実現
class Sell:
    def __init__(self, name: str, money: int):
        self._name = name
        self._money = money

    def __add__(self, other: Sell):
        if self._name == other._name:
            self._money += other._money
        else:
            raise ValueError('Not equal.')
        return self

    def __str__(self):
        # フィールドの値をとりあえず出力しておきたい場合
        return self.__dict__.__str__()


hat = Sell('hat', 500)
print(hat)

hat2 = Sell('hat', 1000)
hat += hat2
print(hat)
