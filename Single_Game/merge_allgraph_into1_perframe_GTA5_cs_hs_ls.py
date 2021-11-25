# -*- coding: utf-8 -*-
"""
union all graphs within a frame into a disjoint one graph (raw shaders)
"""
import os 
import pandas as pd
import networkx as nx

path1  ='./GrandAuto/combine_all/all_unfold_edgelist_hash_cs/'
path2 = './GrandAuto/combine_all/all_unfold_edgelist_hash_ls/'
path3 = './GrandAuto/combine_all/all_unfold_edgelist_hash_hs/'

output = './prepare_GCN_inputdata/'
if(os.listdir(output)==False):
    os.mkdir(output)

for i in range(10, 635, 1 ):
    graph_pre = []
    fnum = 'f'+str(i)
    print(fnum)

    edgefiles =  [i for i in os.listdir(path1+'edgelist/') if i.find('_'+fnum+'_')!=-1 ]  
    if(len(edgefiles) !=0):
        for edge in edgefiles:
            print(edge)
            edge_list = pd.read_csv(path1 + 'edgelist/' + edge, header = None)
            node_list = pd.read_csv(path1 + 'hash/' + edge.replace('edgelist', 'nodelist'), header = None)
            diG = nx.DiGraph()
            for i, elrow in edge_list.iterrows():
                diG.add_edge(elrow[0], elrow[1])
            for i, nodrow  in node_list.iterrows():
                diG.nodes[i]['value'] =nodrow 
                #print(nodrow)
            graph_pre.append(diG)
        
    edgefiles2 =  [i for i in os.listdir(path2+'edgelist/') if i.find('_'+fnum+'_')!=-1 and i.endswith('_edgelist')]  
    if(len(edgefiles2) !=0):
        for edge in edgefiles2:
            edge_list = pd.read_csv(path2 + 'edgelist/' + edge, header = None)
            node_list = pd.read_csv(path2 + 'hash/' + edge.replace('edgelist', 'nodelist'), header = None)
            diG = nx.DiGraph()
            for i, elrow in edge_list.iterrows():
                diG.add_edge(elrow[0], elrow[1])
            for i, nodrow  in node_list.iterrows():
                diG.nodes[i]['value'] =nodrow 
                #print(nodrow)
            graph_pre.append(diG)
            
    edgefiles3 =  [i for i in os.listdir(path3+'edgelist/') if i.find('_'+fnum+'_')!=-1 and i.endswith('_edgelist')]  
    if(len(edgefiles3) !=0):
        for edge in edgefiles3:
            edge_list = pd.read_csv(path3 + 'edgelist/' + edge, header = None)
            node_list = pd.read_csv(path3 + 'hash/' + edge.replace('edgelist', 'nodelist'), header = None)
            diG = nx.DiGraph()
            for i, elrow in edge_list.iterrows():
                diG.add_edge(elrow[0], elrow[1])
            for i, nodrow  in node_list.iterrows():
                diG.nodes[i]['value'] =nodrow 
                #print(nodrow)
            graph_pre.append(diG)

            
    all = nx.disjoint_union_all(graph_pre)
    nx.write_edgelist(all, output +'/'+ fnum+'_rawshader.edgelist', data = False, delimiter =',')
    
    xx = nx.get_node_attributes(all, 'value')
    xx_items = xx.items()
    xx_list = list(xx_items)
    xx_final = []
    for i in range(len(xx_list)):
        xx_final.append(xx_list[i][1][1])
        
    df=pd.DataFrame(xx_final)
    df.to_csv(output+ '/'+ fnum+'_rawshader_NodeLabel.csv', header=False)    