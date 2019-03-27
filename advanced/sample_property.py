# getter、setterではなく、@propertyデコレータを使う。
# objectクラスを明示的に継承する必要がある。（python3では暗黙のため不要）
# 参考ページ：http://taustation.com/python3-gettersetter/
class Person():
    def __init__(self):
        print('init.')
        self._name = 'empty'

    @property
    def name(self):
        print('call getter.')
        return self._name

    @name.setter
    def name(self, name):
        print('call setter.')
        if not name:
            raise ValueError('invalid parameter.')
        self._name = name

# 使う側はpublic属性時と同じくシンプルになる
person = Person()
person.name = 'suzaki'
print(person.name)
person.name = ''
