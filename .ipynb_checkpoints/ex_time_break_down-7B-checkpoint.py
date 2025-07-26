# # import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import matplotlib.pylab as pylab
# # from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# # # 绘图参数全家桶
# # params = {
# #     'axes.labelsize': '13',
# #     'xtick.labelsize': '11',
# #     'ytick.labelsize': '10',
# #     'legend.fontsize': '10',
# #     'figure.figsize': '3.5, 2.5',
# #     'figure.dpi':'300',
# #     'figure.subplot.left':'0.15',
# #     'figure.subplot.right':'0.96',
# #     'figure.subplot.bottom':'0.14',
# #     'figure.subplot.top':'0.91',
# #     'pdf.fonttype':'42',
# #     'ps.fonttype':'42',
# # }
# # pylab.rcParams.update(params)

# # N = 4
# # read_json = (0.001, 0.001, 0.001, 0.001)
# # load_model_structure = (0.856, 0.861, 1.857, 3.636)
# # assign_weight = (0.231, 0.256, 0.154, 0.295)

# # ind = np.arange(N)    # the x locations for the groups
# # width = 0.5       # the width of the bars: can also be len(x) sequence

# # color_1 = "#F27970"
# # color_2 = "#BB9727"
# # color_3 = "#54B345"
# # color_4 = "#32B897"
# # color_5 = "#05B9E2"

# # fig = plt.figure(1)
# # ax1 = plt.subplot(111)

# # p1 = plt.bar(ind, read_json, width, color='none', edgecolor=color_4, hatch="-----", alpha=.99)
# # p2 = plt.bar(ind, load_model_structure, width,
# #              bottom=read_json, color='none', edgecolor=color_2, hatch="/////", alpha=.99)
# # p3 = plt.bar(ind, assign_weight, width,
# #              bottom=[read_json[i] + load_model_structure[i] for i in range(N)], color='none', edgecolor=color_3, hatch="|||||", alpha=.99)

# # # hatch="....."
# # # hatch="xxxxx"

# # plt.ylabel('Lantecy (s)')

# # plt.xticks(ind, ('4096', '8192', '16384', '32768'), rotation=30)
# # plt.legend((p1[0], p2[0], p3[0]), ('KV Selection', 'Local KV Management', 'Approximate Attention'), loc="upper left")

# # ax1.set_ylim((0, 10))

# # plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)

# # ax2 = fig.add_axes([0.33,0.43,0.35,0.15])

# # plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)
# # p1 = plt.bar(ind, [read_json[i] * 1000 for i in range(N)], width, color='none', edgecolor=color_3, hatch="-----", alpha=.99)
# # # plt.xticks(ind, ('', '', '', '', '', ''))

# # ax2.set_ylim((0, 2))
# # plt.yticks([0, 2], ["0", "2ms"])

# # plt.savefig("figure/Ex_break_time.pdf", format = 'pdf', bbox_inches='tight')

# # plt.show()


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.pylab as pylab
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# # 绘图参数全家桶
# params = {
#     'axes.labelsize': '13',
#     'xtick.labelsize': '11',
#     'ytick.labelsize': '10',
#     'legend.fontsize': '10',
#     'figure.figsize': '3.5, 2.5',  # 可能需要调整以适应横向图
#     'figure.dpi':'300',
#     'figure.subplot.left':'0.15',
#     'figure.subplot.right':'0.96',
#     'figure.subplot.bottom':'0.14',
#     'figure.subplot.top':'0.91',
#     'pdf.fonttype':'42',
#     'ps.fonttype':'42',
# }
# pylab.rcParams.update(params)

# N = 4
# Encode = (0, 0, 0.001, 0.001,)
# Trans = (0, 0, 0, 32)
# Comp = (96.5, 152, 96.5, 96.5,)  
# Decode = (0, 0, 0.001, 0.001, )

# ind = np.arange(N)    # the y locations for the groups (横向条形图中的y位置)
# width = 0.5       # the height of the bars: can also be len(x) sequence

# color_1 = "#F27970"
# color_2 = "#BB9727"
# color_3 = "#54B345"
# color_4 = "#32B897"
# color_5 = "#05B9E2"

# fig = plt.figure(1)
# ax1 = plt.subplot(111)

