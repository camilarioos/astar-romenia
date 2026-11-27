# -*- coding: utf-8 -*-
 # fase4_expandir.py — Fase 4: transformar a expansão em função e repetir à mão.
 # Rode com: python fase4_expandir.py

 # ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: função que mostra a fronteira de forma resumida -----
def mostrar_fronteira(fronteira):
    """Imprime cada nó da fronteira como Cidade(f=...)."""
    partes = []
    for f, g, cidade, caminho in fronteira:
        partes.append(f'{cidade}(f={f})')
    print(' fronteira:', ', '.join(partes))