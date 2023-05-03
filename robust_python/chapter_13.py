from __future__ import annotations

from typing import Protocol, Callable


# プロトコルで型定義（TypeScriptのtypeみたいなもの？）
# 継承は使いたくないけど、安全にダックタイピングしたい。
class Event(Protocol):
    event_id: int
    name: str

    def get_file_names(self) -> list[str]:
        pass


def print_file_names(event: Event):
    files = event.get_file_names()
    for file in files:
        print(file)


class CrashEvent:
    # Event(Protocol)の型定義と一致
    def __init__(self, name: str, event_id: int):
        self.name = name
        self.event_id = event_id

    def get_file_names(self) -> list[str]:
        return [f'{self.event_id}/{self.name}/front.jpg', f'{self.event_id}/{self.name}/rear.jpg']


class MotionEvent:
    # Event(Protocol)の型定義と一致
    def __init__(self, name: str, event_id: int):
        self.name = name
        self.event_id = event_id

    def get_file_names(self) -> list[str]:
        return [f'{self.event_id}/{self.name}/front_m.jpg', f'{self.event_id}/{self.name}/rear_m.jpg']


class AccOff:
    # Event(Protocol)の型定義と不一致
    def __init__(self, name: str, event_id: int):
        self.name = name
        self.event_id = event_id

    def get_file_name(self) -> str:
        return f'{self.event_id}/{self.name}/front_acc.jpg'


crash_event = CrashEvent('Crash', 123)
motion_event = MotionEvent('Motion', 456)
acc = AccOff('Acc', 789)

print_file_names(crash_event)
print_file_names(motion_event)
# mypyでエラー検出される。（実行時にも例外になる。）
print_file_names(acc)
