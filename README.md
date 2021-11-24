# Graph Analysis on the Shader Codes of Online Video Games 
<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
* [Graph creation](#Graph-creation)
  * [Google_bigquery](#Google-bigquery)
  * [Kaggle](#Kaggle)
  * [Github](#github)
//* [Tables Explanation](#Table-Explanation)  
* [Scripts Explanation](#Scripts-Explanation)
  * [Network Extraction](#Network-Extraction)
  * [Graph Analysis](#Graph-Analysis)
  * [Community Detection and Prediction](#Community-Detection-and-Prediction)	
* [Useful linkes](#Useful-linkes)
* [Reference](#Reference)



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- Data Extraction -->
## Data Extraction 
Due to the size limitation, instead of uploading the dataset, we will introduce the extraction method we are using to obtain the data. We also demonstrate a sample arc list and corresponding address hased table split by year and by month (only for Contract Net) in each folder.


<!-- Scripts Explanation -->
## Scripts Explanation

All the scripts are written in python 3.8. To run the script, please lunch a python tools like Anaconda or directly run "python xx.py" 


###  Graph Analysis 
[Link to the folder](Network_extraction/)

The folder contains four folders for transactionNet, traceNet,tokenNet and contractNet arc list and accounts extraction. 

For [transactionNet](Network_extraction/TransactionNet), [traceNet](Network_extraction/TraceNet), [tokenNet](Network_extraction/TokenNet)
 1. Annual graph 
 
    The raw data obtained from Google Bigquery is in annual basis.
    Scripts named as "tracexx.py","tokenxx.py" and "transactionxx.py" are to process annual-based raw data, form the annual based arc list and corresponding hash table. 

 2. Result

    Due to the file size limitation in github, only Year2015 annual arc list and hash table is uploaded as a reference 


For [contractNet](Network_extraction/ContractNet)
1. Annual graph 

   The raw data obtained from Google Bigquery is in annual basis.
   Scripts named as "xx_Annual_xx.py" is to process annual-based raw data, form the annual based arc list and corresponding hash table. 

2. Monthly graph 

   Script named as "xx_Monthly_xx.py" will not only form the arc list and hash table but also help to partition the arc list into different month by matching with the timestamp in raw data.

3. Result

   Due to the file size limitation in github, only ContractNet Year2015 annual arc list and hash table is uploaded as a reference in folder "contractNet_address_hash" and "contractNet_edgelist_example".



### Single Game Analysis
[Link to the folder](Graph_analysis/)

1. [Evolution of Shader Code Graphs](graph_analysis/networkx_Count_vertex_arc_of_network.py)
	
	An example to analyze contractNet_2019 number of vertices, arcs and self-loops for figure 2 and 3.
	

2. [Sudden Change Detection in Frames](graph_analysis/igraph_reciprocity_associtativity_connectedComponent_kcore.py)
   
   An example for extract network properties for section 4, 5 and 6
   
3. [A Frame's Scene Prediction](graph_analysis/networkx_vertices_degree_distribution.py)

   An example to calculate number of degree/indegree/outdegree for each vertex in the network. Input is the network edgelist, Output is a csv with the account and corresponding results.
   
   [Find tokenNet top10 degree accounts](graph_analysis/find_tokenNet_degree_top10.py)

	
### Intergame Analysis

1. Frequent subgraph result analysis 



2. Game clustering 
	
    There are 2 steps in community detection

    Step1: Dataset preparation 
   
	[find_contract2019_community_multilevel_realEdgeIndex_3mon.py ](community_detection_prediction/community_detection/find_contract2019_community_multilevel_realEdgeIndex_3mon.py )
	
	Note: python igraph library output communities arc list using index instead of real value of nodes. In order to perform matching in next step, it is needed to attach values (which is annual basis index) to each nodes. 

    Step2: Match communities in 3-month dataset and 1-month dataset
    
	[Find_continuous_community1_grow_die_compareREALindex.py](community_detection_prediction/community_detection/Find_continuous_community1_grow_die_compareREALindex.py)
	
	This script makes use of vf2 algorithm for subiomorphism matching. The matching not only consider graph shape but also node values to be matched. 


2. shader efficiency prediction

   [Link to the folder](community_detection_prediction/community_prediction/)

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
1. [Github ethereum](https://github.com/blockchain-etl/ethereum-etl)
2. [Google bigquery](https://cloud.google.com/bigquery)
3. [Kaggle](https://www.kaggle.com/bigquery/ethereum-blockchain)

<!-- Reference -->
## Reference
1. Evgeny Medvedev and the D5 team, "Ethereum ETL," https://github.com/blockchain-etl/ethereum-etl, 2018.
2. Ethereum Blockchain, https://www.kaggle.com/bigquery/ethereum-blockchain, 2020
