import shelve

# Dictionaryの形式でファイルの読み書きができる
# 単純なKey=Valueであれば、標準ライブラリで事足りる

FILE_NAME = 'shelve'

with shelve.open(FILE_NAME) as f:
    f['key1'] = 'value1'
    f['key2'] = 'value2'

with shelve.open(FILE_NAME, 'r') as f:
    print(f['key1'])
    print(f['key2'])

