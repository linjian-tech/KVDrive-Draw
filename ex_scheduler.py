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
    'figure.figsize': '3.5, 2.5',
    'figure.dpi': '300',
    'figure.subplot.left': '0.15',
    'figure.subplot.right': '0.96',
    'figure.subplot.bottom': '0.25',  # 增加底部空间来容纳倾斜标签
    'figure.subplot.top': '0.91',
    'pdf.fonttype': '42',
    'ps.fonttype': '42',
}
pylab.rcParams.update(params)

N = 3
memory_size = [4.1, 4.44, 4.8] 

ind = np.arange(N)    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

# 为每个柱子定义不同的标记样式
hatch_patterns = ["-----", "/////", "|||||", "....."]
colors = [color_2, color_3, color_4, color_5]

fig = plt.figure(1)
ax1 = plt.subplot(111)

# 单独绘制每个柱子，以便使用不同的标记
for i in range(N):
    p = plt.bar(ind[i], memory_size[i], width, color='none', 
                edgecolor=colors[i], hatch=hatch_patterns[i], alpha=.99)

# 设置y轴的范围以突出显示差异
# 计算最小值和最大值，然后设置一个适当的范围
# min_val = min(memory_size) * 0.995  # 略小于最小值
# max_val = max(memory_size) * 1.002  # 略大于最大值
# ax1.set_ylim(min_val, max_val)

plt.ylabel('Tokens/s')
# plt.xlabel('Window Size')

# 设置x轴标签并倾斜45度
plt.xticks(ind, ('FCFS', 'KVDrive', 'Ideal'))
plt.setp(ax1.get_xticklabels(), rotation=30, ha='right', rotation_mode='anchor')

# 给每个柱子添加数值标签，只显示两位小数
# for i, v in enumerate(memory_size):
#     ax1.text(i, v + (max_val - min_val) * 0.01, f'{v:.2f}', 
#              ha='center', va='bottom', fontsize=9)

plt.grid(linestyle="--", linewidth=0.5, color='black', alpha=0.3)

# 添加虚线指示y轴中断
# 创建一个中断的y轴
# def add_axis_break(ax, ypos, d=0.015):
#     # 中断标记
#     kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
#     dx = 0.01
#     ax.plot((-dx, +dx), (ypos-d, ypos+d), **kwargs)
#     ax.plot((-dx, +dx), (ypos-2*d, ypos-4*d), **kwargs)

#     # 水平参考线
#     ax.axhline(min_val, linestyle='--', color='gray', alpha=0.3)
#     ax.axhline(max_val, linestyle='--', color='gray', alpha=0.3)

# # 添加中断标记在y轴上
# add_axis_break(ax1, 0.05)

plt.tight_layout()
plt.savefig("figure/scheduler_8B.pdf", format='pdf', bbox_inches='tight')

plt.show()