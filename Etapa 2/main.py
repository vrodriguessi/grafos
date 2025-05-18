from src.utils.leitura_dados import parse_file_into_grafo, parse_capacidade
from src.algorithms.path_scanning import path_scanning
from src.utils.imprimir_resultados import salvar_resultado_path_scanning
import argparse
import os
import sys
import time
sys.stdout.reconfigure(encoding='utf-8')

def processar_arquivo(arquivo):
    print(f"📂 Processando o arquivo {arquivo}...\n")
    
    grafo = parse_file_into_grafo(arquivo)

    if not grafo:
        print(f"⚠ Erro: O arquivo {arquivo} não contém dados válidos.")
        return

    print(f"✅ Grafo de {arquivo} carregado com sucesso!")

    capacidade_veiculo = parse_capacidade(arquivo)
    
    start_clocks = time.process_time()
    solucao = path_scanning(grafo, capacidade_veiculo, deposito=1)
    end_clocks = time.process_time()

    tempo_execucao = end_clocks - start_clocks
    tempo_encontrar_solucao = tempo_execucao 

    nome_arquivo_solucao = f"sol-{os.path.basename(arquivo).replace('.dat', '')}.dat"

    salvar_resultado_path_scanning(solucao, tempo_execucao, tempo_encontrar_solucao, nome_arquivo_solucao)

    print(f"✅ Resultado salvo no arquivo {nome_arquivo_solucao}")

def main():
    parser = argparse.ArgumentParser(description="Processa um arquivo .dat específico na pasta padrão.")
    parser.add_argument("nome_arquivo", help="Nome do arquivo .dat (ex: grafo01.dat)")

    args = parser.parse_args()
    pasta_arquivos = "C:/Projetos/Grafos/Etapa 2/MCGRP/"
    caminho_arquivo = os.path.join(pasta_arquivos, args.nome_arquivo)

    if os.path.isfile(caminho_arquivo):
        processar_arquivo(caminho_arquivo)
    else:
        print(f"Arquivo '{args.nome_arquivo}' não encontrado na pasta '{pasta_arquivos}'.")

if __name__ == "__main__":
    main()
