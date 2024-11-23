import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# 绘制密度分布图
path = "H:\组会汇报\论文写作\新论文结构重新构建\城镇化密度直方图.xlsx"
data = pd.read_excel(path, header=0, index_col=0, sheet_name='不同城镇化')

# data = data['Longitude']
ice = data[data['1985_2020']>=0.971926]['Longitude']#密度曲线图读取的数据
nice = ice = data[(data['1985_2020'] >= 0.281786) & (data['1985_2020'] <= 0.971925)]['Longitude']
noice = data[data['1985_2020']<=0.281785]['Longitude']


fig = plt.figure(figsize=(10, 1))
ax2 = fig.add_subplot(111)
ax2.spines['top'].set_visible(False)#设置顶部和右边无框
ax2.spines['right'].set_visible(False)
# ax2.set_xticks([])#隐藏x的刻度刻度
ax2.set_xticklabels([])#隐藏y轴的刻度
# ax2.set_xlim(xmin=20, xmax=50)
# sns.kdeplot(ice, color='#7D9BE5', fill=True)
# sns.kdeplot(noice, color='#F5D78F', fill=True)
plt.hist(ice, color='#7576A1', bins=150, alpha=0.6)
plt.hist(nice, color='#7200A6', bins=150, alpha=0.6)
plt.hist(noice, color='#7800A6', bins=150, alpha=0.6)

plt.xlabel(' ')
plt.ylabel('Density')
# plt.title('Density Distribution Plot')

# 显示图片
plt.show()