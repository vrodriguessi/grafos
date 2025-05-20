def construir_mapeamento_servico_id(grafo):
    mapeamento = {}
    contador = 1

    # Otimização: Pré-processar nós obrigatórios
    for no_info in grafo.nos_obrigatorios:
        no = no_info['no']
        mapeamento[("no", no)] = contador
        contador += 1

    # Otimização: Evitar sorted repetido para arestas
    for u, v, _, _ in grafo.arestas_obrigatorias:
        chave = ("aresta", (u, v) if u < v else (v, u))
        if chave not in mapeamento:
            mapeamento[chave] = contador
            contador += 1

    # Otimização: Arcos já são únicos por definição
    for u, v, _, _ in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        mapeamento[chave] = contador
        contador += 1

    return mapeamento


def path_scanning(grafo):
    grafo.calcular_floyd_warshall()
    
    servicos_pendentes = set()
    servico_info = {}
    mapeamento_id = {}

    contador_id = 1
    
    for no_info in grafo.nos_obrigatorios:
        no = no_info['no']
        chave = ("no", no)
        servicos_pendentes.add(chave)
        servico_info[chave] = {
            "demanda": no_info.get("demanda", 1),
            "custo": no_info.get("custo", 0),
            "extremos": (no, no),
        }
        mapeamento_id[chave] = contador_id
        contador_id += 1

    for u, v, custo, demanda in grafo.arestas_obrigatorias:
        chave = ("aresta", (u, v) if u < v else (v, u))
        servicos_pendentes.add(chave)
        servico_info[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }
        mapeamento_id[chave] = contador_id
        contador_id += 1

    for u, v, custo, demanda in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        servicos_pendentes.add(chave)
        servico_info[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }
        mapeamento_id[chave] = contador_id
        contador_id += 1

    solucao = []
    deposito = 1
    capacidade_max = grafo.capacidade

    while servicos_pendentes:
        rota = [deposito]
        carga = 0
        custo = 0
        servicos_rota = []
        detalhes_visitas = [{"servico": {"tipo": "D"}}] 
        no_atual = deposito

        while True:
            melhor_servico = None
            menor_custo = float('inf')
            melhor_chegada = None
            melhor_outro_extremo = None

            for serv in servicos_pendentes:
                info = servico_info[serv]
                if carga + info["demanda"] > capacidade_max:
                    continue

                extremos = info["extremos"]
                
                if serv[0] == "no":
                    dist = grafo.obterDistanciaMinima(no_atual, extremos[0])
                    chegada = extremos[0]
                    outro_extremo = extremos[0]
                else:
                    dist1 = grafo.obterDistanciaMinima(no_atual, extremos[0])
                    dist2 = grafo.obterDistanciaMinima(no_atual, extremos[1])
                    
                    if dist1 <= dist2:
                        dist = dist1
                        chegada = extremos[0]
                        outro_extremo = extremos[1]
                    else:
                        dist = dist2
                        chegada = extremos[1]
                        outro_extremo = extremos[0]

                if dist < menor_custo:
                    melhor_servico = serv
                    menor_custo = dist
                    melhor_chegada = chegada
                    melhor_outro_extremo = outro_extremo

            if melhor_servico is None:
                break

            # Adicionar caminho até o serviço
            caminho = grafo.obterCaminhoMinimo(no_atual, melhor_chegada)
            if caminho and len(caminho) > 1:
                # Otimização: Calcular custo diretamente usando a distância já obtida
                custo += menor_custo
                rota.extend(caminho[1:])  # Evitar append em loop

            # Processar serviço
            info = servico_info[melhor_servico]
            custo += info["custo"]
            carga += info["demanda"]
            servicos_rota.append(melhor_servico)
            no_atual = melhor_outro_extremo

            # Registrar visita
            id_servico = mapeamento_id[melhor_servico]
            visita = {
                "servico": {
                    "tipo": melhor_servico[0],
                    "id": id_servico,
                    "origem": info["extremos"][0],
                    "destino": info["extremos"][1] if melhor_servico[0] != "no" else info["extremos"][0],
                }
            }
            detalhes_visitas.append(visita)
            servicos_pendentes.remove(melhor_servico)

        # Voltar ao depósito
        if no_atual != deposito:
            caminho_volta = grafo.obterCaminhoMinimo(no_atual, deposito)
            if caminho_volta:
                dist_volta = grafo.obterDistanciaMinima(no_atual, deposito)
                custo += dist_volta
                rota.extend(caminho_volta[1:])

        # Finalizar rota
        detalhes_visitas.append({"servico": {"tipo": "D"}})
        
        solucao.append({
            "rota": rota,
            "servicos_atendidos": servicos_rota,
            "demanda": carga,
            "custo": custo,
            "detalhes": detalhes_visitas,
        })

    return solucao