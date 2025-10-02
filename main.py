from dijks import dijkstra, carregar_grafo

def main():
    Mygrafo = carregar_grafo("grafo.json")

    origem = input("Digite o nó de origem: ").strip().upper()
    destino = input("Digite o nó de destino: ").strip().upper()

    if origem not in Mygrafo or destino not in Mygrafo:
        print("Um dos nós não existe no grafo.")
        return

    custo, caminho = dijkstra(Mygrafo, origem, destino)
    if caminho:
        print(f"Melhor caminho: {' -> '.join(caminho)}")
        print(f"Custo total: {custo}")
    else:
        print("Não existe caminho entre os nós informados.")

if __name__ == "__main__":
    main()
