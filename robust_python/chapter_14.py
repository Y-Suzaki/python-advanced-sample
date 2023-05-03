import json
from pydantic import constr
from pydantic.dataclasses import dataclass
from pydantic.error_wrappers import ValidationError
from typing import Optional, Literal


# pydanticを使うと、データ型に合わせてバリデーションが行われる。
@dataclass
class Location:
    date_time: str
    lat: float
    lng: float


@dataclass
class Address:
    city: constr(min_length=3, max_length=10)
    building: int


@dataclass
class LocationAddress:
    date_time: str
    lat: float
    lng: float
    address: Address


# OK
with open("./chapter_14_1.json") as f:
    _json = json.load(f)

_loc_1 = Location(**_json)
print(_loc_1)

# latが数字ではなく、文字列になっているためNG
with open("./chapter_14_2.json") as f:
    _json = json.load(f)

try:
    _loc_2 = Location(**_json)
    print(_loc_2)
except ValidationError as e:
    # value is not a valid float (type=type_error.float)
    print(e)


# ネストした定義 OK
with open("./chapter_14_3.json") as f:
    _json = json.load(f)

try:
    _loc_3 = LocationAddress(**_json)
    print(_loc_3)
except Exception as e:
    print(e)

# ネストした定義 NG（文字列の長さでNG）
with open("./chapter_14_4.json") as f:
    _json = json.load(f)

try:
    _loc_4 = LocationAddress(**_json)
    print(_loc_4)
except ValidationError as e:
    print(e)
