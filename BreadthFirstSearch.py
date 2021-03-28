# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:22:31 2021

@author: hsume
"""

from node import Node
from graph import Graph

# Busca em Largura
def breadth_first_search(graph, start, end):
    
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
        # Get the first node (FIFO)
        current_node = open.pop(0)
        print(current_node.name)
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
                continue
            # Check if neighbor is in open list and if it has a lower f value
            if(neighbor in open):
                continue
            # Calculate cost so far
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            # Everything is green, add neighbor to open list
            open.append(neighbor)
    # Return None, no path is found
    return None