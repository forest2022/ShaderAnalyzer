# -*- coding: utf-8 -*-
"""
Figure 12b
"""

import matplotlib.pyplot as plt
import pandas as pd

path1 = './inter_games/allshader_gspan_output/25percent_result/intergame_all_node_occurance_gspan_fsm2.csv'
df = pd.read_csv(path1 , header = 'infer')

list_to_plot_nodesize = []

game_set = df.drop_duplicates(subset=['gameid'])['gameid']
print(len(game_set))

for frame in game_set:
    print(frame)
    node_sort = df[df.gameid == frame]
    node_sort = node_sort.sort_values(by=['nodesize'])
    node_set = node_sort.drop_duplicates(subset=['nodesize'])['nodesize'].sort_values(ascending=True)
    # x = np.cumsum(node_sort['occurance'])
    # node_sort['cum_occ'] = x
    
    temp1 =pd.DataFrame(columns = ['nodesize', 'occurance', 'frame'])
    for each in node_set:
        temp = node_sort[node_sort.nodesize == each]
        temp1 = temp1.append(temp)
    list_to_plot_nodesize.append(temp1['nodesize'])
    
    
# Create a figure instance
fig = plt.figure(1, figsize=(12,7))
labelsize=25
ax = fig.add_subplot(111)
bp = ax.boxplot(list_to_plot_nodesize)
ax.set_ylabel("Avg # nodes in each frequent subgraph", fontsize=labelsize)
ax.set_xlabel("game ID", fontsize=labelsize)
ax.tick_params(size=labelsize-20)
ax.tick_params(labelsize=labelsize-3) 
ax.xticks=([i+1 for i in range(len(game_set))])
ax.set_xticklabels(ax.set_xticklabels(game_set,ha='center'))

for tick in ax.get_xticklabels():
    tick.set_rotation(60)
