# This is how to use string format.
name = 'tanaka'
age = 30

# previous version
out = '{}/{}'.format(name, age)
print(out)

# current version
out = f'{name}/{age}'
print(out)

