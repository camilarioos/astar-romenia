
# -*- coding: utf-8 -*-
# fase5_busca.py — Fase 5: o laço while que repete a expansão até chegar.
# Rode com: python fase5_busca.py

# ----- PASSO 1: importar os dados -----
from mapa import mapa_romenia, heuristica_bucareste

# ----- PASSO 2: a função de busca A* -----
def busca_a_estrela(inicio, objetivo):
    """Devolve (caminho, custo) do melhor caminho, ou (None, infinito)."""

    # Fronteira guarda as cidades que ainda podem ser exploradas.
    # Cada nó contém: (f, g, cidade, caminho).
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]

    # Guarda as cidades que já foram exploradas.
    explorados = set()

    # Repete enquanto houver cidades na fronteira.
    while fronteira:

        # Organiza as cidades pelo menor f (custo estimado total).
        fronteira.sort(key=lambda no: no[0])

        # Retira da fronteira a cidade com menor f.
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # Verifica se a cidade retirada é o destino.
        if cidade_atual == objetivo:
            return caminho, g_atual

        # Se a cidade já foi explorada, pula para a próxima rodada.
        if cidade_atual in explorados:
            continue

        # Marca a cidade atual como explorada.
        explorados.add(cidade_atual)

        # Percorre os vizinhos da cidade atual.
        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:

            # Só considera vizinhos que ainda não foram explorados.
            if vizinho not in explorados:

                # g = custo real acumulado até o vizinho.
                novo_g = g_atual + custo_estrada

                # f = custo acumulado + estimativa até Bucareste.
                novo_f = novo_g + heuristica_bucareste[vizinho]

                # Adiciona o vizinho à fronteira com seu novo custo e caminho.
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    # Se a fronteira acabar sem encontrar o destino, retorna ausência de caminho.
    return None, float('inf')


# ----- PASSO 3: chamar a função e mostrar o resultado -----

# Executa a busca começando em Arad e procurando Bucareste.
caminho, custo = busca_a_estrela('Arad', 'Bucharest')

# Mostra as cidades percorridas, separadas por setas.
print('Caminho:', ' -> '.join(caminho))

# Mostra o custo total do caminho encontrado.
print('Custo :', custo, 'km')

# Conta quantas estradas foram percorridas.
print('Passos :', len(caminho) - 1, 'estradas')
