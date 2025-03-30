from src.utils.leitura_dados import carregar_grafo
from src.algorithms.estatisticas import calcular_estatisticas
from src.algorithms.floyd_warshall import floyd_warshall
from src.algorithms.componentes import encontrar_componentes
import os

def processar_arquivo(arquivo):
    print(f"Processando o arquivo {arquivo}...")
    
    grafo = None
    
    # Aguarda até que o grafo seja carregado corretamente
    print(f"Aguardando o carregamento do grafo de {arquivo}...")  # Imprime apenas uma vez
    while grafo is None or not grafo.vertices:
        grafo = carregar_grafo(arquivo)  # Tenta carregar o grafo para o arquivo específico
    
    # Agora que o grafo está carregado, calcule as estatísticas e execute as operações
    print(f"Grafo de {arquivo} carregado com sucesso!")

    estatisticas = calcular_estatisticas(grafo)
    matriz_caminhos = floyd_warshall(grafo)
    componentes = encontrar_componentes(grafo)

    # Exibe as estatísticas do grafo carregado
    print(f"\n📊 Estatísticas do Grafo {arquivo}:")
    for chave, valor in estatisticas.items():
        print(f"{chave}: {valor}")

    print("\n🔗 Componentes Conectados:")
    for i, comp in enumerate(componentes, 1):
        print(f"Componente {i}: {comp}")
    
def main():
    # Caminho para os arquivos
    pasta_arquivos = "C:/Projetos/Grafos/data/selected_instances/"
    
    # Listando todos os arquivos na pasta
    arquivos = [f for f in os.listdir(pasta_arquivos) if f.endswith(".dat")]
    
    # Processar cada arquivo um por vez
    for arquivo in arquivos:
        processar_arquivo(os.path.join(pasta_arquivos, arquivo))

if __name__ == "__main__":
    main()
