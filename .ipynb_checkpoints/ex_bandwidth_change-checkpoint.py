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
    'figure.subplot.bottom': '0.14',
    'figure.subplot.top': '0.91',
    'pdf.fonttype': '42',
    'ps.fonttype': '42',
}
pylab.rcParams.update(params)

# 数据准备
N = 5
Bandwidth = np.array([0.3, 0.6, 1.2, 2.4, 4.8])  # x 轴窗口大小
Strawman =   402 * 8/ Bandwidth
Fullcache =   np.array([96, 96, 96, 96, 96 ]) *2
KVDrive =  23 * 8/ Bandwidth  # 通信时间
KVDrive = np.maximum(KVDrive, 96*2)
Strawman = np.maximum(Strawman, 96*2)
# KVDrive[3:5] = 96.9
# KVDrive[4] = 80
# load_model_structure = np.array([0.856, 0.861, 1.857, 3.636]) / 32 * 100  # 加载模型结构百分比
# assign_weight = np.array([0.231, 0.256, 0.154, 0.295]) / 32 * 100  # 分配权重百分比

# x 轴位置
ind = np.arange(N)

# 颜色定义
color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

# 创建画布
fig = plt.figure(1)
ax1 = plt.subplot(111)

# 绘制多条折线
plt.plot(Bandwidth, Strawman, label='InfiniGen', color=color_2, marker='o', linestyle='-', linewidth=1, markersize=8)
plt.plot(Bandwidth, Fullcache, label='Full Cache', color=color_3, marker='^', linestyle='--', linewidth=1, markersize=8)
plt.plot(Bandwidth, KVDrive, label='KVDrive', color=color_4, marker='s', linestyle='-.', linewidth=1, markersize=8)

# 设置 x 轴和 y 轴标签
plt.xlabel('Bandwidth (Gbps)')
plt.ylabel('TBT (ms)')

# 设置 x 轴刻度
# plt.xticks(ind, window_sizes)
ax1.xaxis.set_major_locator(MultipleLocator(1)) 
ax1.set_yscale('log') 
# 设置 y 轴范围
ax1.set_ylim(0, max(max(Strawman), max(Fullcache), max(KVDrive)) * 1.5)  # 动态调整 y 轴上限

# 添加图例
plt.legend(loc="upper left")
ax1.xaxis.set_major_locator(MultipleLocator(1))
# 添加网格
plt.grid(linestyle="--", linewidth=0.5, color='black', alpha=0.3)

# 保存图像
plt.savefig("figure/Ex_bandwidth_8B.pdf", format='pdf', bbox_inches='tight')

# 显示图像
plt.show()