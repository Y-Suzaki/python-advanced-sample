import numpy

x = numpy.array([1, 2, 3])
y = numpy.array([2., 3.9, 6.1])

# 中心化
x_center = x - x.mean()
y_center = y - y.mean()

# 各要素の二乗計算
xx = x_center * x_center
xy = x_center * y_center

print(f'{xx=}, {xy=}')

# 単回帰分析の要素aを求める
a = xy.sum() / xx.sum()
print(f'{a=}')
