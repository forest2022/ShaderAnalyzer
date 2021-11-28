"""
read all files in folder, list down the hardwares in set or dict, make them a train or test dataset

"""


import os
import pandas as pd
from collections import Counter

src = './new_label_game/shader_project_more_games_lip/'
readPath1 = src+'output_for_fsm_25per/25percent/result/'

folders  = [i for i in os.listdir(readPath1)]
fname = []
feature_all = set()
feature_list = []

for folder in folders:
    files =  [i for i in os.listdir(readPath1 + folder +'/') if i.endswith('.csv')==False]  

    for file in files:
        fname.append(file)
        with open (readPath1 + folder + '/'+ file, 'r') as fin:
            feature = []
            for line in fin:
                if(line.find('nop')==-1 and line.find('label_')==-1):
                    command = line.split(' ')[2].split('~')[1]
#                    print(command)
  
                    sv ="_".join(command.split("_")[0:2])
                    if (sv==' '):
                        print(command)
                    feature_all.add(sv)
                    feature.append(sv)
        feature_cnt = Counter(feature)    
        feature_list.append(feature_cnt)


# print(len(feature_all))
# print(feature_all)

df = pd.DataFrame(columns=list(feature_all))
        
for idx in range(len(feature_list)):
  
    if(len(feature_list[idx]) !=0):
        df1 = pd.DataFrame.from_dict(feature_list[idx], orient='index').reset_index()
        df1 = df1.set_index(['index'])
        tmp = idx
    
        df1.columns = [fname[idx]]
        df1 = df1.T
        df = df.append(df1)
        df = df.fillna(0)

df.to_csv(src + '/training/dataset_detail_25per_gsSan.csv',index=True,header=True)