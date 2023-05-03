from __future__ import annotations
from dataclasses import dataclass

from typing import Protocol, Callable

# Template Methodパターン
# 一部の処理のみ上書きするパターン。


class User(Protocol):
    def init(self) -> None:
        pass

    def finalize(self) -> None:
        pass


class AdminUser:
    def init(self) -> None:
        print('Admin init.')

    def finalize(self) -> None:
        print('Admin finalize.')


class NormalUser:
    def init(self) -> None:
        print('Normal init.')

    def finalize(self) -> None:
        print('Normal finalize.')


def create_user(user: User):
    user.init()
    print('Main logic.')
    user.finalize()


create_user(AdminUser())
create_user(NormalUser())


# Strategy パターン
# 関数を引数に渡して、一部の処理のみ書き換えるパターン
@dataclass
class UserData:
    name: str
    age: int


def create_admin_user(user: UserData):
    print(f"管理者ユーザーを作成します。 {user=}")
    print("管理者権限を付与します。")


def create_normal_user(user: UserData):
    print(f"ノーマルユーザーを作成します。, {user=}")


def create_user_strategy(create: Callable[[UserData], None], user: UserData):
    print("共通の初期化処理")
    create(user)
    print("共通の終了処理")


create_user_strategy(create_admin_user, UserData('suzaki', 41))
create_user_strategy(create_normal_user, UserData('suzaki', 42))

