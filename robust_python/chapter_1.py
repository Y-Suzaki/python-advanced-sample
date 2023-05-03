# defaultdictは、存在しないキーにアクセスした場合に、自動でデフォルト値が入る。

from collections import defaultdict
from dataclasses import dataclass
from typing import Any


@dataclass
class Cookbook:
    autor: str


def create_author_count_mapping(cookbooks: list[Cookbook]):
    counter: defaultdict[Any, int] = defaultdict(lambda: 0)
    for cookbook in cookbooks:
        counter[cookbook.autor] += 1
    return counter

_cookbooks = [
    Cookbook('book1'),
    Cookbook('book2'),
    Cookbook('book3'),
    Cookbook('book1')
]
_counter = create_author_count_mapping(_cookbooks)
print(_counter)
