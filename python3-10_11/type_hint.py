"""
Python3.10
型定義
"""
# Unionから|
# TypeScriptのようの記載できる。
from typing import Union


def print_out(message: Union[str, None]):
    print(message)


def print_out_10(message: str | None):
    print(message)


"""
Python3.11
型定義 TypedDictに必須、オプション
"""
from typing import TypedDict, Required, NotRequired


# NotRequiredがない場合、省略するとエラーが表示される。
# あくまでも型定義なので、実行時のエラーは出ない。
class NormalMovie(TypedDict):
    title: str
    year: int


movie_2: NormalMovie = {'title': 'ドラゴンクエスト'}
print(movie_2)


class Movie(TypedDict):
    title: str
    year: NotRequired[int]


movie_2: Movie = {'title': 'ドラゴンクエスト'}
print(movie_2)


# total = falseで、デフォルトをすべてオプションにもできる。
class OptionalMovie(TypedDict, total=False):
    title: str
    year: int


movie_3: OptionalMovie = {}
print(movie_3)


"""
Python3.11
型定義 自分のクラスを型で返す場合にselfが使える
"""
from typing import Self


class Location:
    @classmethod
    def create(cls) -> Self:
        return Location()

    def __str__(self):
        return "location"


location = Location.create()
print(location)

