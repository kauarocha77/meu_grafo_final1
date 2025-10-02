# - a função dijkstra que ver o melhor caminho no grafo
# - a função carregar_grafo que lê o grafo de um arquivo JSON
from dijks import dijkstra, carregar_grafo

def main():
    # carrega o grafo e guarda no arquivo grafo.json
    Mygrafo = carregar_grafo("grafo.json")

    # pergunta pro usuário qual é o ponto de partida e o ponto de chegada
    # strip() tira espaços extras, upper() deixa tudo maiúsculo
    origem = input("Digite o nó de origem: ").strip().upper()
    destino = input("Digite o nó de destino: ").strip().upper()

    # vê se os dois pontos realmente existem dentro do grafo
    if origem not in Mygrafo or destino not in Mygrafo:
        print("Um dos nós não existe no grafo.")
        return  # se não existir, para o programa aqui

    # chama a função dijkstra para calcular o menor caminho e o custo
    custo, caminho = dijkstra(Mygrafo, origem, destino)

    # se achou um caminho válido, mostra o resultado
    if caminho:
        print(f"Melhor caminho: {' -> '.join(caminho)}")  # junta os pontos com "->"
        print(f"Custo total: {custo}")  # mostra o custo total desse trajeto
    else:
        # caso não exista caminho entre os nós informados
        print("Não existe caminho entre os nós informados.")

if __name__ == "__main__":
    main()    

