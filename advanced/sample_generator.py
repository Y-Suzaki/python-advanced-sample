# **** yieldを記載すると、generator関数になる ****
def simple_generator(x):
    yield x ** 2

# generatorはiteratorを返すため、next()で次の要素を取得できる
print(next(simple_generator(5)))


# **** iteratorが値を返す限り続く ****
def roop_generator(x):
    print('roop_generator start')
    for i in range(x):
        yield i ** 2
    print('roop_generator end')

# generator関数は呼び出し時点では実行されない
rg = roop_generator(5)
print('**************')
for i in rg:
    print(i)

# iteratorが終端に達した後、next()を呼び出すとStopIterationがraiseされる
next(rg)

