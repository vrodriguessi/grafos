def calcular_estatisticas(grafo):
    ReA = grafo.ReA
    ARC = grafo.ARC
    ReE = grafo.ReE
    EDGE = grafo.EDGE
    ReN = grafo.ReN

    # Junta todos os vértices usados
    num_vertices = set()
    for u, v, *_ in ReA + ARC + ReE + EDGE:
        num_vertices.add(u)
        num_vertices.add(v)
    num_vertices.update(ReN)  # Garante que nós obrigatórios também são contados

    num_vertices_total = len(num_vertices)
    num_arcos_total = len(ReA) + len(ARC)
    num_arestas_total = len(ReE) + len(EDGE)

    # Inicializa grau de entrada e saída com 0 para todos os vértices
    grau_in = {v: 0 for v in num_vertices}
    grau_out = {v: 0 for v in num_vertices}

    # Arestas são bidirecionais: contam como entrada e saída para ambos
    for u, v, *_ in ReE + EDGE:
        grau_in[u] += 1
        grau_out[u] += 1
        grau_in[v] += 1
        grau_out[v] += 1

    # Arcos são direcionais: saída do u, entrada no v
    for u, v, *_ in ReA + ARC:
        grau_out[u] += 1
        grau_in[v] += 1

    # Grau total por vértice = grau de entrada + grau de saída
    grau_total = {v: grau_in[v] + grau_out[v] for v in num_vertices}
    grau_min = min(grau_total.values()) if grau_total else 0
    grau_max = max(grau_total.values()) if grau_total else 0

    # Densidade considerando arcos e arestas
    densidade = (num_arcos_total + num_arestas_total) / (num_vertices_total * (num_vertices_total - 1)) if num_vertices_total > 1 else 0

    return {
        "Quantidade de vértices": num_vertices_total,
        "Quantidade de arestas obrigatórias": len(ReE),
        "Quantidade de arestas opcionais": len(EDGE),
        "Quantidade total de arestas": num_arestas_total,
        "Quantidade de arcos obrigatórios": len(ReA),
        "Quantidade de arcos opcionais": len(ARC),
        "Quantidade total de arcos": num_arcos_total,
        "Quantidade de nós obrigatórios": len(grafo.ReN),
        "Grau mínimo dos vértices": grau_min,
        "Grau máximo dos vértices": grau_max,
        "Densidade do grafo": densidade
    }

def calcular_caminho_medio(dist):
    total = 0
    count = 0

    n = len(dist)

    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                total += dist[i][j]
                count += 1

    return total / count if count != 0 else 0

def calcular_diametro(dist):
    diametro = 0
    n = len(dist)

    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                diametro = max(diametro, dist[i][j])

    return diametro
