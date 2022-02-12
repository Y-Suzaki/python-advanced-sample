import pandas
from matplotlib import pyplot

df = pandas.read_csv('sample.csv')
print(df)

x = df['x']
y = df['y']


# 散布図でプロット
pyplot.scatter(x, y)
pyplot.show()
