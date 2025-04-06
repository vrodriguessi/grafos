def floyd_warshall(ReA, ARC, ReE, EDGE, ReN):
    # Garante que os parâmetros sejam conjuntos
    ReA = set(ReA)
    ARC = set(ARC)
    ReE = set(ReE)
    EDGE = set(EDGE)
    ReN = set(ReN)

    # Une os arcos obrigatórios e não obrigatórios
    arcos = ReA.union(ARC)

    if not arcos:
        return [], []

    # Determina o número de nós
    n = max(max(u, v) for u, v, *_ in arcos)
    INF = float('inf')

    # Inicializa as matrizes de distâncias e predecessores
    dist = [[INF] * n for _ in range(n)]
    pred = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    # Adiciona os arcos com peso 1
    for u, v, *_ in arcos:
        dist[u - 1][v - 1] = 1  # peso padrão
        pred[u - 1][v - 1] = u - 1

    # Algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    # Reconstrói caminhos
    def reconstruir_caminho(i, j):
        caminho = []
        if pred[i][j] is None:
            return caminho
        while j != i:
            caminho.append((pred[i][j], j))
            j = pred[i][j]
        caminho.reverse()
        return caminho

    # Conjuntos usados
    arcos_usados = set()
    nos_usados = set()
    todos_arcos = {(u - 1, v - 1) for u, v, *_ in arcos}

    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != INF:
                caminho = reconstruir_caminho(i, j)
                for u, v in caminho:
                    arcos_usados.add((u, v))
                for _, v in caminho[:-1]:
                    nos_usados.add(v)

    # Atualiza os conjuntos de arcos obrigatórios e não obrigatórios
    ReA.update((u + 1, v + 1) for u, v in arcos_usados)
    ARC.update((u + 1, v + 1) for u, v in todos_arcos - arcos_usados)

    # Atualiza os conjuntos de arestas obrigatórias e não obrigatórias
    todas_arestas = {tuple(sorted((u, v))) for u, v in {(u + 1, v + 1) for u, v in todos_arcos}}
    arestas_usadas = {tuple(sorted((u + 1, v + 1))) for u, v in arcos_usados}

    ReE.update(arestas_usadas)
    EDGE.update(todas_arestas - ReE)

    # Atualiza os nós obrigatórios
    ReN.update(v + 1 for v in nos_usados)

    return dist, pred
