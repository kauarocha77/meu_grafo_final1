import json as js  # para ler o grafo que está guardado em um arquivo JSON
import heapq as hq  # estrutura de fila de prioridade, sempre pega o menor custo primeiro
from typing import Dict, Tuple, List  # só para deixar claro os tipos que usamos


# Função Dijkstra
def dijkstra(grafo: Dict[str, Dict[str, float]], origem: str, destino: str) -> Tuple[float, List[str]]:
    # cria a fila de prioridade. Ela começa com o nó de origem, custo 0 e o caminho contendo só a origem
    fila = [(0, origem, [origem])]
    visitados = set()  # guarda os nós que já foram visitados, para não repetir

    # enquanto ainda tiver nós na fila
    while fila:
        custo, atual, caminho = hq.heappop(fila)  # pega o nó com o menor custo até agora

        if atual in visitados:  # se já visitou esse nó, ignora
            continue
        visitados.add(atual)  # marca como visitado

        if atual == destino:  # se chegou no destino, devolve o custo e o caminho
            return custo, caminho

        # para cada vizinho do nó atual
        for vizinho, peso in grafo.get(atual, {}).items():
            if vizinho not in visitados:  # só coloca na fila quem ainda não foi visitado
                hq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))  # adiciona o vizinho na fila

    # se não encontrou caminho até o destino, retorna infinito e lista vazia
    return float("inf"), []


# função para carregar grafo de JSON
def carregar_grafo(caminho_arquivo: str) -> Dict[str, Dict[str, float]]:
    with open(caminho_arquivo, "r", encoding="utf-8") as f:  # abre o arquivo JSON
        grafo = js.load(f)  # transforma o conteúdo do arquivo em um dicionário Python
    return grafo  # devolve o grafo pronto para ser usado
