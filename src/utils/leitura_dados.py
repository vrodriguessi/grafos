from src.models.grafo import Grafo

def carregar_grafo(caminho_arquivo):
    grafo = Grafo()
    
    with open(caminho_arquivo, 'r') as f:
        for linha in f:
            dados = linha.strip().split()
            tipo = dados[0]
            
            if tipo == "V":  # Vértice
                grafo.adicionar_vertice(int(dados[1]))
            elif tipo == "E":  # Aresta
                u, v, custo, demanda = map(int, dados[1:])
                grafo.adicionar_aresta(u, v, custo, demanda)
            elif tipo == "A":  # Arco
                u, v, custo, demanda = map(int, dados[1:])
                grafo.adicionar_arco(u, v, custo, demanda)

    return grafo
