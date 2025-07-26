import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# 绘图参数全家桶
params = {
    'axes.labelsize': '13',
    'xtick.labelsize': '11',
    'ytick.labelsize': '10',
    'legend.fontsize': '10',
    'figure.figsize': '5, 2.5',  # 增加宽度以容纳四个柱子
    'figure.dpi': '300',
    'figure.subplot.left': '0.12',
    'figure.subplot.right': '0.96',
    'figure.subplot.bottom': '0.14',
    'figure.subplot.top': '0.91',
    'pdf.fonttype': '42',
    'ps.fonttype': '42',
}
pylab.rcParams.update(params)

# 数据
N = 4

window_1 = [87.35, 55.37, 80.47, 74.12]
window_5 = [94.87, 100, 94.81, 100]
window_10 = [94.87, 100, 98.82, 100]
window_20 = [94.87,100,100,100]


ind = np.arange(N)  # x 轴的位置
width = 0.2  # 每个柱子的宽度（调整为更窄以容纳四个柱子）

# 颜色设置
color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

fig = plt.figure(1)
ax1 = plt.subplot(111)

# 绘制四个并排的柱子
p1 = plt.bar(ind - 1.5 * width, window_1, width, color='none', edgecolor=color_2, hatch="-----", alpha=.99, label='Size=1')
p2 = plt.bar(ind - 0.5 * width, window_5, width, color='none', edgecolor=color_3, hatch="/////", alpha=.99, label='Size=5')
p3 = plt.bar(ind + 0.5 * width, window_10, width, color='none', edgecolor=color_4, hatch="|||||", alpha=.99, label='Size=10')
p4 = plt.bar(ind + 1.5 * width, window_20, width, color='none', edgecolor=color_5, hatch=".....", alpha=.99, label='Size=20')

# 设置标签和刻度
plt.ylabel('Percentage')
plt.xlabel('Layers')
plt.xticks(ind, ('2', '12', '22', '31'))
plt.legend(loc="upper left")

# 设置网格
plt.grid(linestyle="--", linewidth=0.5, color='black', alpha=0.3)

# 保存和显示
plt.savefig("figure/Pre_Recover_Rate.pdf", format='pdf', bbox_inches='tight')
plt.show()