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
print(data)
gb = data.groupby(
    by=['手机品牌']
)['月消费（元）'].agg({
    '月消费': numpy.sum
});

index = numpy.arange(gb['月消费'].size);

#竖向柱形图
plt.bar(index, gb['月消费'], 1, color='G');
plt.show();

plt.bar(index, gb['月消费'], 1, color='G');
plt.xticks(index + 1/2, gb.index);
plt.show();

#横向柱形图
plt.barh(index, gb['月消费'], 1, color='G');
plt.yticks(index + 1/2, gb.index);
plt.show();

