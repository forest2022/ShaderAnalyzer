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
[Link to the folder](Graph_analysis/)



### Single Game Analysis
[Link to the folder](single_game_analysis/)

1. [Evolution of Shader Code Graphs](graph_analysis/networkx_Count_vertex_arc_of_network.py)
	
	An example to analyze contractNet_2019 number of vertices, arcs and self-loops for figure 2 and 3.
	

2. [Sudden Change Detection in Frames](graph_analysis/igraph_reciprocity_associtativity_connectedComponent_kcore.py)
   
   An example for extract network properties for section 4, 5 and 6
   
3. [A Frame's Scene Prediction](graph_analysis/networkx_vertices_degree_distribution.py)

   An example to calculate number of degree/indegree/outdegree for each vertex in the network. Input is the network edgelist, Output is a csv with the account and corresponding results.

	
### Intergame Analysis

1. Frequent subgraph result analysis 
Frequent subgraph mining utilized the library of gSpan in the link listed in useful link. 
To list the number of frequent subgraphs obtained and their average number of node and edge, the scripts are in []()

2. Game clustering 
	
    There are 2 steps in community detection

    Step1: Dataset preparation 
   
	[find_contract2019_community_multilevel_realEdgeIndex_3mon.py ](community_detection_prediction/community_detection/find_contract2019_community_multilevel_realEdgeIndex_3mon.py )
	
	Note: python igraph library output communities arc list using index instead of real value of nodes. In order to perform matching in next step, it is needed to attach values (which is annual basis index) to each nodes. 

    Step2: Match communities in 3-month dataset and 1-month dataset
    
	[Find_continuous_community1_grow_die_compareREALindex.py](community_detection_prediction/community_detection/Find_continuous_community1_grow_die_compareREALindex.py)
	
	This script makes use of vf2 algorithm for subiomorphism matching. The matching not only consider graph shape but also node values to be matched. 


2. shader efficiency prediction

    There are 2 steps in community detection

   Step1: Dataset preparation

   Scripts [logistic_regression.py](community_detection_prediction/community_prediction/logistic_regression.py)
   and [random_forest.py ](community_detection_prediction/community_prediction/random_forest.py )are used for each time period prediction. 
   The script are generalized, it only requires to input the class 1 and class 0 training features and labels. 
   There is a random selection function in the script to balance class 1 and class 0. It needs to adjust based input data. 

   Step2: Classification 

   Scripts [random_forest_combine_allMonth.py](community_detection_prediction/community_prediction/random_forest_combine_allMonth.py )
    

<!-- Useful linkes -->
## Useful linkes
1. [gSpan](https://github.com/betterenvi/gSpan)
2. [RenderDoc](https://renderdoc.org/)
3. [AMD GPU Toolkit](https://gpuopen.com/introducing-radeon-developer-tool-suite/})
4. [NVIDIA Shader Disassembly library](https://developer.nvidia.com/shader-disasm)
5. [Interpretability-GCN](https://github.com/tsKenneth/interpretable-graph-classification)



<!-- Reference -->
## Reference

