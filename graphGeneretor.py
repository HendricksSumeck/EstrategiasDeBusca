# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:51:51 2021

@author: hsume
"""

import graph as gp

def graph_generetor():
    
    # Instancia o grago
    graph = gp.Graph()
    
    # Cria o grafo com base nas distacias por terra entre as cidades
    graph.connect('BoaVista', 'Manaus', 785)
    graph.connect('Manaus', 'RioBranco', 1445)
    graph.connect('Manaus', 'PortoVelho', 901)
    graph.connect('Manaus', 'Brasilia', 3490)
    graph.connect('Manaus', 'Belem', 5298)
    graph.connect('RioBranco', 'PortoVelho', 544)
    graph.connect('PortoVelho', 'Cuiaba', 1456)
    graph.connect('Belem', 'Macapa', 650) #Distancia tirada do site https://www.geografos.com.br/distancia-entre-cidades/distancia-entre-macapa-e-belem.php
    graph.connect('Brasilia', 'Palmas', 973)
    graph.connect('Brasilia', 'Goiania', 209)
    graph.connect('Brasilia', 'SaoPaulo', 1015)
    graph.connect('Brasilia', 'BeloHorizonte', 716)
    graph.connect('Brasilia', 'Fortaleza', 2200)
    graph.connect('Brasilia', 'Cuiaba', 1133)
    graph.connect('Fortaleza', 'SaoLuis', 1070)
    graph.connect('Fortaleza', 'Teresina', 634)
    graph.connect('Fortaleza', 'Natal', 537)
    graph.connect('Fortaleza', 'Recife', 800)
    graph.connect('Fortaleza', 'Salvador', 1389)
    graph.connect('Cuiaba', 'CampoGrande', 694)
    graph.connect('Cuiaba', 'SaoPaulo', 1614)
    graph.connect('CampoGrande', 'Curitiba', 991)
    graph.connect('Curitiba', 'Florianopolis', 300)
    graph.connect('Curitiba', 'SaoPaulo', 408)
    graph.connect('Florianopolis', 'PortoAlegre', 476)
    graph.connect('SaoPaulo', 'RioDeJaneiro', 429)
    graph.connect('RioDeJaneiro', 'Vitoria', 521)
    graph.connect('RioDeJaneiro', 'Salvador', 1649)
    graph.connect('Salvador', 'Aracaju', 356)
    graph.connect('Salvador', 'Natal', 1126)
    graph.connect('Aracaju', 'Maceio', 294)
    graph.connect('Maceio', 'Recife', 285)
    graph.connect('Recife', 'JoaoPessoa', 120)
    graph.connect('JoaoPessoa', 'Natal', 185)
    graph.connect('BeloHorizonte', 'SaoPaulo', 586)
    graph.connect('BeloHorizonte', 'RioDeJaneiro', 434)
    
    # Trasforma o grafo unidiricionalmente
    graph.make_undirected()
    
    # Criar as heurística (distância em linha reta, distância de viagem aérea)
    heuristics = {}
    heuristics['BoaVista'] = 1335
    heuristics['Manaus'] = 761
    heuristics['RioBranco'] = 449
    heuristics['PortoVelho'] = 0
    heuristics['Belem'] = 1886
    heuristics['Macapa'] = 1724
    heuristics['Cuiaba'] = 1137
    heuristics['CampoGrande'] = 1634
    heuristics['Curitiba'] = 2412
    heuristics['Florianopolis'] = 2641
    heuristics['PortoAlegre'] = 2706
    heuristics['SaoPaulo'] = 2463
    heuristics['RioDeJaneiro'] = 2707
    heuristics['Vitoria'] = 2835
    heuristics['Salvador'] = 2808
    heuristics['Aracaju'] = 2946
    heuristics['Maceio'] = 3090
    heuristics['Recife'] = 3190
    heuristics['Natal'] = 3179
    heuristics['JoaoPessoa'] = 3200
    heuristics['Fortaleza'] = 2855
    heuristics['SaoLuis'] = 2274
    heuristics['Brasilia'] = 1900
    heuristics['BeloHorizonte'] = 2477
    heuristics['Goiania'] = 1813
    heuristics['Palmas'] = 1711
    heuristics['Teresina'] = 2362
    
    return graph, heuristics
