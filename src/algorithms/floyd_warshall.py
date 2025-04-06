def floyd_warshall(grafo):
    n = grafo.num_vertices
    INF = float('inf')

    # Clona a matriz de adjacência original
    dist = [row[:] for row in grafo.adj_matrix]
    pred = [[None] * n for _ in range(n)]

    # Inicializa predecessores: se há caminho direto, o predecessor é o vértice de origem
    for u in range(n):
        for v in range(n):
            if u != v and dist[u][v] != INF:
                pred[u][v] = u + 1  # Usa +1 porque seus vértices são 1-based

    # Executa o algoritmo de Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred
