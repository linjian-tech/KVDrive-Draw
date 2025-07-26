import matplotlib.pyplot as plt
import numpy as np

# 数据点（假设）
context_len = [1024, 4096, 8192, 16384, 32768]  # 横坐标：上下文长度
communication_size = [1, 1.2, 1.31, 1.46, 1.50]  # 纵坐标：通信大小（单位可以是 MB 或其他）

# 设置 MobiCom 论文风格
plt.rcParams.update({
    'font.size': 12,           # 字体大小
    'font.family': 'serif',
    'axes.labelsize': 14,      # 坐标轴标签大小
    'axes.titlesize': 16,      # 标题大小
    'legend.fontsize': 12,     # 图例字体大小
    'xtick.labelsize': 12,     # x 轴刻度标签大小
    'ytick.labelsize': 12,     # y 轴刻度标签大小
    'lines.linewidth': 2,      # 折线宽度
    'figure.figsize': (6, 4),  # 图表尺寸（宽 6 英寸，高 4 英寸）
})

# 创建折线图
plt.figure()
plt.plot(context_len, communication_size, marker='o', color='b', label='Communication Size')

# 设置坐标轴标签
plt.xlabel('Context Length')
plt.ylabel('Communication Size (MB)')

# 设置标题（可选，MobiCom 通常在 caption 中说明）
plt.title('Communication Size vs. Context Length')

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend()

# 设置刻度
plt.xticks(context_len)  # 显示所有数据点的刻度
plt.yticks(np.arange(0, max(communication_size) + 1, 1.0))

# 调整布局
plt.tight_layout()

# 保存为高质量图片（MobiCom 推荐 EPS 或 PDF 格式）
plt.savefig('figure/communication_size_vs_context_length.pdf', format='pdf', dpi=300, bbox_inches='tight')

# 显示图表
plt.show()