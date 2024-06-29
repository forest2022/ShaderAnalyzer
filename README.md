# Identifying Shader Sub-Patterns for GPU Performance Tuning and Architecture Design
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Graph creation](#Graph-creation)
* [Scripts Explanation](#Scripts-Explanation)
  * [Data Characteristics ](#Graph-Analysis)
  * [Predicting A Frame's Scene](#Single-game)
  * [Tuning for A New Application ](#Inter-game)
* [Useful links](#Useful-linkes)
* [Reference](#Reference)



<!-- ABOUT THE PROJECT -->
## About The Project
This is a description of the code applied for the experiments described in the paper titled Graph Mining and Machine Learning for Shader Codes Analysis to Accelerate GPU Tuning. This is a joint work from Lin Zhao (NTU Singapore), Chai Kiat Yeo (NTU Singapore), Arijit Khan (AAU Denmark), Robby Luo.

<!-- Graph creation -->
## Graph  
The sample graphs of disassembly shaders can be found in  [Link to the folder](sample_graph/)


<!-- Scripts Explanation -->
## Scripts Explanation

All the scripts are written in python 3.8. To run the script, please lunch a python tools like Anaconda or directly run "python xx.py" 

###  Data Characteristics  
[Link to the folder](Graph_Analysis/)

An example of tfidf vectorization computation for 2 consecutive frames:

[tfidf-vectorization computation](Graph_Analysis/tfid_vector_2consecutiveFrame_FS.py)

An example of WL kernel computation for 2 consecutive frames

[WL kernel calculation](Graph_Analysis/WL_kernel_2consecutiveFrame_FS.py)


### Predicting A Frame's Scene
[Link to the folder](Single_Game/)

An example to merge all graphs in the same frame as one disjoint graph. 

[Prepare dataset (Merge all graphs from one frame)](Single_Game/merge_allgraph_into1_perframe_GTA5_cs_hs_ls.py)

GCN with interpretability library  
   
[GCN with interpretability library](https://github.com/tsKenneth/interpretable-graph-classification)

Make use of the existing libraries of Graphsage for scalability study

[Graphsage](https://github.com/diningphil/gnn-comparison)
	
### Tuning for A New Application
[Link to the folder](Inter_Game/)

1. Frequent subgraph result analysis 

   Frequent subgraph mining utilized the library of gSpan in the link 
   
   [gSpan](https://github.com/betterenvi/gSpan) . 

   An example to convert gSpan output text to edgelist and nodelist: 
    
   [Convert gSpan result to graph format](Inter_Game/convert_fsm_file_to_edgelist_hash.py)

   An example to select longest distinct subgraphs from gSpan result. This is to eliminate the smaller subgraphs which are subset of another subgraph:
    
   [Select longest patterns from gSpan result ](Inter_Game/select_distinct_subgraph_labelgame.py)

2. Game clustering 
	
   There are 2 steps for clustering games into groups:

   Step1: Dataset preparation 
    
	[Find max similarity for each pair of games' fsm](Inter_Game/WL_kernel_inter_game_fsm.py)
   
  	[Prepare train dataset](Inter_Game/prepare_dataset_clustering.py)


   Step2: Clustering with PCA feature reduction. This script using K-Means, GaussianMixture and BIRCH with PCA feature reduction
    
	[Clutering](Inter_Game/Kmeans_PCA.py)
	

3. Shader efficiency prediction

    There are 2 steps in shader subgraphs efficiency prediction 

    Step1: Dataset preparation

	[Prepare train dataset](Inter_Game/prepare_dataset_predict_efficiency_select_distinct_hw_used_in_shader.py)
	
    Step2: Classification  
    
	[random_forest](Inter_Game/random_forest_crossValidation.py)

    

<!-- Useful linkes -->
## Useful links
1. [gSpan](https://github.com/betterenvi/gSpan)
2. [RenderDoc](https://renderdoc.org/)
3. [AMD GPU Toolkit](https://gpuopen.com/introducing-radeon-developer-tool-suite/})
4. [NVIDIA Shader Disassembly library](https://developer.nvidia.com/shader-disasm)
5. [Interpretability-GCN](https://github.com/tsKenneth/interpretable-graph-classification)
6. [Graphsage](https://github.com/diningphil/gnn-comparison)



<!-- Reference -->
## Reference

