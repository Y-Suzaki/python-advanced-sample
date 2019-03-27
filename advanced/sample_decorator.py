class DBException(Exception):
    pass


# Exceptionが発生したら、DBExceptionにラップしてraiseするデコレータ
# DBトランザクションやロギング等、関数に共通処理を挟みたい場合に有効
def exception_handler(func):
    import functools

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('--start--')
        try:
            # 引数で渡された関数オブジェクトの__call__が呼ばれる
            func(*args, **kwargs)
        except Exception as e:
            print('--exception end--')
            raise DBException(e)
        finally:
            print('--exception finally--')
        print('--end--')
    return wrapper


@exception_handler
def update(name):
    print('update {}'.format(name))


@exception_handler
def delete(id):
    print('delete {}'.format(id))
    raise ValueError('param error.')


update('suzaki')
delete(1234)
