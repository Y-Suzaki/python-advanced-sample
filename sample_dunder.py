# 組み込み関数は、内部でdunder（__xxx__）を呼んでいる
ar = [1, 2, 3]
print(len(ar))
print(ar.__len__())


# 関数もオブジェクトである
def add(a, b, c):
    return a + b + c

# 下記は、<class 'function'>と出力される
print(type(add))

# 関数呼び出しは、functionクラスに実装された__call_メソッドを呼んでいるだけ。
print(add(1, 10, 100))
print(add.__call__(1, 10, 100))
