# -*- coding: utf-8 -*-
import numpy;
import matplotlib;
from pandas import read_csv;
from matplotlib import pyplot as plt;

font = {
    'family' : 'SimHei'
};
matplotlib.rc('font', **font);

data = read_csv('./data_1.csv');

d1 = '手机品牌';
d2 = '通信品牌';
v = "月消费";

gb = data.groupby(by=[d1, d2])['月消费（元）'].agg({v: numpy.sum});

d1size = gb.index.levels[0].size;
d2size = gb.index.levels[1].size;

index = numpy.arange(d1size);
colors = ['r', 'g', 'b'];
bsum = index*0.0;

for i in range(0, d2size):
    print(i);
    subgb = gb[v][gb.index.labels[1]==i];
    bar = plt.bar(index, subgb, color=colors[i], bottom=bsum);
    bsum += subgb;

plt.xticks(index+1/2, gb.index.levels[0]);

plt.legend(gb.index.levels[1]);
plt.show();
