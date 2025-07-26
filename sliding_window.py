import matplotlib.pyplot as plt
import numpy as np

# 数据点（假设）
sliding_window_size = [1, 5, 10, 15, 20]  # 横坐标：滑动窗口大小
communication_size = [15, 5.5, 4, 3.7, 3.5]       # 第一条线：通信大小 (MB)
memory_size = [100, 140, 150, 153, 155]             # 第二条线：内存大小 (MB)

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
plt.plot(sliding_window_size, communication_size, marker='o', color='b', label='Communication Size')
plt.plot(sliding_window_size, memory_size, marker='s', color='r', label='Memory Size')

# 设置坐标轴标签和标题
plt.xlabel('Window Size')
plt.ylabel('Percentage')
plt.title('Communication and Memory Percentage vs. Sliding Window Size')

# 添加网格和图例
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

# 设置 X 轴刻度
plt.xticks(sliding_window_size)

# 自适应 Y 轴刻度
min_y = min(min(communication_size), min(memory_size))
max_y = max(max(communication_size), max(memory_size))
y_range = max_y - min_y
tick_count = 6  # 目标刻度数
step_size = y_range / (tick_count - 1)
y_ticks = np.arange(np.floor(min_y), np.ceil(max_y) + step_size, step_size)
plt.yticks(y_ticks)

# 调整布局并保存
plt.tight_layout()
plt.savefig('figure/size_vs_sliding_window.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()