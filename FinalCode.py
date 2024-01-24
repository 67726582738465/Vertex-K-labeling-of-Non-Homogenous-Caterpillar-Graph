import math
from math import ceil  #Importing CEIl
import pandas as pd
class Vertex:
    def __init__(self, weight, linked_node):
        self.weight = weight  # Initialize weight of the vertex
        self.linked_node = linked_node  # Initialize linked node

    def __str__(self):
        return f"({self.linked_node},{self.weight})"  # Return formatted string representation of the Vertex

# Function to label a graph based on given parameters
def label_graph(root_nodes, max_label):
    adjacency_list = {}  # Initialize an empty adjacency list to store graph connections
    weight = 3  # Initialize weight value
    adjacency_list[1] = [Vertex(2, 1)]  # Initialize the first node with its linked node and weight
    edge_count = 3  # Initialize the edge count
    root_node = 2  # Initialize the root node 
    i = 1  # Initialize a counter

    used_weight = -1  # Initialize a flag to track used weight

    # Loop to create the adjacency list for the graph
    while i < root_nodes:
        j = 0
        # Loop to populate the adjacency list
        while j < edge_count:
            next_link = weight - root_node  # Calculate the next linked node
            if weight != used_weight:
                vertex = Vertex(weight, next_link)  # Create a new vertex with weight and linked node
                if root_node not in adjacency_list:
                    adjacency_list[root_node] = []  # Create a new list for the root node if it doesn't exist
                adjacency_list[root_node].append(vertex)  # Append the new vertex to the root node's list
            weight += 1  # Increment weight
            j += 1

        edge_count += 1  # Increment edge count
        if i == root_nodes - 2:
            used_weight = max_label + root_node  # Update the used weight
            adjacency_list[max_label] = [Vertex(max_label + root_node, root_node)]  # Add a vertex to the adjacency list
            root_node = max_label  # Update the root node
        else:
            root_node = weight - root_node  # Update the root node

        i += 1  # Increment counter

    return adjacency_list  # Return the final adjacency list of the graph

root_nodes = 7   # Number of root nodes
total_nodes = root_nodes * (root_nodes + 3)  / 2 # Calculate total nodes in the graph changed here
max_label = math.ceil(total_nodes / 2)  # Calculate the maximum label for the graph changed here
total_edges = total_nodes - 1
adjacency_list = label_graph(root_nodes, max_label)  # Generate the adjacency list for the graph

# Print various details of the graph
print('Max Label', max_label)
print('Root Nodes', root_nodes)
print('Total Nodes', total_nodes)
print('Total Edges', total_edges)
# Function to format the output
def format_output(input_list):
    formatted_output = []
    for idx, item in enumerate(input_list):
        if isinstance(item, tuple):
            for vertex in item[1]:
                formatted_output.append(f"({item[0]},{str(vertex)})")
        else:
            formatted_output.append(f"({idx+1},{item})")
    return ', '.join(formatted_output)

output = format_output(adjacency_list.items())  # Format the adjacency list for output
print()
print("Output")
print(output)
print()

def calculate_values(root_nodes):
    total_nodes = root_nodes * (root_nodes + 3) // 2
    max_label = math.ceil(total_nodes / 2)
    total_edges = total_nodes - 1
    return total_nodes, max_label, total_edges

# Create lists to store values
root_nodes_list = []
total_nodes_list = []
max_label_list = []
total_edges_list = []

# Generate values for root_nodes in intervals of 50
###
# for root_nodes in range(1, 50000, 250):
#     total_nodes, max_label, total_edges = calculate_values(root_nodes)
#     root_nodes_list.append(root_nodes)
#     total_nodes_list.append(total_nodes)
#     max_label_list.append(max_label)
#     total_edges_list.append(total_edges)

# # Create a DataFrame to display the table
# data = {
#     'root_nodes': root_nodes_list,
#     'total_nodes': total_nodes_list,
#     'max_label': max_label_list,
#     'total_edges': total_edges_list
# }

# df = pd.DataFrame(data)
# print()
# print('Values for different n values')
# print()
# print(df)  
###