## 関数引数の１つ「*」は可変長引数
def func_one_asta(*args):
    for i in args:
        print(i)
    print()

func_one_asta('aa', 'bb', 'cc')


## 関数呼び出し時の１つ「*」はアンパック
names = ('suzaki', 'tanaka', 'sato')

# １つのtapleオブジェクトとして渡される
func_one_asta(names)

# それぞればらばらの引数として渡される
func_one_asta(*names)


## 関数引数の２つ「**」キーワード付きの可変長引数
def func_two_asta(**args):
    for key in args:
        print(args.get(key))
    print()

func_two_asta(name='suzaki', age=30)


## 関数呼び出し時の２つ「**」はDictのアンパック

person = {'name': 'tanaka', 'age': 28, 'address': 'tokyo'}

# それぞればらばらのキーワード付引数として渡される
func_two_asta(**person)
