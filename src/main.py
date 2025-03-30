from utils.leitura_dados import carregar_grafo
from algorithms.estatisticas import calcular_estatisticas
from algorithms.floyd_warshall import floyd_warshall
from algorithms.componentes import encontrar_componentes

def main():
    caminho_arquivo = "data/dados.txt"
    grafo = carregar_grafo(caminho_arquivo)

    estatisticas = calcular_estatisticas(grafo)
    matriz_caminhos = floyd_warshall(grafo)
    componentes = encontrar_componentes(grafo)

    print("📊 Estatísticas do Grafo:")
    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")

    print("\n🔗 Componentes Conectados:")
    for i, comp in enumerate(componentes, 1):
        print(f"Componente {i}: {comp}")

if __name__ == "__main__":
    main()
