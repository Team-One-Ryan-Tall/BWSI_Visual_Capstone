from platform import node
from Descriptors import descriptors_from_filestack
from Profile import Profile
from CosineDists import cosine_distances
from Node import Node
import numpy as np
import random

def get_neighbors(descriptor, descriptor_list, indexes):
    neighbors = []
    for index in indexes:
        similarity = cosine_distances(descriptor, descriptor_list[index])
    
        if (0 < similarity <= 0.5):
            neighbors.append(index)
            
    return neighbors

def labels(dvs):       
    return list(range(len(dvs)))

def generate_network(filepaths):
    descriptors = descriptors_from_filestack(filepaths)
    lbls = labels(descriptors)
    nodes = []
    for i  in lbls:
        nodes.append(Node(i, get_neighbors(descriptors[i], descriptors, lbls), descriptor=descriptors[i], file_path=filepaths[i]))
    adj_matrix = make_adjacencies(nodes)
    run_whispers(nodes, adj_matrix)
    return nodes, adj_matrix

def make_adjacencies(nodes: list):
    adj_matrix = np.zeros((len(nodes), len(nodes)))
    for i in range(len(nodes)):
        for neighbr in nodes[i].neighbors: 
            # print(i, neighbr)
            adj_matrix[i, neighbr] = 1/(cosine_distances(nodes[i].descriptor, nodes[neighbr].descriptor) ** 2)

    return adj_matrix

def run_whispers(nodes, adj_matrix, multiplier=15):
    for _ in range(len(nodes) * multiplier):#len(nodes) * multiplier):
        current = random.choice(nodes)
        # print(f"s{_}")
        whispers(nodes, current, adj_matrix)
        # print(_)

    
def whispers(nodes, node, adj_matrix):
    m = 0
    index = -1
    labels_and_weights = {}
    
    for neighbor in node.neighbors:
        if nodes[neighbor].label not in labels_and_weights:
            labels_and_weights[nodes[neighbor].label] = adj_matrix[node.id, neighbor]
        else:
            labels_and_weights[nodes[neighbor].label] += adj_matrix[node.id, neighbor]
    for label in labels_and_weights.keys():
        if (m < labels_and_weights[label]):
                m = labels_and_weights[label]
                index = label
    
    if (index != -1):
        node.label = index
        
def connected_components(nodes):
    connections = {}
    for node in nodes:
        if(node.label in connections):
            connections[node.label].append(node.id)
        else:
            connections[node.label] = [node.id]
    return list(connections.values()) 