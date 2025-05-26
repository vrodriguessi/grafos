from src.utils.leitura_dados import parse_file_into_grafo
from src.algorithms.path_scanning import path_scanning
from src.utils.imprimir_resultados import salvar_resultado_path_scanning
import argparse
import os
import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

def processar_arquivo(arquivo, pasta_saida="Solucoes"):
    print(f"📂 Processando o arquivo {arquivo}...\n")

    start_total = time.monotonic_ns()
    
    grafo = parse_file_into_grafo(arquivo)

    if not grafo:
        print(f"⚠ Erro: O arquivo {arquivo} não contém dados válidos.")
        return

    print(f"✅ Grafo de {arquivo} carregado com sucesso!")
    
    start_solucao = time.monotonic_ns()
    solucao = path_scanning(grafo)
    end_solucao = time.monotonic_ns()

    end_total = time.monotonic_ns()

    # tempos em nanosegundos (int)
    tempo_execucao_total = end_total - start_total
    tempo_solucao_clocks = end_solucao - start_solucao

    # Define o caminho completo do arquivo de saída (ex: Solucoes/sol-BHW1.dat)
    nome_arquivo_solucao = f"sol-{os.path.basename(arquivo).replace('.dat', '')}.dat"
    caminho_saida = os.path.join(pasta_saida, nome_arquivo_solucao)

    salvar_resultado_path_scanning(solucao, tempo_execucao_total, tempo_solucao_clocks, caminho_saida)

    print(f"✅ Resultado salvo no arquivo {nome_arquivo_solucao}")

def main():
    parser = argparse.ArgumentParser(description="Processa todos os arquivos .dat na pasta MCGRP e salva as soluções em Solucoes/.")
    args = parser.parse_args()

    pasta_entrada = "MCGRP/"
    pasta_saida = "Solucoes/"

    # Criar a pasta de saída se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Processar todos os arquivos .dat na pasta de entrada
    for nome_arquivo in os.listdir(pasta_entrada):
        if nome_arquivo.endswith(".dat"):
            caminho_entrada = os.path.join(pasta_entrada, nome_arquivo)
            print(f"\n✅ Processando: {nome_arquivo}")

            # Processa o arquivo (a função já salva o resultado internamente)
            processar_arquivo(caminho_entrada)

if __name__ == "__main__":
    main()
