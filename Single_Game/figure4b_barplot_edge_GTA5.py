# -*- coding: utf-8 -*-
"""
Figure 4b
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import itertools

path1 = './GrandAuto/combine_all/rawdata_nodesize/rawdata_edge_occurance_pass0.csv'
df = pd.read_csv(path1 , header = 'infer')
df['scene']=[0]*len(df['frame'])
edge_sort_0  = df
edge_sort_0 = edge_sort_0.sort_values(by=['edgesize'])
edge_set_0 = set(edge_sort_0.drop_duplicates(subset=['edgesize'])['edgesize'])
#print(edge_set_0)
#print(len(edge_set_0)) # 77
x = np.cumsum(edge_sort_0['occurance'])
edge_sort_0['cum_occ'] = x


path1 = './GrandAuto/combine_all/rawdata_nodesize/rawdata_edge_occurance_pass1.csv'

df1 = pd.read_csv(path1 , header = 'infer')
df1['scene']=[1]*len(df1['frame'])
df = df.append(df1)
edge_sort_1  = df1
edge_sort_1 = edge_sort_1.sort_values(by=['edgesize'])
edge_set_1 = set(edge_sort_1.drop_duplicates(subset=['edgesize'])['edgesize'])
#print(edge_set_1)
#print(len(edge_set_1)) # 77
x = np.cumsum(edge_sort_1['occurance'])
edge_sort_1['cum_occ'] = x



path1 = './GrandAuto/combine_all/rawdata_nodesize/rawdata_edge_occurance_pass2.csv'
#df = df.append(pd.read_csv(path1 , header = 'infer'))
df1 = pd.read_csv(path1 , header = 'infer')
df1['scene']=[2]*len(df1['frame'])
df = df.append(df1)
edge_sort_2  = df1
edge_sort_2 = edge_sort_2.sort_values(by=['edgesize'])
edge_set_2 = set(edge_sort_2.drop_duplicates(subset=['edgesize'])['edgesize'])
#print(edge_set_2)
#print(len(edge_set_2)) # 77
x = np.cumsum(edge_sort_2['occurance'])
edge_sort_2['cum_occ'] = x

path1 = './GrandAuto/combine_all/rawdata_nodesize/rawdata_edge_occurance_pass3.csv'
#df = df.append(pd.read_csv(path1 , header = 'infer'))
df1 = pd.read_csv(path1 , header = 'infer')
df1['scene']=[3]*len(df1['frame'])
df = df.append(df1)
edge_sort_3  = df1
edge_sort_3 = edge_sort_3.sort_values(by=['edgesize'])
edge_set_3 = set(edge_sort_3.drop_duplicates(subset=['edgesize'])['edgesize'])
#print(edge_set_3)
#print(len(edge_set_3)) # 77
x = np.cumsum(edge_sort_3['occurance'])
edge_sort_3['cum_occ'] = x


path1 = './GrandAuto/combine_all/rawdata_nodesize/rawdata_edge_occurance_pass4.csv'
#df =df.append(pd.read_csv(path1 , header = 'infer'))
df1 = pd.read_csv(path1 , header = 'infer')
df1['scene']=[4]*len(df1['frame'])
df = df.append(df1)
edge_sort_4  = df1
edge_sort_4 = edge_sort_4.sort_values(by=['edgesize'])
edge_set_4 = set(edge_sort_4.drop_duplicates(subset=['edgesize'])['edgesize'])
#print(edge_set_4)
#print(len(edge_set_4)) # 77
x = np.cumsum(edge_sort_4['occurance'])
edge_sort_4['cum_occ'] = x


list_to_plot3=[]
list_to_plot4 = []

#edge_sort['cum_occ'] = x
node_0_group=range(1,174)
node_1_group=range(1,174)
node_2_group=range(1,174)
node_3_group=range(1,174)
node_4_group=range(1,174)
## for scene1 
for idx in range(4):
    small_set = set(itertools.islice(node_0_group, idx*20+0, idx*20+20))
    print(small_set)
#   print(each)
    temp1 =pd.DataFrame(columns = ['edgesize', 'occurance', 'frame'])
    for each in  small_set:
        #print(each)
        temp = edge_sort_0[edge_sort_0.edgesize == each]
        temp1 = temp1.append(temp)
        sum_occ = sum(temp1['occurance'])

    list_to_plot3.append(sum_occ)
    
small_set = set(range(81,300))
for each in  small_set:
    temp = edge_sort_0[edge_sort_0.edgesize == each]
    temp1 = temp1.append(temp)
    sum_occ = sum(temp1['occurance'])

list_to_plot3.append(sum_occ)  

list_to_plot3_sum = sum(list_to_plot3)
for each in list_to_plot3:
    tem = each/list_to_plot3_sum
    list_to_plot4.append(tem)      


## for scene2 
for idx in range(4):
    small_set = set(itertools.islice(node_1_group, idx*20+0, idx*20+20))
    print(small_set)
#   print(each)
    temp1 =pd.DataFrame(columns = ['edgesize', 'occurance', 'frame'])
    for each in  small_set:
        #print(each)
        temp = edge_sort_1[edge_sort_1.edgesize == each]
        temp1 = temp1.append(temp)
        sum_occ = sum(temp1['occurance'])

    list_to_plot3.append(sum_occ)
    
small_set = set(range(81,300))
for each in  small_set:
    temp = edge_sort_1[edge_sort_1.edgesize == each]
    temp1 = temp1.append(temp)
    sum_occ = sum(temp1['occurance'])

list_to_plot3.append(sum_occ)   

list_to_plot3_sum2 = sum(list_to_plot3[5:10])
for each in list_to_plot3[5:10]:
    print(each)
    tem = each/list_to_plot3_sum2
    list_to_plot4.append(tem)



#  for scene3 
for idx in range(4):
    small_set = set(itertools.islice(node_2_group, idx*20+0, idx*20+20))
    print(small_set)
#   print(each)
    temp1 =pd.DataFrame(columns = ['edgesize', 'occurance', 'frame'])
    for each in  small_set:
      #  print(each)
        temp = edge_sort_2[edge_sort_2.edgesize == each]
        temp1 = temp1.append(temp)
        sum_occ = sum(temp1['occurance'])

    list_to_plot3.append(sum_occ)
    
small_set = set(range(81,300))
for each in  small_set:
    temp = edge_sort_2[edge_sort_2.edgesize == each]
    temp1 = temp1.append(temp)
    sum_occ = sum(temp1['occurance'])

list_to_plot3.append(sum_occ)      

list_to_plot3_sum2 = sum(list_to_plot3[10:15])
for each in list_to_plot3[10:15]:
    print(each)
    tem = each/list_to_plot3_sum2
    list_to_plot4.append(tem) 

    
    
## for scene4 
for idx in range(4):
    small_set = set(itertools.islice(node_3_group, idx*20+0, idx*20+20))
    print(small_set)
#   print(each)
    temp1 =pd.DataFrame(columns = ['edgesize', 'occurance', 'frame'])
    for each in  small_set:
        #print(each)
        temp = edge_sort_3[edge_sort_3.edgesize == each]
        temp1 = temp1.append(temp)
        sum_occ = sum(temp1['occurance'])

    list_to_plot3.append(sum_occ)
    
small_set = set(range(81,300))
for each in  small_set:
    temp = edge_sort_3[edge_sort_3.edgesize == each]
    temp1 = temp1.append(temp)
    sum_occ = sum(temp1['occurance'])

list_to_plot3.append(sum_occ) 

list_to_plot3_sum2 = sum(list_to_plot3[15:20])
for each in list_to_plot3[15:20]:
    print(each)
    tem = each/list_to_plot3_sum2
    list_to_plot4.append(tem)  


## for scene5
for idx in range(4):
    small_set = set(itertools.islice(node_4_group, idx*20+0, idx*20+20))
    print(small_set)
#   print(each)
    temp1 =pd.DataFrame(columns = ['edgesize', 'occurance', 'frame'])
    for each in  small_set:
       # print(each)
        temp = edge_sort_4[edge_sort_4.edgesize == each]
        temp1 = temp1.append(temp)
        sum_occ = sum(temp1['occurance'])

    list_to_plot3.append(sum_occ)
    
small_set = set(range(81,300))
for each in  small_set:
    temp = edge_sort_4[edge_sort_4.edgesize == each]
    temp1 = temp1.append(temp)
    sum_occ = sum(temp1['occurance'])

list_to_plot3.append(sum_occ)  

list_to_plot3_sum2 = sum(list_to_plot3[20:25])
for each in list_to_plot3[20:25]:
    print(each)
    tem = each/list_to_plot3_sum2
    list_to_plot4.append(tem) 

# Create a figure instance
fig = plt.figure(1, figsize=(15,7))
labelsize=30
# Create an axes instance
ax = fig.add_subplot(111)
ax.xticks=([i for i in range(len(list_to_plot3))])
    
ax.set_xticklabels((   '1-20', '21-40', '41-60','61-80','>80'
                      ,'1-20', '21-40', '41-60','61-80','>80'
                      ,'1-20', '21-40', '41-60','61-80','>80'
                      ,'1-20', '21-40', '41-60','61-80','>80'
                      ,'1-20', '21-40', '41-60','61-80','>80'
              ),ha='center')


dim = len(list_to_plot3)
w =10.75
dimw = w / dim
x = np.arange( len(list_to_plot3))
y = [d for d in list_to_plot4]
ax.bar(x + 0.5 * dimw, y, dimw, bottom=0.001)  
ax.set_yticks(np.arange(0,0.51, step=0.1000))   
plt.yticks([0, 0.1, 0.2,0.3,0.4,0.5],["0%","10%","20%","30%","40%","50%"])  
ax.set_xticks(x + dimw / 2)
for tick in ax.get_xticklabels():
    tick.set_rotation(60)

ax.tick_params(size=15)   
ax.tick_params(labelsize=labelsize)   
ax.set_xlabel('edge count group', fontsize=labelsize)
ax.set_ylabel("% of graphs having specific edge count", fontsize=labelsize)
ax3 = ax.twiny()
new_tick_locations = np.array([0, 0.22, 0.41,0.59,0.78])
ax3.set_xticks(new_tick_locations)
ax3.set_xticklabels(['                   Scene1','                  Scene2',
                     '                   Scene3','                  Scene4',
                     '                   Scene5'])

ax3.tick_params(labelsize=labelsize)
ax3.tick_params(size=labelsize-20)
ax3.grid( linestyle='-', linewidth=2)#