# # 颠倒顺序，使1024在顶部
# labels = ('Full Cache', 'Quantization', 'BW=2Gbps', 'BW=1Gbp',)
# ind = np.arange(N)

# # 使用barh而不是bar来创建横向条形图
# # 创建横向条形图
# p1 = ax1.barh(ind, Encode, width, color='none', edgecolor=color_5, hatch="-----", alpha=.99)  # 使用纯色

# # 如果后面几组数据不为零，则添加它们
# if any(Trans) or any(Comp) or any(Decode):
#     p2 = ax1.barh(ind, Trans, width,
#                 left=Encode, color='none', edgecolor=color_2, hatch="/////", alpha=.99)
#     p3 = ax1.barh(ind, Comp, width,
#                 left=[Encode[i] + Trans[i] for i in range(N)], color='none', edgecolor=color_3, hatch="|||||", alpha=.99)
#     p4 = ax1.barh(ind, Decode, width,
#                 left=[Encode[i] + Trans[i] + Comp[i] for i in range(N)], color='none', edgecolor=color_4, hatch="xxxxx", alpha=.99)
    
#     # 设置完整图例
#     plt.legend((p1[0], p2[0], p3[0], p4[0]), 
#               ('Serial.', 'Extra Comm.', 'Comp.', 'Deserial.'), 
#               loc="lower right")
# else:
#     # 如果只有Encode有数据，则不需要图例
#     pass

# # 添加1.69x标注和箭头（与图像匹配）


# # 设置坐标轴
# plt.xlabel('Latency (ms)')  # 原图没有x轴标签
# plt.yticks(ind, labels)

# # 设置x轴范围和刻度
# ax1.set_xlim((0, 170))
# ax1.set_xticks([0, 40, 80, 120, 160])

# # 为子图设置新的位置 - 可能需要调整以适应横向布局
# # ax2 = fig.add_axes([0.33, 0.65, 0.35, 0.15])  # 调整子图位置

# # 为子图添加网格线和数据
# # plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3, axis='x')
# # p1 = ax2.barh(ind, [read_json[i] * 1000 for i in range(N)], width, color='none', edgecolor=color_3, hatch="-----", alpha=.99)

# # 设置子图的x轴范围和刻度
# # ax2.set_xlim((0, 2))
# # plt.xticks([0, 2], ["0", "2ms"])
# # plt.yticks([])  # 隐藏子图的y轴刻度

# plt.savefig("figure/Ex_break_time.pdf", format = 'pdf', bbox_inches='tight')

# plt.show()


# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.pylab as pylab
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# # 绘图参数全家桶
# params = {
#     'axes.labelsize': '13',
#     'xtick.labelsize': '11',
#     'ytick.labelsize': '10',
#     'legend.fontsize': '10',
#     'figure.figsize': '3.5, 2.5',
#     'figure.dpi':'300',
#     'figure.subplot.left':'0.15',
#     'figure.subplot.right':'0.96',
#     'figure.subplot.bottom':'0.14',
#     'figure.subplot.top':'0.91',
#     'pdf.fonttype':'42',
#     'ps.fonttype':'42',
# }
# pylab.rcParams.update(params)

# N = 4
# read_json = (0.001, 0.001, 0.001, 0.001)
# load_model_structure = (0.856, 0.861, 1.857, 3.636)
# assign_weight = (0.231, 0.256, 0.154, 0.295)

# ind = np.arange(N)    # the x locations for the groups
# width = 0.5       # the width of the bars: can also be len(x) sequence

# color_1 = "#F27970"
# color_2 = "#BB9727"
# color_3 = "#54B345"
# color_4 = "#32B897"
# color_5 = "#05B9E2"

# fig = plt.figure(1)
# ax1 = plt.subplot(111)

# p1 = plt.bar(ind, read_json, width, color='none', edgecolor=color_4, hatch="-----", alpha=.99)
# p2 = plt.bar(ind, load_model_structure, width,
#              bottom=read_json, color='none', edgecolor=color_2, hatch="/////", alpha=.99)
# p3 = plt.bar(ind, assign_weight, width,
#              bottom=[read_json[i] + load_model_structure[i] for i in range(N)], color='none', edgecolor=color_3, hatch="|||||", alpha=.99)

# # hatch="....."
# # hatch="xxxxx"

# plt.ylabel('Lantecy (s)')

