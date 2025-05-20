def construir_mapeamento_servico_id(grafo):
    mapeamento = {}
    contador = 1

    for no_info in grafo.nos_obrigatorios:
        no = no_info['no']
        chave = ("no", no)
        if chave not in mapeamento:
            mapeamento[chave] = contador
            contador += 1

    for u, v, _, _ in grafo.arestas_obrigatorias:
        chave = ("aresta", tuple(sorted((u, v))))
        if chave not in mapeamento:
            mapeamento[chave] = contador
            contador += 1

    for u, v, _, _ in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        if chave not in mapeamento:
            mapeamento[chave] = contador
            contador += 1

    return mapeamento


def path_scanning(grafo):
    grafo.calcular_floyd_warshall()

    servicos_pendentes = set()
    servico_info = {}

    for u, v, custo, demanda in grafo.arestas_obrigatorias:
        chave = ("aresta", tuple(sorted((u, v))))
        servicos_pendentes.add(chave)
        servico_info[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": tuple(sorted((u, v))),
        }

    for u, v, custo, demanda in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        servicos_pendentes.add(chave)
        servico_info[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }

    for no_info in grafo.nos_obrigatorios:
        no = no_info['no']
        chave = ("no", no)
        servicos_pendentes.add(chave)
        servico_info[chave] = {
            "demanda": no_info.get("demanda", 1),
            "custo": no_info.get("custo", 0),
            "extremos": (no, no),
        }

    mapeamento_id = construir_mapeamento_servico_id(grafo)
    solucao = []
    deposito = 1  # Ajuste conforme o problema

    while servicos_pendentes:
        rota = [deposito]
        carga = 0
        custo = 0
        servicos_rota = []
        detalhes_visitas = []
        no_atual = deposito

        while True:
            melhor_servico = None
            melhor_caminho = None
            menor_custo = float('inf')
            melhor_extremos = None
            outro_extremo = None

            for serv in servicos_pendentes:
                info = servico_info[serv]
                extremos = info["extremos"]

                if serv[0] == "no":
                    caminho = grafo.obterCaminhoMinimo(no_atual, extremos[0])
                    dist = grafo.obterDistanciaMinima(no_atual, extremos[0])
                    chegada = extremos[0]
                    outro_extremo = extremos[0]
                else:
                    caminho1 = grafo.obterCaminhoMinimo(no_atual, extremos[0])
                    dist1 = grafo.obterDistanciaMinima(no_atual, extremos[0])
                    caminho2 = grafo.obterCaminhoMinimo(no_atual, extremos[1])
                    dist2 = grafo.obterDistanciaMinima(no_atual, extremos[1])

                    if dist1 <= dist2:
                        caminho = caminho1
                        dist = dist1
                        chegada = extremos[0]
                        outro_extremo = extremos[1]
                    else:
                        caminho = caminho2
                        dist = dist2
                        chegada = extremos[1]
                        outro_extremo = extremos[0]

                demanda = info["demanda"]
                if carga + demanda > grafo.capacidade:
                    continue

                if dist < menor_custo:
                    melhor_servico = serv
                    melhor_caminho = caminho
                    menor_custo = dist
                    melhor_extremos = extremos

            if melhor_servico is None:
                break

            # Atualizar rota e custo com o caminho até o serviço
            if melhor_caminho and len(melhor_caminho) > 1:
                for i in range(1, len(melhor_caminho)):
                    custo += grafo.obterDistanciaMinima(melhor_caminho[i - 1], melhor_caminho[i])
                    rota.append(melhor_caminho[i])

            # Atualizar carga e custo com o serviço
            info = servico_info[melhor_servico]
            demanda = info["demanda"]
            custo += info["custo"]
            carga += demanda
            servicos_rota.append(melhor_servico)

            # Se for serviço do tipo "no", adiciona explicitamente à rota
            if melhor_servico[0] == "no":
                rota.append(info["extremos"][0])
                no_atual = info["extremos"][0]
            else:
                no_atual = outro_extremo

            # Registrar detalhes da visita
            id_servico = mapeamento_id[melhor_servico]
            if melhor_servico[0] == "no":
                visita = {
                    "servico": {
                        "tipo": "no",
                        "id": id_servico,
                        "origem": info["extremos"][0],
                        "destino": info["extremos"][0],
                    }
                }
            else:
                u, v = info["extremos"]
                if melhor_servico[0] == "arco":
                    origem, destino = u, v
                else:
                    origem, destino = min(u, v), max(u, v)

                visita = {
                    "servico": {
                        "tipo": melhor_servico[0],
                        "id": id_servico,
                        "origem": origem,
                        "destino": destino,
                    }
                }

            detalhes_visitas.append(visita)
            servicos_pendentes.remove(melhor_servico)

        # Voltar ao depósito
        if no_atual != deposito:
            caminho_volta = grafo.obterCaminhoMinimo(no_atual, deposito)
            if caminho_volta:
                for i in range(1, len(caminho_volta)):
                    custo += grafo.obterDistanciaMinima(caminho_volta[i - 1], caminho_volta[i])
                    rota.append(caminho_volta[i])
            no_atual = deposito

        # Adicionar visita ao depósito (D) no início e fim
        detalhes_visitas.insert(0, {"servico": {"tipo": "D"}})
        detalhes_visitas.append({"servico": {"tipo": "D"}})

        solucao.append({
            "rota": rota,
            "servicos_atendidos": servicos_rota,
            "demanda": carga,
            "custo": custo,
            "detalhes": detalhes_visitas,
        })

    return solucao
