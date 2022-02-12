import os
import numpy
from sample_threading import loop_print

ar = numpy.asarray([1, 4, 5, 2, 9, 3])
print(ar)

# 平均値
print(ar.mean())

# 最小、最大
print(ar.min())
print(ar.max())

# 和
print(ar.sum())

# ソート
ar.sort()
print(ar)