# plt.xticks(ind, ('4096', '8192', '16384', '32768'), rotation=30)
# plt.legend((p1[0], p2[0], p3[0]), ('KV Selection', 'Local KV Management', 'Approximate Attention'), loc="upper left")

# ax1.set_ylim((0, 10))

# plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)

# ax2 = fig.add_axes([0.33,0.43,0.35,0.15])

# plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)
# p1 = plt.bar(ind, [read_json[i] * 1000 for i in range(N)], width, color='none', edgecolor=color_3, hatch="-----", alpha=.99)
# # plt.xticks(ind, ('', '', '', '', '', ''))

# ax2.set_ylim((0, 2))
# plt.yticks([0, 2], ["0", "2ms"])

# plt.savefig("figure/Ex_break_time.pdf", format = 'pdf', bbox_inches='tight')

# plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# 绘图参数全家桶
params = {
    'axes.labelsize': '13',
    'xtick.labelsize': '11',
    'ytick.labelsize': '10',
    'legend.fontsize': '10',
    'figure.figsize': '3.5, 2.5',  # 可能需要调整以适应横向图
    'figure.dpi':'300',
    'figure.subplot.left':'0.15',
    'figure.subplot.right':'0.96',
    'figure.subplot.bottom':'0.14',
    'figure.subplot.top':'0.91',
    'pdf.fonttype':'42',
    'ps.fonttype':'42',
}
pylab.rcParams.update(params)

N = 3
Encode = (0, 0, 0.001)
Trans = (0, 0,  80)
Comp = (96.5*2,  96.5*2, 96.5*2,)  
Decode = (0, 0, 0.001, )

ind = np.arange(N)    # the y locations for the groups (横向条形图中的y位置)
width = 0.5       # the height of the bars: can also be len(x) sequence

color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

fig = plt.figure(1)
ax1 = plt.subplot(111)

# 颠倒顺序，使1024在顶部
labels = ('Full Cache', 'BW=1Gbps', 'BW=0.5Gbps',)
ind = np.arange(N)

# 使用barh而不是bar来创建横向条形图
# 创建横向条形图
p1 = ax1.barh(ind, Encode, width, color='none', edgecolor=color_5, hatch="-----", alpha=.99)  # 使用纯色

# 如果后面几组数据不为零，则添加它们
if any(Trans) or any(Comp) or any(Decode):
    p2 = ax1.barh(ind, Trans, width,
                left=Encode, color='none', edgecolor=color_2, hatch="/////", alpha=.99)
    p3 = ax1.barh(ind, Comp, width,
                left=[Encode[i] + Trans[i] for i in range(N)], color='none', edgecolor=color_3, hatch="|||||", alpha=.99)
    p4 = ax1.barh(ind, Decode, width,
                left=[Encode[i] + Trans[i] + Comp[i] for i in range(N)], color='none', edgecolor=color_4, hatch="xxxxx", alpha=.99)
    
    # 设置完整图例
    plt.legend((p1[0], p2[0], p3[0], p4[0]), 
              ('Serial.', 'Extra Comm.', 'Comp.', 'Deserial.'), 
              loc="lower right")
else:
    # 如果只有Encode有数据，则不需要图例
    pass

# 添加1.69x标注和箭头（与图像匹配）


# 设置坐标轴
plt.xlabel('Latency (ms)')  # 原图没有x轴标签
plt.yticks(ind, labels)

# 设置x轴范围和刻度
ax1.set_xlim((0, 400))
ax1.set_xticks([0, 100, 200, 300, 400])

# 为子图设置新的位置 - 可能需要调整以适应横向布局
# ax2 = fig.add_axes([0.33, 0.65, 0.35, 0.15])  # 调整子图位置

# 为子图添加网格线和数据
# plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3, axis='x')
# p1 = ax2.barh(ind, [read_json[i] * 1000 for i in range(N)], width, color='none', edgecolor=color_3, hatch="-----", alpha=.99)

# 设置子图的x轴范围和刻度
# ax2.set_xlim((0, 2))
# plt.xticks([0, 2], ["0", "2ms"])
# plt.yticks([])  # 隐藏子图的y轴刻度

plt.savefig("figure/Ex_break_time_7B.pdf", format = 'pdf', bbox_inches='tight')

plt.show()