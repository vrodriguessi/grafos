def path_scanning(grafo, capacidade_veiculo, deposito=1):
    grafo.calcular_matriz_distancia_minima()
    arcos_servico = grafo.get_arcos_obrigatorios()
    visitados = set()
    rotas = []

    while len(visitados) < len(arcos_servico):
        carga = 0
        custo_rota = 0
        rota = []
        posicao_atual = deposito

        while True:
            candidatos = []

            for idx, (u, v, custo, demanda) in enumerate(arcos_servico):
                if idx in visitados:
                    continue
                if demanda + carga > capacidade_veiculo:
                    continue

                dist = grafo.distancia(posicao_atual, u)
                candidatos.append((dist, idx, u, v, custo, demanda))

            if not candidatos:
                break

            candidatos.sort() 
            _, idx, u, v, custo, demanda = candidatos[0]
            carga += demanda
            custo_rota += grafo.distancia(posicao_atual, u) + custo
            rota.append((u, v))
            posicao_atual = v
            visitados.add(idx)

        custo_rota += grafo.distancia(posicao_atual, deposito)
        rotas.append({
            'rota': rota,
            'carga': carga,
            'custo': custo_rota
        })

    return rotas
