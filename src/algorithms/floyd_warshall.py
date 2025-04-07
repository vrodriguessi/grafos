def floyd_warshall(grafo):
    n = grafo.num_vertices
    INF = float('inf')

    dist = [row[:] for row in grafo.adj_matrix]
    pred = [[None] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if u != v and dist[u][v] != INF:
                pred[u][v] = u + 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

def obter_matriz_distancias(grafo):
    distancias, _ = floyd_warshall(grafo)
    return distancias

def obter_matriz_predecessores(grafo):
    _, predecessores = floyd_warshall(grafo)
    return predecessores
