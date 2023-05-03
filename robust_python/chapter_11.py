from contextlib import contextmanager
# context managerの基本的な使い方
from typing import TypedDict, Optional


@contextmanager
def create_db_session():
    session = 'dummy-session'
    try:
        yield session
    except Exception as e:
        print(f'Exception {e}')
        raise e
    finally:
        print('Close session.')


class LoginUser(TypedDict):
    name: str


def get_user() -> LoginUser:
    with create_db_session() as session:
        print(f'Use the session. {session}')
        return {'name': 'tanaka'}


def get_user_with_error() -> Optional[LoginUser]:
    with create_db_session() as session:
        print(f'Use the session. {session}')
        raise ValueError('Value error.')
    return {'name': 'tanaka'}


print(get_user())
print(get_user_with_error())
