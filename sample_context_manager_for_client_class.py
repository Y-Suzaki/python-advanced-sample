from contextlib import contextmanager

# with分を使って、アクセスライブラリのClose漏れを防ぐ

class S3Client:
    def __init__(self):
        print('init')

    def get(self):
        print('s3 get.')

    def close(self):
        print('close.')

@contextmanager
def s3_helper():
    s3_client = S3Client()
    try:
        yield s3_client
        print('end yield.')
    finally:
        s3_client.close()

# ジェネレータで返された値は、asで受け取ることができる
with s3_helper() as client:
    client.get()