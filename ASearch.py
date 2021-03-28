# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:22:00 2021

@author: hsume
"""

from node import Node
from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx

# Busca A*
def a_search(graph, heuristics, start, end):
    
    # Cria variaveis do grafo
    G = nx.Graph()
    edgelist = []
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                # Relaciona truplas dos grafos
                edgetruple = (current_node.name, neighbor.name)
                edgelist.append(edgetruple)
                continue
            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
                G.add_edge(current_node.name, neighbor.name)
        # define o posicionamento do grafo
        pos = nx.spring_layout(G)
        nx.draw(G, pos, font_size=16, with_labels=False)
        # nodes
        options = {"node_size": 500, "alpha": 0.8}
        nx.draw_networkx_nodes(G, pos, nodelist=[start_node.name], node_color="g", **options)
        if(goal_node in open):
            nx.draw_networkx_nodes(G, pos, nodelist=[goal_node.name], node_color="b", **options)
        # edge
        nx.draw_networkx_edges(G, pos, edgelist=edgelist, width=2, alpha=0.5, edge_color="r")
        # Plot grafo
        nx.draw_networkx_labels(G, pos)
        plt.axis("off")
        plt.show()
    # Return None, no path is found
    return None

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True