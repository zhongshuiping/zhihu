# -*- coding: utf-8 -*-
import matplotlib;
from pandas import read_csv;
from matplotlib import pyplot as plt;

font = {
    'family' : 'SimHei'
};
matplotlib.rc('font', **font);

data = read_csv('./data_1.csv');

plt.hist(data['购买用户数']);
plt.show();

plt.hist(data['购买用户数'], bins=20);
plt.show();

plt.hist(data['购买用户数'], bins=20, cumulative=True);
plt.show();
