About The Project
Graph
The sample graphs of disassembly shaders can be found in (sample_graph/)

Scripts Explanation
All the scripts are written in python 3.8. To run the script, please lunch a python tools like Anaconda or directly run "python xx.py"

Data Characteristics(Graph_Analysis/)

An example of tfidf vectorization computation for 2 consecutive frame

tfidf-vectorization computation:Graph_Analysis/tfid_vector_2consecutiveFrame_FS.py

An example of WL kernel computation for 2 consecutive frame: Graph_Analysis/WL_kernel_2consecutiveFrame_FS.py

WL kernel calculation

Predicting A Frame's Scene((Single_Game/)

A Frame's Scene Prediction(Graph_Analysis/WL_kernel_2consecutiveFrame_FS.py)

Prepare dataset (Merge all graphs): Single_Game/merge_allgraph_into1_perframe_GTA5_cs_hs_ls.py

An example to merge all graphs in the same frame as one disjoint graph.

GCN with interpretability library: https://github.com/tsKenneth/interpretable-graph-classification

Make use of the existing libraries for GCN and the result explainability.

Tuning for A New Application (Inter_Game/)

Frequent subgraph result analysis

Frequent subgraph mining utilized the library of gSpan in the link listed in useful link.

An example to convert gSpan output text to edgelist and nodelist:Inter_Game/convert_fsm_file_to_edgelist_hash.py

Convert gSpan result to graph format

An example to select longest distinct subgraphs from gSpan result:

Select longest patterns from gSpan result: Inter_Game/select_distinct_subgraph_labelgame.py

Game clustering

There are 2 steps in community detection

Step1: Dataset preparation

Find max similarity for each pair of games' fsm: Inter_Game/WL_kernel_inter_game_fsm.py

Prepare train dataset: Inter_Game/prepare_dataset_clustering.py

Step2:clustering with PCA feature reduction

Clutering script: Inter_Game/3dplot_Kmeans.py

This script using Kmenas with PCA feature reduction. The clustering result will be plotted in 3d as table3 figure.

shader efficiency prediction

There are 2 steps in community detection

Step1: Dataset preparation

Prepare train dataset

Step2: Classification

random_forest script: Inter_Game/random_forest_crossValidation.py

Useful linkes
1. [gSpan](https://github.com/betterenvi/gSpan)
2. [RenderDoc](https://renderdoc.org/)
3. [AMD GPU Toolkit](https://gpuopen.com/introducing-radeon-developer-tool-suite/})
4. [NVIDIA Shader Disassembly library](https://developer.nvidia.com/shader-disasm)
5. [Interpretability-GCN](https://github.com/tsKenneth/interpretable-graph-classification)
6. [Graphsage](https://github.com/diningphil/gnn-comparison)