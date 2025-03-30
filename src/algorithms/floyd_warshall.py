def floyd_warshall(grafo):
    INF = float('inf')
    vertices = list(grafo.vertices)
    n = len(vertices)
    
    dist = {v: {w: INF for w in vertices} for v in vertices}
    for v in vertices:
        dist[v][v] = 0

    for (u, v), dados in grafo.arestas.items():
        dist[u][v] = dados["custo"]
    for (u, v), dados in grafo.arcos.items():
        dist[u][v] = dados["custo"]

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
