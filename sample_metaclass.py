from abc import abstractmethod
from abc import ABCMeta

class Human:
    @abstractmethod
    def shut(self):
        pass

class Employee(Human):
    def __init__(self):
        print('init:{}'.format(self.__class__))


# @abstractmethodを付与しただけでは、特にエラーになってくれない
# classオブジェクト作成時に、metaclassの機能を動かす必要がある
print('start employee = Employee()')
employee = Employee()
employee.shut()


# metaclass=ABCMetaを指定する。ABCクラスを継承するでも良い。
class NewHuman(metaclass=ABCMeta):
    @abstractmethod
    def shut(self):
        pass

class NewEmployee(NewHuman):
    pass

# TypeError: Can't instantiate abstract class NewEmployee with abstract methods shutをきちんとraiseしてくれる
print('start new_employee = NewEmployee()')
new_employee = NewEmployee()
