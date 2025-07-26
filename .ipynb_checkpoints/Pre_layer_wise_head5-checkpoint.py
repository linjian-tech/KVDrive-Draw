import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import os

# 绘图参数全家桶
params = {
    'axes.labelsize': '13',
    'xtick.labelsize': '11',
    'ytick.labelsize': '10',
    'legend.fontsize': '10',
    'figure.figsize': '3.5, 2.5',
    'figure.dpi': '300',
    'figure.subplot.left': '0.15',
    'figure.subplot.right': '0.96',
    'figure.subplot.bottom': '0.14',
    'figure.subplot.top': '0.91',
    'pdf.fonttype': '42',
    'ps.fonttype': '42',
}
pylab.rcParams.update(params)

# 直接定义数据
x_values = list(range(2, 32))  # 表示Block ID
# y_values = np.array([1062, 1200, 1462, 860, 1730, 1924, 2403, 1793, 2488, 881, 800, 1429, 1374, 2665, 2594, 823, 925, 2025, 1959, 1839, 2011, 906, 1034, 976, 1226, 783, 1139, 950, 1650, 925]) * 2/ 1024 /32 /8

y_values = np.array([14, 10,  21, 10, 15, 11, 8, 10, 21, 11, 16, 26,\
                     27, 22, 15, 20, 19, 10, 8, 7, 10, 14, 19, 15, 8, 11,10,6,7,15])*2/32/8


# 创建画布
fig, ax1 = plt.subplots(figsize=(3.5, 2.5), dpi=300)

# 颜色定义
color_2 = "#BB9727"

# 绘制折线
plt.plot(x_values, y_values, color=color_2, 
         marker='o', linestyle='-', linewidth=1, markersize=6)

# 设置x轴和y轴标签
plt.xlabel('Layer Index')
plt.ylabel('Non-overlapping (MB)')

# 设置x轴刻度每隔4显示一次
x_ticks = x_values[::4]  # 每隔4个取一个值
plt.xticks(x_ticks)

# 设置y轴范围
min_val = min(y_values)
max_val = max(y_values)
margin = (max_val - min_val) * 0.1
ax1.set_ylim(max(0, min_val - margin), max_val + margin)

# 添加图例
# plt.legend(loc="upper right")

# 添加网格
plt.grid(linestyle="--", linewidth=0.5, color='black', alpha=0.3)

# 确保figure目录存在
if not os.path.exists('figure'):
    os.makedirs('figure')

# 保存图像
plt.tight_layout()
plt.savefig("figure/Pre_layer_wise_comm_head5.pdf", format='pdf', bbox_inches='tight')

# 显示图像
plt.show()