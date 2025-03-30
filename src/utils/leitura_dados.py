import os
from src.models.grafos import Grafo

def carregar_grafo(caminho_arquivo=None):
    grafo = Grafo()

    if caminho_arquivo is None:
        caminho_arquivo = input("Por favor, forneça o caminho do arquivo .dat: ").strip()

        if not os.path.exists(caminho_arquivo):
            print(f"Erro: o arquivo {caminho_arquivo} não foi encontrado.")
            return None

    with open(caminho_arquivo, 'r') as f:
        section = None
        for linha in f:
            linha = linha.strip()

            if not linha or linha.startswith("#"):
                continue 

            # Identificação da seção
            if linha.startswith("ReN."):
                section = "ReN"
            elif linha.startswith("ReE."):
                section = "ReE"
            elif linha.startswith("ReA."):
                section = "ReA"
            elif linha.startswith("EDGE"):
                section = "EDGE"
            elif linha.startswith("ARC"):
                section = "ARC"

            # Processamento das seções
            if section == "ReN":
                processar_ReN(linha, grafo)
            elif section == "ReE":
                if linha.startswith('E'):  # As linhas de dados começam com 'E' seguido de número
                    processar_ReE(linha, grafo)
            elif section == "ReA":
                if linha.startswith('A'):  # As linhas de dados começam com 'A' seguido de número
                    processar_ReA(linha, grafo)
            elif section == "EDGE":
                if linha.startswith('E'):  # As linhas de dados começam com 'E' seguido de número
                    processar_EDGE(linha, grafo)
            elif section == "ARC":
                if linha.startswith('NrA'):  # As linhas de dados começam com 'NrA' seguido de número
                    processar_ARC(linha, grafo)

    return grafo

def processar_ReN(linha, grafo):
    dados = linha.split()
    if len(dados) == 3: 
        nodo = dados[0]
        grafo.adicionar_vertice(nodo) 

def processar_ReE(linha, grafo):
    dados = linha.split()
    if len(dados) == 6: 
        de = dados[1]
        para = dados[2]
        custo = int(dados[3])
        demanda = int(dados[4])
        grafo.adicionar_aresta(de, para, custo, demanda)

def processar_ReA(linha, grafo):
    dados = linha.split()
    if len(dados) == 6: 
        de = dados[1]
        para = dados[2]
        custo = int(dados[3])
        demanda = int(dados[4])
        grafo.adicionar_arco(de, para, custo, demanda)

def processar_EDGE(linha, grafo):
    dados = linha.split()
    if len(dados) == 5: 
        de = dados[1]
        para = dados[2]
        custo = int(dados[3])
        grafo.adicionar_aresta(de, para, custo, 0)  

def processar_ARC(linha, grafo):
    dados = linha.split()
    if len(dados) == 4: 
        de = dados[1]
        para = dados[2]
        custo = int(dados[3])
        grafo.adicionar_arco(de, para, custo, 0) 