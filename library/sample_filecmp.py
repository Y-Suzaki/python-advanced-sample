import tempfile
import filecmp
import os

with tempfile.TemporaryDirectory() as dr:
    temp_path_1 = os.path.join(dr, 'temp.txt')
    with open(temp_path_1, 'w') as f:
        f.write('aaa')
        f.write('bcbc')

    temp_path_2 = os.path.join(dr, 'temp2.txt')
    with open(temp_path_2, 'w') as f:
        f.write('aaa')
        f.write('bcbc')

    temp_path_3 = os.path.join(dr, 'temp3.txt')
    with open(temp_path_3, 'w') as f:
        f.write('aaa')
        f.write('bcb')

    # true
    print(filecmp.cmp(temp_path_1, temp_path_2))

    # false
    print(filecmp.cmp(temp_path_1, temp_path_3))
