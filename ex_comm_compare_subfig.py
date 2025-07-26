import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.gridspec as gridspec

# 绘图参数全家桶
params = {
    'axes.labelsize': '13',
    'xtick.labelsize': '11',
    'ytick.labelsize': '10',
    'legend.fontsize': '12',
    'figure.figsize': '14, 8',  # 减小了整体高度
    'figure.dpi': '300',
    'pdf.fonttype': '42',
    'ps.fonttype': '42',
}
pylab.rcParams.update(params)

# 创建主画布
fig = plt.figure(figsize=(14, 8))

# 创建网格布局，顶部留出空间放置图例，减小了行间距
gs = gridspec.GridSpec(4, 1, height_ratios=[0.4, 4, 4, 0.5])  # 减小了顶部和底部的比例

# 顶部用于放置图例的区域
ax_legend = fig.add_subplot(gs[0])
ax_legend.axis('off')  # 隐藏坐标轴

# 底部用于放置共享x轴标签的区域
ax_xlabel = fig.add_subplot(gs[3])
ax_xlabel.axis('off')  # 隐藏坐标轴

# 创建子图网格 (2行4列)，减小行间距和列间距
gs_main = gridspec.GridSpecFromSubplotSpec(2, 4, subplot_spec=gs[1:3], hspace=0.10, wspace=0.30)  # 减小了间距

# 色彩定义
color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

# 预定义图例线条
legend_lines = []
legend_labels = []

model_name = ["LLaMA3-8B-1M on Long_s", "LLaMA3-8B-1M on Long_oracle", "LLaMA3-8B-1M on PG19", "LLaMA2-7B-32k on Long_oracle", "LLaMA3-8B-128k on Long_s", "LLaMA3-8B-128k on Long_oracle", "LLaMA3-8B-128k on PG19", "LLaMA2-7B-32k on PG19"]
Memory_2_list=[[2] for i in range(8)]
Memory_3_list=[[402, 253, 160], [80, 58, 27], [250, 171, 115], [160, 100, 35], 
               [402+3, 253-5, 160+6], [80-2, 58+4, 27+1], [250-6, 171+2, 115-3], [268, 137, 59]]

Memory_4_list=[[23,20,18], [14, 2 ,1], [14, 11, 12],  [27, 6 ,4], [23-1,20-1,18-2], [14+1, 2 ,1], [14-2, 11-1, 12-2], [17, 10, 5]]

Fullcache_list=[[42], [71], [5.12], [48], [42], [71], [5.12], [8.6]]
InfiniGen_list=[[41.4, 40.8, 34.8], [70, 68, 65], [5.9, 7.13, 9.5], [47, 44, 43],[41.4, 40.8, 34.8], [70, 68, 65], [5.9, 7.13, 9.5],[8.9, 9.7, 9.8]]
KVDrive_list=[[41.4, 40.8, 34.8], [70, 68, 65], [5.9, 7.13, 9.5], [47, 44, 43],[41.4, 40.8, 34.8], [70, 68, 65], [5.9, 7.13, 9.5],[8.9, 9.7, 9.8]]

x_list = [(0,450), (0,100),(0,300), (0, 200),(0,450), (0,100),(0,300), (0,300)]
y_list = [(30,45), (60,80), (4,12), (30, 50),(30,45), (60,80), (4,12), (8, 10)]
# 生成8个子图
axes = []
for i in range(2):
    for j in range(4):
        ax = fig.add_subplot(gs_main[i, j])
        axes.append(ax)
        
        # 为每个子图设置标题
        ax.set_title(model_name[i*4+j], fontsize=13)
        
        # 数据准备 - 为每个子图准备不同的数据
        Memory_2 = Memory_2_list[i*4+j]
        Memory_3 = Memory_3_list[i*4+j]
        Memory_4 = Memory_4_list[i*4+j]
        
        Fullcache = Fullcache_list[i*4+j]
        InfiniGen = InfiniGen_list[i*4+j]
        KVDrive = KVDrive_list[i*4+j]
        
        # 绘制数据
        line_full = ax.plot(Memory_2, Fullcache, color=color_2, marker='*', 
                            linestyle='--', linewidth=1, markersize=6)[0]
        line_infini = ax.plot(Memory_3, InfiniGen, color=color_3, marker='p', 
                              linestyle=':', linewidth=1, markersize=6)[0]
        line_kv = ax.plot(Memory_4, KVDrive, color=color_4, marker='s', 
                          linestyle='-.', linewidth=1, markersize=6)[0]
        
        # 只为第一个子图获取图例线条引用
        if i == 0 and j == 0:
            legend_lines = [line_full, line_infini, line_kv]
            legend_labels = ['Full Cache', 'InfiniGen', 'KVDrive']
        
        # 设置x轴范围为0到128
        ax.set_xlim(x_list[i*4+j])
        ax.set_ylim(y_list[i*4+j])
        
        # 设置较大的x轴刻度
        ax.xaxis.set_major_locator(MultipleLocator(64))
        
        # 保持原始代码的宽高比 (3.5:2.5)
        x_left, x_right = ax.get_xlim()
        y_bottom, y_top = ax.get_ylim()
        ax.set_aspect(abs((x_right-x_left)/(y_bottom-y_top))*(2.5/3.5))
        
        # 每个子图设置自己的y轴标签
        y_labels = ['Accuracy', 'Accuracy', 'Perplexity', 'Accuracy', 
                    'Accuracy', 'Accuracy', 'Perplexity', 'Perplexity']
        ax.set_ylabel(y_labels[i*4+j])
        
        # 添加网格 
        ax.grid(linestyle="-", linewidth=0.5, color='gray', alpha=0.3)
        
        # 减少底部间距，使底部更靠近x轴标签
        if i == 1:  # 只对第二行的子图调整
            plt.setp(ax.get_xticklabels(), y=0.05)  # 稍微上移x轴刻度标签

# 在顶部空间创建图例
ax_legend.legend(legend_lines, legend_labels, loc='center', ncol=3, 
                 frameon=False, fontsize=14)

# 添加共享的x轴标签，上移标签位置使其更靠近图表
ax_xlabel.text(0.5, 0.7, 'Communications Volume (MB)', 
               ha='center', va='center', fontsize=15)

# 调整布局，减小顶部和底部的空白
plt.tight_layout()
plt.subplots_adjust(top=0.92, bottom=0.12, hspace=0.2)  # 调整整体的垂直间距

# 保存图像
model_name = ['8_subplots_compact']
for name in model_name:
    plt.savefig(f"figure/Ex_comm_compare_{name}_longmem_oracle.pdf", 
                format='pdf', bbox_inches='tight')

# 显示图像
plt.show()