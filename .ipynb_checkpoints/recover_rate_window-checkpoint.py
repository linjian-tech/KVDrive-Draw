import matplotlib.pyplot as plt
import numpy as np

# 数据点（假设）
# sliding_window_size = [1, 5, 10, 20]  # 横坐标：滑动窗口大小
# layer_2 = [87.35, 94.87, 94.87, 94.87]
# layer_12 = [55.37, 100, 100, 100]
# layer_22 = [80.47, 94.81, 98.82, 100]
# layer_31 = [74.12,100,100,100]

layer_index = [2, 12, 22, 31]  # 横坐标：滑动窗口大小
window_1 = [87.35, 55.37, 80.47, 74.12]
window_5 = [94.87, 100, 94.81, 100]
window_10 = [94.87, 100, 98.82, 100]
window_20 = [94.87,100,100,100]

# 设置 MobiCom 论文风格
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',  # 使用 serif，避免字体问题
    'axes.labelsize': 14,
    'axes.titlesize': 16,
    'legend.fontsize': 12,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'lines.linewidth': 2,
    'figure.figsize': (6, 4),
})

# 创建折线图
plt.figure()
plt.plot(layer_index, window_1, marker='o', color='b', label='Window Size=1')
plt.plot(layer_index, window_5, marker='s', color='r', label='Window Size=5')
plt.plot(layer_index, window_10, marker='.', color='y', label='Window Size=10')
plt.plot(layer_index, window_20, marker='*', color='g', label='Window Size=20')

# 设置坐标轴标签和标题
plt.xlabel('Layer Index')
plt.ylabel('Recover Rate')
plt.title('Recover Rate vs. Sliding Window Size')

# 添加网格和图例
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 设置 X 轴刻度
plt.xticks(layer_index)

# 自适应 Y 轴刻度
# min_y = min(min(layer_2), min(layer_12),min(layer_22), min(layer_31))
# max_y = max(max(layer_2), max(layer_12), max(layer_22), max(layer_31))
min_y = 0
max_y = 100
y_range = max_y - min_y
tick_count = 5  # 目标刻度数
step_size = y_range / (tick_count - 1)
y_ticks = np.arange(np.floor(min_y), np.ceil(max_y) + step_size, step_size)
plt.yticks(y_ticks)

# 调整布局并保存
plt.tight_layout()
plt.savefig('figure/recover_rate_vs_sliding_window.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()