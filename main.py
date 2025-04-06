from src.Grafos import Grafo
from src.utils.leitura_dados import parse_file_into_grafo
from src.algorithms.estatisticas import calcular_estatisticas, calcular_caminho_medio, calcular_diametro
from src.algorithms.floyd_warshall import floyd_warshall
# from src.algorithms.componentes import encontrar_componentes
import os

def processar_arquivo(arquivo):
    print(f"📂 Processando o arquivo {arquivo}...\n")
    
    # Carrega o grafo
    grafo = parse_file_into_grafo(arquivo)

    # Verifica se os dados são válidos
    if not grafo:
        print(f"⚠️ Erro: O arquivo {arquivo} não contém dados válidos.")
        return

    print(f"✅ Grafo de {arquivo} carregado com sucesso!")

    # Calcula as estatísticas e executa os algoritmos
    estatisticas = calcular_estatisticas(grafo)
    dist, pred = floyd_warshall(grafo)
    # componentes = encontrar_componentes(grafo)

    caminho_medio = calcular_caminho_medio(dist)
    diametro = calcular_diametro(dist)

    # Exibe os resultados
    print(f"\n📊 Estatísticas do Grafo {arquivo}:")
    for chave, valor in estatisticas.items():
        print(f"  {chave}: {valor}")
    
    print(f"  Caminho médio: {caminho_medio}")
    print(f"  Diametro: {diametro}")

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
