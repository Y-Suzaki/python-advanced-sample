from typing import Union, TypedDict

MOTION_EVENT = dict[str, Union[str, int]]


# 型エイリアスで別名付けるのもあり。
def get_event(_id: int) -> MOTION_EVENT:
    if _id == 1:
        return {
            "test": "test"
        }
    else:
        return {
            "test": 123
        }


# TypedDictでdictを使いやすく
class Video(TypedDict):
    video_id: int
    video_path: str


class AccOffEvent(TypedDict):
    event_id: int
    event_name: str
    content: Video


# 型だけでなく、変数名を指摘してくれる。ただし、実行時にはただのdictでしかない。
acc_off: AccOffEvent = {
    "event_id": 123,
    "event_name": "name",
    "content": {
        "video_id": 123,
        "video_path": "path"
    }
}

print(type(acc_off), acc_off)
