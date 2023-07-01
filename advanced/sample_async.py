import asyncio
import time


async def main_simple():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
    return {
        'message': 'success'
    }


async def get_message(_id: str):
    print(f'get_message start. {_id}, {time.strftime("%X")}')
    await asyncio.sleep(2)
    print(f'get_message end. {_id}')
    return {
        'message': 'success'
    }


async def main_multiple():
    print(f'\n**** main_multiple ****')
    print(await get_message('001'))
    print(await get_message('002'))
    print(f'main_multiple end, {time.strftime("%X")}')


async def main_gather():
    print(f'\n**** main_gather ****')
    coroutine_1 = get_message('101')
    coroutine_2 = get_message('102')
    _response = await asyncio.gather(coroutine_1, coroutine_2)
    print(f'main_gather end, {time.strftime("%X")}')
    return _response


# 単に呼んでも`coroutine`オブジェクトが返ってくるだけで、実行はされない。
coroutine = main_simple()
print(coroutine)
print(type(coroutine))
print()

# 実行するには、asyncio.run()に渡す。
response = asyncio.run(coroutine)
print(response)

# 非同期関数を順番に実行したい場合は、awaitで待つ。
# 結局順番に実行待ちするため完了に4秒掛かる。この書き方自体はあまり意味がない。
asyncio.run(main_multiple())

# 複数の非同期処理を実行して、合わせて待つ。
# 複数IOを同時に投げて並列処理させて、とりあえず待つには良い。完了は2秒で済む。
response = asyncio.run(main_gather())
# 結果は単純なlist[dict]で返ってくる。
print(response)
