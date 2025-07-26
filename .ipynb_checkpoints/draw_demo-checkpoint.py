import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 步骤1: 创建示例tensor向量
tensor_vector = torch.tensor([2, 3, 0, 5, 0, 7, 0, 8, 9, 0])
print("原始向量:", tensor_vector)

# 步骤2: 保存向量到文本文件
os.makedirs('data', exist_ok=True)
file_path = 'data/vector_data.txt'

with open(file_path, 'w') as f:
    for value in tensor_vector:
        f.write(f"{value.item()}\n")

print(f"向量已保存到 {file_path}")

# 步骤3: 从文本文件读取数据
def read_vector_from_file(filename):
    with open(filename, 'r') as f:
        data = [float(line.strip()) for line in f.readlines()]
    return np.array(data)

# 读取向量数据
vector_data = read_vector_from_file(file_path)
print("从文件读取的向量:", vector_data)

# 步骤4: 创建热力图数据
# 将向量转换为二进制标记 (>0 为 1, =0 为 0)
binary_data = (vector_data > 0).astype(int)
print("二进制标记 (1=非零, 0=零):", binary_data)

# 步骤5: 绘制热力图
plt.figure(figsize=(10, 2))

# 创建自定义颜色图 - 蓝色为非零值，灰色为零值
cmap = sns.color_palette(["lightgray", "#3498db"])

# 绘制热力图
ax = sns.heatmap([binary_data], cmap=cmap, cbar=False, 
                 linewidths=1, linecolor='white',
                 square=True, annot=[vector_data], fmt=".1f",
                 annot_kws={"size": 12})

# 设置x轴标签为索引
plt.xticks(np.arange(len(vector_data))+0.5, range(len(vector_data)))
plt.yticks([])  # 隐藏y轴刻度

# 添加标题和标签
plt.title("向量可视化: 蓝色=非零元素, 灰色=零元素")
plt.xlabel("索引")

# 让图形更紧凑
plt.tight_layout()

# 保存图像
plt.savefig("vector_heatmap.png", dpi=300, bbox_inches='tight')

# 显示图形
plt.show()

# 步骤6: 另一种可视化方式 - 单行矩阵形式
plt.figure(figsize=(10, 1.5))
ax = plt.gca()

# 创建单行矩阵形式的数据
matrix_data = binary_data.reshape(1, -1)

# 绘制矩阵
for i in range(len(vector_data)):
    color = "#3498db" if vector_data[i] > 0 else "lightgray"
    rect = plt.Rectangle((i, 0), 1, 1, linewidth=1, 
                         edgecolor='white', facecolor=color)
    ax.add_patch(rect)
    # 添加原始值作为文本
    plt.text(i + 0.5, 0.5, f"{vector_data[i]:.1f}", 
             horizontalalignment='center', verticalalignment='center')

# 设置坐标轴
ax.set_xlim(0, len(vector_data))
ax.set_ylim(0, 1)
plt.xticks(np.arange(len(vector_data)) + 0.5, range(len(vector_data)))
plt.yticks([])

# 添加标题
plt.title("向量元素可视化: 蓝色=非零元素, 灰色=零元素")
plt.xlabel("索引")

# 保存图像
plt.savefig("vector_matrix.png", dpi=300, bbox_inches='tight')

# 显示图形
plt.tight_layout()
plt.show()