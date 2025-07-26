import numpy as np
# import pandas as pd
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

N = 4
memory_size = np.array([5.04, 5.18, 5.60, 4.85]) /4.85 * 2.73
# load_model_structure = (0.856, 0.861, 1.857, 3.636)
# assign_weight = (0.231, 0.256, 0.154, 0.295)

ind = np.arange(N)    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

color_1 = "#F27970"
color_2 = "#BB9727"
color_3 = "#54B345"
color_4 = "#32B897"
color_5 = "#05B9E2"

fig = plt.figure(1)
ax1 = plt.subplot(111)

p1 = plt.bar(ind, memory_size, width, color='none', edgecolor=color_2, hatch="/////", alpha=.99, label='Memory Size')
# p2 = plt.bar(ind, load_model_structure, width,
#              bottom=read_json, color='none', edgecolor=color_2, hatch="/////", alpha=.99)
# p3 = plt.bar(ind, assign_weight, width,
#              bottom=[read_json[i] + load_model_structure[i] for i in range(N)], color='none', edgecolor=color_3, hatch="|||||", alpha=.99)

# hatch="....."
# hatch="xxxxx"

plt.ylabel('Memory Usage (GB)')
plt.xlabel('Context Length')
# plt.legend(loc="upper right")
plt.xticks(ind, ( '70K', '80K', '90K', '100K'))
# plt.legend((p1[0], p2[0], p3[0]), ('Deserialize Model File', 'Load Model Structure', 'Assign Weights'), loc="upper left")

# ax1.set_ylim((0, 10))

plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)

# ax2 = fig.add_axes([0.33,0.43,0.35,0.15])

# plt.grid(linestyle="--", linewidth=0.5, color='black', alpha = 0.3)
# p1 = plt.bar(ind, [read_json[i] * 1000 for i in range(N)], width, color='none', edgecolor=color_1, hatch="-----", alpha=.99)
# plt.xticks(ind, ('', '', '', '', '', ''))

# ax2.set_ylim((0, 2))
# plt.yticks([0, 2], ["0", "2ms"])

plt.savefig("figure/Pre_stability_Memory.pdf", format = 'pdf', bbox_inches='tight')

plt.show()