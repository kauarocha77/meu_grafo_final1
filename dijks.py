import json as js
import heapq as hq
from typing import Dict, Tuple, List

# Função Dijkstra
def dijkstra(grafo: Dict[str, Dict[str, float]], origem: str, destino: str) -> Tuple[float, List[str]]:
    """
    Calcula o caminho mínimo entre origem e destino usando Dijkstra.
    Retorna (custo_total, caminho_completo)
    """
    fila = [(0, origem, [origem])]  # tupla: (custo, nó atual, caminho até aqui)
    visitados = set()

    while fila:
        custo, atual, caminho = hq.heappop(fila)

        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == destino:
            return custo, caminho

        for vizinho, peso in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                hq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))

    return float("inf"), []

# Função para carregar grafo de JSON
def carregar_grafo(caminho_arquivo: str) -> Dict[str, Dict[str, float]]:
    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        grafo = js.load(f)
    return grafo
