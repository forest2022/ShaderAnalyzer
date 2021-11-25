"""
WL kernel to compare vs 
step1: read all vs 
step2: call the library to compute kernel matrix 

"""
from __future__ import print_function
print(__doc__)
from grakel.kernels import WeisfeilerLehman, VertexHistogram
import os 
import pandas as pd

src='./timeSpy/combine/all_edgelist_hash_distinct/edgelist_hash/distinct_vs/'
dst = './timeSpy/combine/all_edgelist_hash_distinct/WL/distinct_vs/'

os.mkdir(dst)


AVERAGE = []   
for j in range(300):
    graph_single = []
    graph_len = []
    for i in range(12+2*j, 15+2*j, 2):# 2 consecutive frames range
        fnum = '_f'+str(i)+'_'
        print(fnum)
        # read in edgelist files and nodelist files
        edgefiles = [i for i in os.listdir(src+'edgelist/') if i.endswith('_edgelist') and i.find(fnum) !=-1 ]
        nodefiles = [i for i in os.listdir(src+'hash/') if i.endswith('_nodelist') and i.find(fnum) !=-1 ]
        graph_pre=[]
    
       
        for idx in range(len(edgefiles)):
            graph_edge=set()
            # node graph correspondence
            ngc = dict()
            # edge line correspondence
            elc = dict()
            # dictionary of labels for nodes
            node_labels = dict()
            # dictionary of labels for edges
            edge_labels = dict()
            edges_path = src + 'edgelist/' + edgefiles[idx]
            with open(edges_path, "r") as f:
                for (i, line) in enumerate(f, 1):
                    edge = line[:-1].replace(' ', '').split(",")
                    elc[i] = (int(edge[0]), int(edge[1]))
                    graph_edge.add(elc[i])
                   # Graphs.add(graph_single)
            
            node_labels_path= src + 'hash/' + edgefiles[idx].split("edgelist")[0]+ 'nodelist'
            with open(node_labels_path, "r") as f:
                for (i, line) in enumerate(f, 1):
                    node_labels[int(line.split(',')[0])] = line.split(',')[1]
            
            for each in graph_edge:
                edge_labels[each] = 0
            
            graph_single.append([graph_edge, node_labels, edge_labels])
        graph_len.append(len(edgefiles))  
 
        print('----------')
    
    gk = WeisfeilerLehman(n_iter=4, base_graph_kernel=VertexHistogram, normalize=True)
    K_train = gk.fit_transform(graph_single)

    #-------calculate average of 2 consecutive frames--------
    df = pd.DataFrame(K_train)
    real_ave_df = df.loc[ graph_len[0]:,:graph_len[0]-1]
    ave=real_ave_df.mean().mean()
    AVERAGE.append(ave)
    df.to_csv(dst+ str(12+2*j)+'_'+str(14+2*j)+'_'+str(ave)+'_WL_kernel_vs_normalize.csv')
    
df1 = pd.DataFrame(AVERAGE)
df1.to_csv(dst+ 'WL_vs_summary.csv')