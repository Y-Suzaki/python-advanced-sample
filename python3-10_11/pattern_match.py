"""
Python3.10
パターンマッチング機能で、Switch文のような使い方ができる。
"""


def http_error(status: int):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong ty the Internet"


print(http_error(400))


def match_position(coordinate: tuple[int, int]):
    """ tupleのようなオブジェクトも利用可能 """
    match coordinate:
        case (0, 0):
            return "Invalid position"
        case (-1, -1):
            return "Error position"
        case _:
            return "OK"


print(match_position((-1, -1)))
print(match_position((145, 38)))
