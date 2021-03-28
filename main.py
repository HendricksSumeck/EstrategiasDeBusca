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

import time
import timeit

graph, heuristics = gg.graph_generetor()

inicio = timeit.default_timer()
print(dp.depth_first_search(graph, "JoaoPessoa", 'PortoVelho'))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

inicio = timeit.default_timer()
print(bff.breadth_first_search(graph, "JoaoPessoa", 'PortoVelho'))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

inicio = timeit.default_timer()
print(uc.uniform_cost_search(graph, "JoaoPessoa", 'PortoVelho'))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

inicio = timeit.default_timer()
print(bf.best_first_search(graph, heuristics, "JoaoPessoa", 'PortoVelho'))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

inicio = timeit.default_timer()
print(ae.a_search(graph, heuristics, "JoaoPessoa", 'PortoVelho'))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()
