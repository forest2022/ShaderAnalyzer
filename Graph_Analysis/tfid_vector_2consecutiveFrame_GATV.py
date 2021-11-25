"""
tf-idf similarity measurement for 2 consecutive frame
"""

from sklearn.feature_extraction.text import TfidfVectorizer
import os 
import pandas as pd

src = './GrandAuto/combine_all/distinct_sp3/distinct_cs1/'

total_sum1= []
count1 = []
ave2 = []
f=[]
writePath = src+'GTAV_2consecutive_CS_tfid_similarity_distinct_new.csv'

for i in range(10, 634, 2):
    fnum1 = '_f'+str(i)+'_'
    fnum2 = 'f'+str(i+2)+'_'
    print(fnum1)
    
    
    edgefile1 = [i for i in os.listdir(src) if i.endswith('.sp3') and i.find(fnum1) !=-1 ]
    edgefile2 = [i for i in os.listdir(src) if i.endswith('.sp3') and i.find(fnum2) !=-1 ]
    if(len(edgefile1)!=0 and len(edgefile2)!=0):
        
        text_files1 = edgefile1+edgefile2
        
        documents = [open(src+ f).read() for f in text_files1]
    
        tfidf = TfidfVectorizer()
        transformed = tfidf.fit_transform(documents)
        #print(tfidf.get_feature_names())
        # no need to normalize, since Vectorizer will return normalized tf-idf
        pairwise_similarity = transformed * transformed.T  
        pairwise_similarity_matrix = pairwise_similarity.todense()
        psm_df = pd.DataFrame(pairwise_similarity_matrix).round(3)
        
        real_ave_df = psm_df.loc[len(edgefile1):, :len(edgefile1)-1]
        real_ave_df = real_ave_df.reset_index(drop=True)
        ave = real_ave_df.mean().mean()   
    
        print(f'ave {ave}')
        print(f'--------end with {fnum1}----------')
        tmp = fnum1.split('_')[1]+'_'+ fnum2.split('_')[0]
        f.append(tmp)
        ave2.append(ave)
        
with open(writePath, 'a') as f2:
    f2.writelines(map("{},{}\n".format,f, ave2))
    