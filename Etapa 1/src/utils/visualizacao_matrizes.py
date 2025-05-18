def imprimir_matrizes(distancias, predecessores):
    num_vertices = len(distancias)
    vertices = list(range(1, num_vertices + 1))

    print("\n📏 Matriz de Distâncias")
    print("     " + " ".join(f"{v:>5}" for v in vertices))
    for i in range(num_vertices):
        linha = [
            f"{int(distancias[i][j]):5d}" if distancias[i][j] != float('inf') else "  inf"
            for j in range(num_vertices)
        ]
        print(f"{vertices[i]:>3} " + " ".join(linha))

    print("\n🧭 Matriz de Predecessores")
    print("     " + " ".join(f"{v:>5}" for v in vertices))
    for i in range(num_vertices):
        linha = [
            f"{predecessores[i][j]:>5}" if predecessores[i][j] is not None else " None"
            for j in range(num_vertices)
        ]
        print(f"{vertices[i]:>3} " + " ".join(linha))
