# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:06:39 2021

@author: linzhao2
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 12:07:12 2021

@author: linzhao2

kmean culstering algorithm , 2 cluster is chosen using silhouette method
"""


import pandas as pd


from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.cluster import Birch
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import seaborn as sns
import plotly.graph_objs as go
from plotly import tools
from plotly.subplots import make_subplots
import plotly.offline as py
import plotly.express as px

import time


print(__doc__)
#src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/allshader_gspan_output/25percent_result/WL/maxInCol/maxInCol_traningdataset.csv'
#src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/allshader_gspan_output/25percent_result/WL/maxInCol/maxInCol_trainingdataset.csv'
#src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/allshader_gspan_output/25percent_result/WL/maxInCol/select22_test6/maxInCol_training_22x386_eg1.csv'
#src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/allshader_gspan_output/25percent_result/WL/maxInCol/select22_test6/maxInCol_training_22x386_eg2.csv'
src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/allshader_gspan_output/25percent_result/WL/maxInCol/select24_test4/maxInCol_training_24x570.csv'
#src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/allshader_gspan_output/25percent_result/WL/maxInCol/select26_test2/maxInCol_training_26x449_eg1.csv'
#src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/new_label_game/shader_project_more_games_lip/output_for_fsm/25percent/WL/maxInCol/maxInCol_training.csv'
src1 = 'C:/Users/linzhao2/Documents/graph work in SRDC/shaders/inter_games/total_62_games_gspan_result_2022_02_15/WL/maxInCol_training.csv' 
data = pd.read_csv(src1, header = 'infer')
X= data.T
newX =X
for i in range(781):
    newX= newX.append(X)
X=newX
game_len = data.shape[1]
#-------apply t-SNE for feature reduction

#tsne = TSNE(n_components=3, verbose=1, perplexity=80, n_iter=500000, learning_rate=2)
#tsne_scale_results = tsne.fit_transform(X)
#tsne_df_scale = pd.DataFrame(tsne_scale_results, columns=['tsne1', 'tsne2', 'tsne3'])
#plt.figure(figsize = (10,10))
#plt.scatter(tsne_df_scale.iloc[:,0],tsne_df_scale.iloc[:,1],alpha=0.25, facecolor='lightslategray')
#plt.xlabel('tsne1')
#plt.ylabel('tsne2')
#plt.show()
##
#

labelsize = 30
pca = PCA()
pca.fit(X)
variance = pca.explained_variance_ratio_
var = np.cumsum(np.round(variance, 3))
print(var)

fig, ax = plt.subplots(figsize=(8,5))

ax.grid()

plt.ylabel('cumulative explained variance', fontsize=labelsize-5)
plt.xlabel('# of features', fontsize=labelsize)
#plt.title('PCA feature vs variance analysis', fontsize=labelsize)
x = [i+1 for i in range(len(var))]
plt.xticks(np.arange(1, game_len, step=5))  
plt.yticks(np.arange(0, 1.1, step=0.20))  
#plt.yticks([0, 20, 40,60,80,100],["0%","20%","40%","60%","80%","100%"])  
plt.ylim(0,1.1)
plt.tick_params(labelsize=labelsize)
plt.plot(x,var,marker='o')

pca = PCA(n_components=3)
pca_scale = pca.fit_transform(X)
#pca_df_scale = pd.DataFrame(pca_scale, columns=['pc1','pc2','pc3','pc4','pc5','pc6','pc7','pc8','pc9','pc10'])
#pca_df_scale = pd.DataFrame(pca_scale, columns=['pc1','pc2','pc3','pc4','pc5','pc6'])
#pca_df_scale = pd.DataFrame(pca_scale, columns=['pc1','pc2','pc3','pc4','pc5'])
pca_df_scale = pd.DataFrame(pca_scale, columns=['pc1','pc2','pc3'])
#pca_df_scale = pd.DataFrame(pca_scale, columns=['pc1','pc2','pc3','pc4','pc5','pc6', 'pc7'])




#--------------apply kmeans
sse = []
k_list = range(1, game_len)
for k in k_list:
    km = KMeans(n_clusters=k)
    km.fit(pca_df_scale)
    sse.append([k, km.inertia_])
    
pca_results_scale = pd.DataFrame({'Cluster': range(1,game_len), 'SSE': sse})
fig, ax2 = plt.subplots(figsize=(8,5))
#ax2.grid()
plt.plot(pd.DataFrame(sse)[0], pd.DataFrame(sse)[1], marker='o')
#plt.title('Number of Clusters vs Inertia', fontsize=labelsize)
plt.xlabel('# clusters', fontsize=labelsize)
plt.ylabel('Within-cluster variance', fontsize=labelsize)
#plt.xticks([1,4,7,10,13,16,19,22,25,28])
plt.xticks(np.arange(0, game_len, step=10))  
plt.tick_params(labelsize=labelsize)


plt.figure(figsize = (8,5))
n_cluster =4

print(f'kmenas:{time.perf_counter()}')
kmeans_pca_scale = KMeans(n_clusters=n_cluster, n_init=100, max_iter=300, init='k-means++', random_state=2).fit(pca_df_scale)
print(f'kmenas:{time.perf_counter()}')
labels_pca_scale = kmeans_pca_scale.labels_
#print('KMeans PCA Scaled Silhouette Score: {}'.format(silhouette_score(pca_df_scale, kmeans_pca_scale.labels_, metric='euclidean')))
centers= kmeans_pca_scale.cluster_centers_
clusters_pca_scale = pd.concat([pca_df_scale, pd.DataFrame({'pca_clusters':labels_pca_scale})], axis=1)



print(f'GaussianMixture:{time.perf_counter()}')
model_Gaussian = GaussianMixture(n_components=4)
model_Gaussian.fit(pca_df_scale)
yhat_Gaussian = model_Gaussian.predict(pca_df_scale)
print(f'GaussianMixture:{time.perf_counter()}')

print(f'Birch:{time.perf_counter()}')
Birch_model = Birch(threshold=0.01, n_clusters=4)
# fit the model
Birch_model.fit(pca_df_scale)
# assign a cluster to each example
yhat_labels = Birch_model.predict(pca_df_scale)
print(f'Birch:{time.perf_counter()}')


Birch_silhouette_values = silhouette_samples(pca_df_scale, yhat_labels)
    

size2 = 30

sns.scatterplot(clusters_pca_scale.iloc[:,0],clusters_pca_scale.iloc[:,1], hue=labels_pca_scale, palette='Set1', s=400, alpha=1).set_title('KMeans clustering with PCA feature reduction', fontsize=25)
plt.scatter(centers[:, 0], centers[:, 1], marker="x",c='black', s=400, alpha=1);
plt.legend(loc="upper right",markerscale=3., fontsize=20)
plt.ylabel('PC2', fontsize=size2)
plt.xlabel('PC1', fontsize=size2)
plt.tick_params(labelsize=size2)

plt.show()

#plt.save('pca_kmeans_group.png')

silhouette_avg = silhouette_score(pca_df_scale, labels_pca_scale)
print("For n_clusters =", n_cluster,
      "The average silhouette_score is :", silhouette_avg)

# Compute the silhouette scores for each sample
sample_silhouette_values = silhouette_samples(pca_df_scale, labels_pca_scale)

