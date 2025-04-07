from src.Grafos import Grafo
from src.utils.leitura_dados import parse_file_into_grafo
from src.algorithms.estatisticas import calcular_estatisticas, calcular_caminho_medio, calcular_diametro, calcular_intermediacao
from src.algorithms.floyd_warshall import floyd_warshall, obter_matriz_distancias, obter_matriz_predecessores
from src.utils.visualizacao import desenhar_grafo
from src.utils.visualizacao_matrizes import imprimir_matrizes
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

def processar_arquivo(arquivo):
    print(f"📂 Processando o arquivo {arquivo}...\n")
    
    grafo = parse_file_into_grafo(arquivo)

    if not grafo:
        print(f"⚠ Erro: O arquivo {arquivo} não contém dados válidos.")
        return

    print(f"✅ Grafo de {arquivo} carregado com sucesso!")

    estatisticas = calcular_estatisticas(grafo)
    dist = obter_matriz_distancias(grafo)
    pred = obter_matriz_predecessores(grafo)

    caminho_medio = calcular_caminho_medio(dist)
    diametro = calcular_diametro(dist)


    print(f"\n📊 Estatísticas do Grafo {arquivo}:")
    for chave, valor in estatisticas.items():
        print(f"  {chave}: {valor}")
    
    print(f"  Caminho médio: {caminho_medio}")
    print(f"  Diametro: {diametro}")
 
    imprimir_matrizes(dist, pred)

    intermediacoes = calcular_intermediacao(dist, pred)
    intermediacao_dict = {i: valor for i, valor in enumerate(intermediacoes, 1)}
    print(f"  Intermediação: {intermediacao_dict}")
    desenhar_grafo(grafo, titulo=f"Grafo - {os.path.basename(arquivo).replace('.dat', '')}")


        
def main():
    pasta_arquivos = "data/selected_instances/"
    
    arquivos = [f for f in os.listdir(pasta_arquivos) if f.endswith(".dat")]
    
    for arquivo in arquivos:
        processar_arquivo(os.path.join(pasta_arquivos, arquivo))

if __name__ == "__main__":
    main()

