"""
Python3.11
複数Exceptionを束ねるExceptionGroupが追加。
並列処理で複数の例外が同時に発生する場合などに利用する。
"""


# まとめてExceptionGroupでexcept
try:
    raise ExceptionGroup("eg", [ValueError("ValueError 1"), TypeError("TypeError 2")])
except ExceptionGroup as eg:
    print(repr(eg))


# バラバラにexceptする方が推奨らしい。
# 両方のexceptブロックが実行される。
try:
    raise ExceptionGroup("eg", [ValueError("ValueError 1"), TypeError("TypeError 2")])
except* ValueError as eg :
    print(f'ValueError. {repr(eg)}')
except* TypeError as eg :
    print(f'TypeError. {repr(eg)}')

print("End")
