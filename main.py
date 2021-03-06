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

# Cidades a serem escolhidas
cidadeComeco = "SaoLuis"
cidadeFim = 'RioBranco'

graph, heuristics = gg.graph_generetor(cidadeFim)

print("Busca em profundidade")
inicio = timeit.default_timer()
print(dp.depth_first_search(graph, cidadeComeco, cidadeFim))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

print("Busca em Largura")
inicio = timeit.default_timer()
print(bff.breadth_first_search(graph, cidadeComeco, cidadeFim))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

print("Busca de custo uniforme")
inicio = timeit.default_timer()
print(uc.uniform_cost_search(graph, cidadeComeco, cidadeFim))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

print("Busca gulosa")
inicio = timeit.default_timer()
print(bf.best_first_search(graph, heuristics, cidadeComeco, cidadeFim))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()

print("Busca A*")
inicio = timeit.default_timer()
print(ae.a_search(graph, heuristics, cidadeComeco, cidadeFim))
fim = timeit.default_timer()
print ('duracao: %f' % (fim - inicio))
print()
