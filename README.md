# Graph Analysis on the Shader Codes of Online Video Games 
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Graph creation](#Graph-creation)
* [Scripts Explanation](#Scripts-Explanation)
  * [Graph Analysis](#Graph-Analysis)
  * [Single Game Analysis](#Single-game)
  * [Intergame Analysis](#Inter-game)
* [Useful linkes](#Useful-linkes)
* [Reference](#Reference)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- Graph creation -->
## Graph  
The sample graphs of disassembly shaders can be found in  [Link to the folder](sample_graph/)


<!-- Scripts Explanation -->
## Scripts Explanation

All the scripts are written in python 3.8. To run the script, please lunch a python tools like Anaconda or directly run "python xx.py" 

###  Graph Analysis 
[Link to the folder](Graph_Analysis/)

An example of tfidf vectorization computation for 2 consecutive frame [figure 1](Graph_Analysis/tfid_vector_2consecutiveFrame_FS.py)

An example of WL kernel computation for 2 consecutive frame [figure 1](Graph_Analysis/WL_kernel_2consecutiveFrame_FS.py)

### Single Game Analysis
[Link to the folder](Single_Game/)

1. Evolution of Shader Code Graphs
   [Figue3a](Single_Game/figure3a_barplot_node_FS.py)
	
	An example to analyze plot figure 3a.
	

2. Sudden Change Detection in Frames
   [Figure 8](Graph_Analysis/WL_kernel_2consecutiveFrame_FS.py)
   
   An example for figure 8
   
3. A Frame's Scene Prediction
   [Merge all graphs in one frame as a disjoint graph](Single_Game/merge_allgraph_into1_perframe_GTA5_cs_hs_ls.py)

   An example to merge all graphs in the same frame as one disjoint graph. 

	
### Intergame Analysis
[Link to the folder](Inter_Game/)

1. Frequent subgraph result analysis 

    Frequent subgraph mining utilized the library of gSpan in the link listed in useful link. 

    An example to list the number of frequent subgraphs obtained and their average number of node and edge: Scripts:[figure12](Inter_Game/boxplot_node_intergame.py)

    An example to convert gSpan output text to edgelist and nodelist: Scripts:[conversion](Inter_Game/convert_fsm_file_to_edgelist_hash.py)

    An example to select longest distinct subgraphs from gSpan result: Scripts: [select](Inter_Game/select_distinct_subgraph_labelgame.py)

2. Game clustering 
	
    There are 2 steps in community detection

    Step1: Dataset preparation 
   


    Step2:clustering with PCA feature reduction
    
	[Clutering](Inter_Game/3dplot_Kmeans.py)
	
	This script using Kmenas with PCA feature reduction. The clustering result will be plotted in 3d as table3 figure.  


2. shader efficiency prediction

    There are 2 steps in community detection

    Step1: Dataset preparation

    Step2: Classification 

        [random_forest](Inter_Game/random_forest_crossValidation.py )
    

<!-- Useful linkes -->
## Useful linkes
1. [gSpan](https://github.com/betterenvi/gSpan)
2. [RenderDoc](https://renderdoc.org/)
3. [AMD GPU Toolkit](https://gpuopen.com/introducing-radeon-developer-tool-suite/})
4. [NVIDIA Shader Disassembly library](https://developer.nvidia.com/shader-disasm)
5. [Interpretability-GCN](https://github.com/tsKenneth/interpretable-graph-classification)



<!-- Reference -->
## Reference

