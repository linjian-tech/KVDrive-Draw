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
    'figure.dpi':'300',
    'figure.subplot.left':'0.15',
    'figure.subplot.right':'0.96',
    'figure.subplot.bottom':'0.14',
    'figure.subplot.top':'0.91',
    'pdf.fonttype':'42',
    'ps.fonttype':'42',
}
pylab.rcParams.update(params)

N = 5
memory_size = np.array([0.61, 0.25, 0.14, 0.056, 0.035])/35*23*1000
memory_size[0] = 402

# 计算相对于baseline的倍数
baseline = memory_size[0]
ratios = [baseline/val for val in memory_size]  # 倒数关系，因为值越小越好

ind = np.arange(N)    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

fig = plt.figure(1)
ax1 = plt.subplot(111)

p1 = plt.bar(ind, memory_size, width, color='none', edgecolor=color_2, hatch="-----", alpha=.99)

# 在每个柱子上方添加倍数标签
for i, (val, ratio) in enumerate(zip(memory_size, ratios)):
    if i == 0:
        ax1.text(i, val + 0.02, f'1×', ha='center', va='bottom', fontsize=9)
    else:
        ax1.text(i, val + 0.02, f'{ratio:.1f}×', ha='center', va='bottom', fontsize=9)

plt.ylabel('Non-overlapping (MB)')
plt.xlabel('Window Size')
# plt.legend(loc="upper right")
plt.xticks(ind, ('1', '5', '10', '20', '40'))

plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)

# 设置y轴上限，确保标签可见
y_max = max(memory_size) * 1.2
ax1.set_ylim(0, y_max)

plt.savefig("figure/Pre_sliding_window_Comm.pdf", format = 'pdf', bbox_inches='tight')

plt.show()