# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:15:37 2021

@author: hsume
"""

import graphGeneretor as gg
import DepthFirstSearch as dp
import BreadthFirstSearch as bff
import UniformCostSearch as uc
import BestFirstSearch as bf
import ASearch as ae


graph, heuristics = gg.graph_generetor()


print(dp.depth_first_search(graph, "BoaVista", 'Natal'))
print()
print(bff.breadth_first_search(graph, "BoaVista", 'RioDeJaneiro'))
print()
print(uc.uniform_cost_search(graph, "Salvador", 'Belem'))
print()
print(bf.best_first_search(graph, heuristics, "BoaVista", 'Natal'))
print()
print(ae.a_search(graph, heuristics, "BoaVista", 'Natal'))
print()
