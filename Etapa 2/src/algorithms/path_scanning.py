def atribuirIdServicos(grafo):
    mapeamento = {}
    contador = 1

    for InfoNo in grafo.nos_obrigatorios:
        no = InfoNo['no']
        mapeamento[("no", no)] = contador
        contador += 1

    for u, v, _, _ in grafo.arestas_obrigatorias:
        chave = ("aresta", (u, v) if u < v else (v, u))
        if chave not in mapeamento:
            mapeamento[chave] = contador
            contador += 1

    for u, v, _, _ in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        mapeamento[chave] = contador
        contador += 1

    return mapeamento


def path_scanning(grafo):
    grafo.calcular_floyd_warshall()
    
    tarefas = set()
    dadosTarefas = {}
    idsServicos = {}

    contadorId = 1
    
    for InfoNo in grafo.nos_obrigatorios:
        no = InfoNo['no']
        chave = ("no", no)
        tarefas.add(chave)
        dadosTarefas[chave] = {
            "demanda": InfoNo.get("demanda", 1),
            "custo": InfoNo.get("custo", 0),
            "extremos": (no, no),
        }
        idsServicos[chave] = contadorId
        contadorId += 1

    for u, v, custo, demanda in grafo.arestas_obrigatorias:
        chave = ("aresta", (u, v) if u < v else (v, u))
        tarefas.add(chave)
        dadosTarefas[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }
        idsServicos[chave] = contadorId
        contadorId += 1

    for u, v, custo, demanda in grafo.arcos_obrigatorios:
        chave = ("arco", (u, v))
        tarefas.add(chave)
        dadosTarefas[chave] = {
            "demanda": demanda,
            "custo": custo,
            "extremos": (u, v),
        }
        idsServicos[chave] = contadorId
        contadorId += 1

    solucao = []
    deposito = 1
    capacidadeMax = grafo.capacidade

    while tarefas:
        rota = [deposito]
        carga = 0
        custo = 0
        servicos_rota = []
        resgistroVisitas = [{"servico": {"tipo": "D"}}] 
        noAtual = deposito

        while True:
            melhorOpcao = None
            menorCusto = float('inf')
            melhorDestino = None
            melhorExtremo = None

            for serv in tarefas:
                info = dadosTarefas[serv]
                if carga + info["demanda"] > capacidadeMax:
                    continue

                extremos = info["extremos"]
                
                if serv[0] == "no":
                    dist = grafo.obterDistanciaMinima(noAtual, extremos[0])
                    chegada = extremos[0]
                    outroExtremo = extremos[0]
                else:
                    dist1 = grafo.obterDistanciaMinima(noAtual, extremos[0])
                    dist2 = grafo.obterDistanciaMinima(noAtual, extremos[1])
                    
                    if dist1 <= dist2:
                        dist = dist1
                        chegada = extremos[0]
                        outroExtremo = extremos[1]
                    else:
                        dist = dist2
                        chegada = extremos[1]
                        outroExtremo = extremos[0]

                if dist < menorCusto:
                    melhorOpcao = serv
                    menorCusto = dist
                    melhorDestino = chegada
                    melhorExtremo = outroExtremo

            if melhorOpcao is None:
                break

            caminho = grafo.obterCaminhoMinimo(noAtual, melhorDestino)
            if caminho and len(caminho) > 1:
                custo += menorCusto
                rota.extend(caminho[1:]) 

            info = dadosTarefas[melhorOpcao]
            custo += info["custo"]
            carga += info["demanda"]
            servicos_rota.append(melhorOpcao)
            noAtual = melhorExtremo

            id_servico = idsServicos[melhorOpcao]
            visita = {
                "servico": {
                    "tipo": melhorOpcao[0],
                    "id": id_servico,
                    "origem": info["extremos"][0],
                    "destino": info["extremos"][1] if melhorOpcao[0] != "no" else info["extremos"][0],
                }
            }
            resgistroVisitas.append(visita)
            tarefas.remove(melhorOpcao)

        if noAtual != deposito:
            caminhoVolta = grafo.obterCaminhoMinimo(noAtual, deposito)
            if caminhoVolta:
                dist_volta = grafo.obterDistanciaMinima(noAtual, deposito)
                custo += dist_volta
                rota.extend(caminhoVolta[1:])

        resgistroVisitas.append({"servico": {"tipo": "D"}})
        
        solucao.append({
            "rota": rota,
            "servicos_atendidos": servicos_rota,
            "demanda": carga,
            "custo": custo,
            "detalhes": resgistroVisitas,
        })

    return solucao