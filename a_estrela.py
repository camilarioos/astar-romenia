# -*- coding: utf-8 -*-
 # a_estrela.py — Fase 6: o programa completo da busca A*.
 # Rode com: python a_estrela.py
 #
 # f(n) = g(n) + h(n)
 # g(n): km já percorridos desde a origem até n (custo real)
 # h(n): km em linha reta de n até Bucareste (estimativa, heurística)
 # f(n): estimativa do custo total do caminho que passa por n

 # ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: funções de apoio para imprimir -----
def resumo_fronteira(fronteira):
 """Texto curto com a fronteira: Cidade(f) separados por vírgula."""
 return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)
