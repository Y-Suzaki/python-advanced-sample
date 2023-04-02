from typing import Optional, Union, Literal, NewType
from dataclasses import dataclass


# Optional型
def get_user(is_admin: bool) -> Optional[str]:
    if is_admin:
        return 'tanaka'
    else:
        return None


# Union型
def get_age(version: int) -> Union[str, int]:
    if version >= 3:
        # version 3以上は、数値型で格納されるように仕様変更があった。
        return 41
    else:
        return "41"


# Literal型
@dataclass
class Event:
    event_id: str
    event_type: Literal['crash', 'motion']  # typescriptの'crash' | 'motion' と同じ


ALERT_EVENT = NewType('ALERT_EVENT', Event)


def print_alert_event(event: ALERT_EVENT):
    print(event)


def main() -> None:
    user = get_user(False)
    print(user)

    if user:
        # Noneチェックがないと警告が出る。
        _user = user + 'test'

    age = get_age(4)
    print(age)

    # crashはOK、testは警告が出る
    crash_event = Event('123', 'crash')
    test_event = Event('456', 'test')
    print(crash_event, test_event)

    # New Type型  typescriptのtypeof で型定義を抜き出しているのと同じ
    alert_event = ALERT_EVENT(crash_event)
    print_alert_event(alert_event)
    # 以下は型が違う警告になる。
    print_alert_event(crash_event)


if __name__ == '__main__':
    main()
