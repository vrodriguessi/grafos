def encontrar_componentes(grafo):
    visitado = set()
    componentes = []

    def dfs(v, componente):
        visitado.add(v)
        componente.append(v)
        for vizinho in grafo.obter_vizinhos(v):
            if vizinho not in visitado:
                dfs(vizinho, componente)

    for vertice in grafo.vertices:
        if vertice not in visitado:
            componente = []
            dfs(vertice, componente)
            componentes.append(componente)

    return componentes
