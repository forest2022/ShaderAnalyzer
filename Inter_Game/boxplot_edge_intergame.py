
"""
Figure 12c plot 
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

path1 = './inter_games/allshader_gspan_output/25percent_result/intergame_all_edge_occurance_gspan_fsm2.csv'
df = pd.read_csv(path1 , header = 'infer')

list_to_plot_edgesize = []

game_set = df.drop_duplicates(subset=['gameid'])['gameid']
print(len(game_set))

for game in game_set:
    print(game)
    edge_sort = df[df.gameid == game]
    edge_sort = edge_sort.sort_values(by=['edgesize'])
    edge_set = edge_sort.drop_duplicates(subset=['edgesize'])['edgesize'].sort_values(ascending=True)
    x = np.cumsum(edge_sort['occurance'])
    edge_sort['cum_occ'] = x
    
    temp1 =pd.DataFrame(columns = ['edgesize', 'occurance', 'frame'])
    for each in edge_set:
        temp = edge_sort[edge_sort.edgesize == each]
        temp1 = temp1.append(temp)

    list_to_plot_edgesize.append(temp1['edgesize'])
    
    
#-------- Create a figure instance-------
fig = plt.figure(1, figsize=(12,7))
labelsize=25
# Create an axes instance
ax = fig.add_subplot(111)
 
bp = ax.boxplot(list_to_plot_edgesize)
ax.set_ylabel("Avg # edges in each frequent subgraph", fontsize=labelsize)
ax.set_xlabel('games ID', fontsize=labelsize)

ax.tick_params(size=labelsize-10)
ax.tick_params(labelsize=labelsize-3) 
frame_set = df.drop_duplicates(subset=['gameid'])['gameid']

ax.tick_params(size=15)
ax.set_xticklabels(ax.set_xticklabels(frame_set,ha='center'))

for tick in ax.get_xticklabels():
    tick.set_rotation(60)

# fig.savefig("figure12_fsm_edge_edgesizespread.png",bbox_inches='tight')    
    