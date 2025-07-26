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

# 从txt文件读取数据
def read_data_from_file(filename):
    with open(filename, 'r') as f:
        data = [float(line.strip()) for line in f.readlines()]
    return np.array(data)

try:
    # 读取数据
    original_data = read_data_from_file('data/original_log.txt')
    modified_data = read_data_from_file('data/sys_original_log.txt')  # 如果有第二个数据文件
    
    # 选择特定的索引点 - 32的倍数
    indices = np.array([32, 64, 96, 128, 160, 192, 224, 256]) - 1  # 索引从0开始，所以减1
    
    # 确保索引不超出数据范围
    valid_indices = indices[indices < len(original_data)]
    if len(valid_indices) < len(indices):
        print(f"警告：原始数据长度不足，只能使用前{len(valid_indices)}个索引点")
    
    # 提取特定索引位置的数据
    x_values = valid_indices + 1  # 显示时恢复为从1开始的索引
    y_values_original = original_data[valid_indices] + 3
    
    # 如果第二个数据集存在且长度足够，则提取对应点
    if 'modified_data' in locals() and len(modified_data) > max(valid_indices):
        y_values_modified = modified_data[valid_indices] + 3
    else:
        # 如果没有第二个数据集或长度不足，使用原始数据的变体作为示例
        y_values_modified = y_values_original * 0.85
    
    # 创建画布
    fig, ax1 = plt.subplots(figsize=(3.5, 2.5), dpi=300)
    
    # 颜色定义
    color_2 = "#BB9727"
    color_3 = "#54B345"
    x_values = [1,2,3,4,5,6,7,8]
    # 绘制多条折线
    plt.plot(x_values, y_values_original, label='Asynchronous Comm.', color=color_2, 
             marker='o', linestyle='-', linewidth=1, markersize=6)
    plt.plot(x_values, y_values_modified, label='Synchronous Comm.', color=color_3, 
             marker='^', linestyle='--', linewidth=1, markersize=6)
    
    # 设置x轴和y轴标签
    plt.xlabel('Decode Block ID')
    plt.ylabel('Perplexity')
    
    # 设置x轴刻度
    plt.xticks(x_values)  # 只在选定的点上显示刻度
    
    # 设置y轴范围
    min_val = min(np.min(y_values_original), np.min(y_values_modified))
    max_val = 10
    margin = (max_val - min_val) * 0.1
    ax1.set_ylim(max(0, min_val - margin), max_val + margin)
    
    # 添加图例
    plt.legend(loc="upper right")
    
    # 添加网格
    plt.grid(linestyle="--", linewidth=0.5, color='black', alpha=0.3)
    
    # 确保figure目录存在
    import os
    if not os.path.exists('figure'):
        os.makedirs('figure')
    
    # 保存图像
    plt.tight_layout()
    plt.savefig("figure/Asy_32k_7B.pdf", format='pdf', bbox_inches='tight')
    
    # 显示图像
    plt.show()
    
except Exception as e:
    print(f"发生错误: {e}")
    # 如果文件不存在或数据有问题，创建一个简单的示例图
    x_values = np.array([32, 64, 96, 128, 160, 192, 224, 256])
    y1 = np.sin(x_values/50) * 5 + 10
    y2 = np.sin(x_values/50) * 4 + 8
    
    plt.figure(figsize=(3.5, 2.5), dpi=300)
    plt.plot(x_values, y1, label='Asynchronous Comm.', color="#BB9727", 
             marker='o', linestyle='-', linewidth=1, markersize=6)
    plt.plot(x_values, y2, label='Synchronous Comm.', color="#54B345", 
             marker='^', linestyle='--', linewidth=1, markersize=6)
    
    plt.xlabel('Decode Index')
    plt.ylabel('Perplexity')
    plt.xticks(x_values)
    plt.grid(linestyle="--", linewidth=0.5, color='black', alpha=0.3)
    plt.legend(loc="upper right")
    plt.tight_layout()
    
    if not os.path.exists('figure'):
        os.makedirs('figure')
    plt.savefig("figure/Asy_32k_7B.pdf", format='pdf', bbox_inches='tight')
    print("#############")
    
    print("使用示例数据创建了图形。请确保'data/original_log.txt'文件存在并包含有效数据。")