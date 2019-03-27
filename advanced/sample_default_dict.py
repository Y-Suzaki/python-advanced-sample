import collections

items = {'orange': 200, 'apple': 100}
key_list = ('orange', 'melon', 'apple', 'suika')
print(items)

class Missing:
    def __init__(self):
        self.missing_count = 0

    def __call__(self, *args):
        """ オブジェクトそのものを渡すと、暗黙的に_call_が呼ばれる """
        print('-- missing --')
        self.missing_count += 1
        return 0

missing = Missing()
new_items = collections.defaultdict(missing, items)
for key in key_list:
    print(new_items[key])
print('result:{}, {}'.format(new_items, missing.missing_count))
