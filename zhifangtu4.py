# -*- coding: utf-8 -*-
import numpy
import matplotlib
from pandas import read_csv
from matplotlib import pyplot as plt

font = {
    'family' : 'SimHei'
}
matplotlib.rc('font', **font)

data = read_csv('./data_1.csv')

d1 = "省份"
d2 = '通信品牌'
v = "月流量"

gb = data.groupby(by=[d1,d2], )['月流量（M）'].agg({v: numpy.sum})
print(gb)
d1size = gb.index.levels[0].size
d2size = gb.index.levels[1].size

index = numpy.arange(d1size)
print(d1size,d2size,index)
colors=['r', 'g', 'b']

for i in range(0, d2size):
    print(i)
    subgb = gb[v][gb.index.labels[1]==i]
    bar = plt.bar(index*d2size + i, subgb, color=colors[i])
                # [0,1,2,3,4,5,6,7]* 3 + i

lIndex = numpy.arange(d1size)*d2size   #[0,1,2,3,4,5,6,7] * 3
#
plt.xticks(lIndex , gb.index.levels[0])

plt.legend(gb.index.levels[1])
plt.show()
