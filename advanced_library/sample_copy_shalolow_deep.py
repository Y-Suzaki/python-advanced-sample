import copy
import pprint

source = [{'key1': 'value1', 'key2': 'value2', 'key3': {'nest_key1': 'nest_value1'}}, {'key4': 'value4'}]
# shallow copy
dist = copy.copy(source)
pprint.pprint(dist)

# deep copy
dist = copy.deepcopy(source)
pprint.pprint(dist)
