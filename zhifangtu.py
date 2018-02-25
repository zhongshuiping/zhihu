import matplotlib;
from pandas import read_csv;
import matplotlib.pyplot as plt;

data = read_csv("./data.csv")
sums = data.groupby('渠道数').sum()



font = {
    'family' : 'SimHei'
}
matplotlib.rc('font', **font);

# plt.plot(data['广告费用'], data['购买用户数'], '.')

# plt.plot(data['广告费用'], data['购买用户数'], 'o')

#plt.plot(data['广告费用'], data['购买用户数'], 'o', color='yellow')
#plt.plot(data['广告费用'], data['购买用户数'], 'o', color='#FFFF00')


# plt.plot(data['渠道数'], data['购买用户数'], 'o', color=(1, 1, 0))
# plt.plot(sums['广告费用'], sums['购买用户数'], 'o')   散点图
plt.bar(sums['广告费用']/10, sums['购买用户数'])    # 直方图

plt.xlabel('广告费用');

plt.ylabel('购买用户数');
plt.grid(True);

plt.show();
