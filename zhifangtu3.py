# -*- coding: utf-8 -*-
import numpy
import matplotlib
from pandas import read_csv
import matplotlib.pyplot as plt

data = read_csv('./data_1.csv')

# gb = data.groupby(
#     by=['省份'],
#     as_index = False
# )['月消费（元）'].sum()
# print(gb)


gc = data.groupby(
    by=['省份'],
    as_index = False
)['月流量（M）'].sum()
print(gc)

font = {
    'family' : 'SimHei'
}
matplotlib.rc('font',**font)

# plt.pie(gb['月消费（元）'], labels=gb['省份'], autopct='%.2f%%')
plt.pie(gc['月流量（M）'], labels=gc['省份'], autopct='%.2f%%')

plt.show()