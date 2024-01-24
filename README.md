# Vertex-K-labeling-of-Non-Homogenous-Caterpillar-Graph
**Graph Representation:**
We chose the adjacency list data structure to efficiently represent and store the graph in memory.
The graph structure is stored as an adjacency list, mapping each node to a list of its neighboring nodes and their corresponding weights.

**Vertex Labeling Algorithm:**
We devised a labeling algorithm using a Greedy strategy, making locally optimal choices at each level to find a globally optimum solution.
The algorithm assigns labels to vertices based on a defined k-labeling definition, ensuring distinctive properties of edge weights.

**Graph Traversal:**
Breadth-First Search (BFS) is applied to traverse the graph.
We modified the BFS algorithm to prioritize visiting nodes with no branches after the root, enhancing the exploration strategy.

**Storage of Labels and Weights:**
The labels of vertices and weights of edges are stored separately, ensuring clarity in the representation of the graph.

**Unique Edge Weights:**
A subroutine is implemented to maintain the distinctiveness of edge weights, ensuring uniqueness by carefully adjusting and storing edge weights.

**Mathematical Property Verification:**
The project computes and compares values of vertices and edges (V(G) & E(G)) for each path length (n) against mathematical properties using these 
Total No. of Vertices V= n(n+3)/2 
Total No. of Edges E = V-1
Max Vertex label k= Ceil(V/2)

**Hardware Resources and System Requirements:**
Processor : 11th gen Intel(R) Core(TM) i7-1165G7 @2.80GHz 2.80
Installed RAM : 12.0 GB(11.8 GB usable)
System Type : 64-bit operating system, x64-based processor

**Time Complexity Analysis:**
The time complexity of the algorithm is analyzed, and it is determined to be O(root_nodes * edge_count), considering the dominant factors in the execution.
