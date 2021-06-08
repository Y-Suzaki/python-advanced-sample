import tempfile
import os

# 一時ディレクトリ
with tempfile.TemporaryDirectory() as dir:
    temp_path = os.path.join(dir, 'temp.txt')
    # shelveを使うことで、ディクショナリ形式で扱うことができる
    with open(temp_path, 'w') as f:
        # 書き込み
        f.write('test')
        # ファイルの存在確認（）
        print(os.path.exists(temp_path))

# 一時ディレクトリのため、この時点では削除されているtrue（false）
print(os.path.exists(temp_path))
