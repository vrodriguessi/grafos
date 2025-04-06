def encontrar_componentes(ReA, ARC, ReE, EDGE, ReN):
    visitado = set()
    componentes = []

    # Criando dicionário de adjacência
    adjacencia = {}

    # Arestas (bidirecionais)
    for u, v, _ in ReE + EDGE:
        adjacencia.setdefault(u, []).append(v)
        adjacencia.setdefault(v, []).append(u)

    # Arcos (direcionais)
    for u, v, _ in ReA + ARC:
        adjacencia.setdefault(u, []).append(v)

    # Garante que os nós obrigatórios apareçam (mesmo isolados)
    for nodo in ReN:
        adjacencia.setdefault(nodo, [])

    def dfs(v, componente):
        visitado.add(v)
        componente.append(v)
        for vizinho in adjacencia.get(v, []):
            if vizinho not in visitado:
                dfs(vizinho, componente)

    # Encontrando componentes conectados
    for vertice in adjacencia:
        if vertice not in visitado:
            componente = []
            dfs(vertice, componente)
            componentes.append(componente)

    return componentes
