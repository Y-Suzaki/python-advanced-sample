from dataclasses import dataclass


@dataclass
class Person:
    # generate __init__ and __str__ automatically.
    name: str = 'tanaka'
    age: int = 30
    address: str = 'tokyo'

    def format(self) -> str:
        return f'{self.name} / {self.age} / {self.address}'


# Construct a dataclass which has no argument.
person = Person()
print(person)

# construct a dataclass which has multiple arguments.
person = Person('ito', 99, 'saitama')
print(person)

