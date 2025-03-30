def calcular_estatisticas(grafo):
    num_vertices = len(grafo.vertices)
    num_arestas = len(grafo.arestas) // 2 
    num_arcos = len(grafo.arcos)
    num_vertices_requeridos = len(grafo.vertices) 
    num_arestas_requeridas = num_arestas
    num_arcos_requeridos = num_arcos

    graus = [len(grafo.obter_vizinhos(v)) for v in grafo.vertices]
    grau_min = min(graus)
    grau_max = max(graus)

    densidade = (2 * num_arestas) / (num_vertices * (num_vertices - 1)) if num_vertices > 1 else 0

    return {
        "Quantidade de vértices": num_vertices,
        "Quantidade de arestas": num_arestas,
        "Quantidade de arcos": num_arcos,
        "Quantidade de vértices requeridos": num_vertices_requeridos,
        "Quantidade de arestas requeridas": num_arestas_requeridas,
        "Quantidade de arcos requeridos": num_arcos_requeridos,
        "Grau mínimo dos vértices": grau_min,
        "Grau máximo dos vértices": grau_max,
        "Densidade do grafo": densidade
    }
