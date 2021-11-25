"""
to extract the distinct patterns only, the repeated one will consider as one 
"""

import os
import igraph
from igraph import *

import pandas as pd

import sys
maxInt = sys.maxsize


def cmp_nodes(g2, g1, i2, i1):
    return g1.vs[i1]['value'] == g2.vs[i2]['value']

def cmp_nodes1(g2, g1, i2, i1):
    return g1.vs[i1]['value'] == g2.vs[i2]['value']

src = './new_label_game/shader_project_more_games_lip/output_for_fsm_10per/10percent/'
folders = [i for i in os.listdir(src) if i.endswith('percent') ]  

for folder in folders:
    directoryPath1 = src + folder +'/'
    print(directoryPath1)
    if(os.path.isdir(directoryPath1) == True):
        nodePath = directoryPath1+'hash/'
        edgePath =  directoryPath1+'edgelist/'
        entries = os.listdir(edgePath)
        
        ent1 = []
        catchName1=[]
        for entry in entries:
            if entry.endswith('.txt'):
                print(f' {entry.split(".")[0]}')
                g1 = Graph.Read_Edgelist(edgePath+entry, directed=True) # produce multiDigraph 
                node_list = pd.read_csv(nodePath+entry.split(".")[0]+ ".csv", header = None)
                for i in g1.vs:
                    i['value'] = node_list[1][i.index]
                    # print(i['value'])
                    # print('-----')
                ent1.append(g1)
                catchName1.append(entry)
                    
                    
        g1g2=[] 
        Name12 = []
        count1=0
        delete = []
        
        for x1 in ent1:
            count2=0
            for x2 in ent1:
                if(x1 != x2):
                    result2 = x1.subisomorphic_vf2(x2,node_compat_fn=cmp_nodes)
                    if result2 ==True:
                        # print(x1.vcount())
                        # print(x2.vcount())
                        x1size = x1.vcount()
                        x2size = x2.vcount()
                        if(x1size >= x2size):
                            delete.append(catchName1[count2])
                        else:
                            delete.append(catchName1[count1])
                            
                        #g1g2.append([x1, x2])
                        Name12.append([catchName1[count1], catchName1[count2]])  
                count2+=1
            count1+=1
        
        if len(Name12) != 0: 
            df1=pd.DataFrame(delete)  
            df1.columns=['delete']
            delete_nodup = df1.drop_duplicates()
            delete_nodup = delete_nodup['delete'].tolist()
            remining= set(catchName1) - set(delete_nodup)
            
            df2=pd.DataFrame(Name12)  
            df2.columns=['g1', 'g2']
            #df2['tobedelete'] = df1
            pd.DataFrame(remining).to_csv(directoryPath1+folder.split('_distinct')[0] +"_singleGraphx_subiso_directed.csv", index=False,header=False)
            df2.to_csv(directoryPath1+folder.split('_distinct')[0]+"_matchGraph_name_growth_compareRealIdx_g1g2_subiso_directed.csv", index=False,header=False)