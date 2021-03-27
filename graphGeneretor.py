# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:51:51 2021

@author: hsume
"""

import graph as gp

def graph_generetor():
    
    # Create a graph
    graph = gp.Graph()
    
    # Create graph connections (Actual distance)
    graph.connect('BoaVista', 'Manaus', 111)
    graph.connect('Manaus', 'RioBranco', 85)
    graph.connect('Manaus', 'PortoVelho', 104)
    graph.connect('Manaus', 'Brasilia', 140)
    graph.connect('Manaus', 'Belem', 183)
    graph.connect('RioBranco', 'PortoVelho', 230)
    graph.connect('PortoVelho', 'Cuiaba', 67)
    graph.connect('Belem', 'Macapa', 191)
    graph.connect('Brasilia', 'Palmas', 64)
    graph.connect('Brasilia', 'Goiania', 171)
    graph.connect('Brasilia', 'SaoPaulo', 170)
    graph.connect('Brasilia', 'BeloHorizonte', 220)
    graph.connect('Brasilia', 'Fortaleza', 107)
    graph.connect('Brasilia', 'Cuiaba', 91)
    graph.connect('Fortaleza', 'SaoLuis', 85)
    graph.connect('Fortaleza', 'Teresina', 120)
    graph.connect('Fortaleza', 'Natal', 184)
    graph.connect('Fortaleza', 'Recife', 55)
    graph.connect('Fortaleza', 'Salvador', 115)
    graph.connect('Cuiaba', 'CampoGrande', 123)
    graph.connect('Cuiaba', 'SaoPaulo', 189)
    graph.connect('CampoGrande', 'Curitiba', 59)
    graph.connect('Curitiba', 'Florianopolis', 81)
    graph.connect('Curitiba', 'SaoPaulo', 81)
    graph.connect('Florianopolis', 'PortoAlegre', 102)
    graph.connect('SaoPaulo', 'RioDeJaneiro', 126)
    graph.connect('RioDeJaneiro', 'Vitoria', 126)
    graph.connect('RioDeJaneiro', 'Salvador', 126)
    graph.connect('Salvador', 'Aracaju', 126)
    graph.connect('Salvador', 'Natal', 126)
    graph.connect('Aracaju', 'Maceio', 126)
    graph.connect('Maceio', 'Recife', 126)
    graph.connect('Recife', 'JoaoPessoa', 126)
    graph.connect('JoaoPessoa', 'Natal', 126)
    
    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    
    # Create heuristics (straight-line distance, air-travel distance)
    heuristics = {}
    heuristics['BoaVista'] = 204
    heuristics['Manaus'] = 247
    heuristics['RioBranco'] = 215
    heuristics['PortoVelho'] = 137
    heuristics['Belem'] = 318
    heuristics['Macapa'] = 164
    heuristics['Cuiaba'] = 120
    heuristics['CampoGrande'] = 47
    heuristics['Curitiba'] = 132
    heuristics['Florianopolis'] = 257
    heuristics['PortoAlegre'] = 168
    heuristics['SaoPaulo'] = 75
    heuristics['RioDeJaneiro'] = 236
    heuristics['Vitoria'] = 153
    heuristics['Salvador'] = 157
    heuristics['Aracaju'] = 0
    heuristics['Maceio'] = 0
    heuristics['Recife'] = 0
    heuristics['Natal'] = 0
    heuristics['JoaoPessoa'] = 0
    heuristics['Natal'] = 0
    heuristics['Fortaleza'] = 0
    heuristics['SaoLuis'] = 0
    heuristics['Brasilia'] = 0
    heuristics['BeloHorizonte'] = 0
    heuristics['Goiania'] = 0
    heuristics['Palmas'] = 0
    heuristics['Teresina'] = 0
    
    return graph, heuristics
