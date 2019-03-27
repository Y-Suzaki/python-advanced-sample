# with構文を使って、一時的な変更を行いたい
# 例では、withブロック内のみ、ログレベルを変更している。

import logging
from contextlib import contextmanager

@contextmanager
def set_log_debug_level():
    logger = logging.getLogger()
    old_log_level = logger.getEffectiveLevel()
    print('The default log level is {}.'.format(logging.getLevelName(old_log_level)))
    logger.setLevel(logging.DEBUG)
    try:
        yield
    finally:
        logger.setLevel(old_log_level)

def log(message):
    logging.debug('debug:' + message)
    logging.info('info:' + message)

# debug、info共に出力される
with set_log_debug_level():
    log('with')

# 何も出力されない
log('not with')
