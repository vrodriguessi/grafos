from copy import deepcopy
from src.algorithms.floyd_warshall import floyd_warshall

def path_scanning(grafo, capacidade_veiculo, deposito=1):
    dist, _ = floyd_warshall(grafo) 

    servicos_pendentes = []
    for u, v, custo, demanda in grafo.ReE: 
        servicos_pendentes.append({
            "tipo": "aresta",
            "origem": u,
            "destino": v,
            "custo": custo,
            "demanda": demanda,
            "atendido": False
        })
    for u, v, custo, demanda in grafo.ReA:
        servicos_pendentes.append({
            "tipo": "arco",
            "origem": u,
            "destino": v,
            "custo": custo,
            "demanda": demanda,
            "atendido": False
        })

    solucao = []

    while any(not s["atendido"] for s in servicos_pendentes):
        rota = [deposito] 
        carga = 0
        custo = 0
        servicos_rota = []
        detalhes_visitas = []

        no_atual = deposito

        while True:
            candidatos = [s for s in servicos_pendentes if not s["atendido"] and s["demanda"] + carga <= capacidade_veiculo]
            if not candidatos:
                break

            candidatos.sort(key=lambda s: dist[no_atual-1][s["origem"]-1])
            proximo = candidatos[0]

            custo_ate_servico = dist[no_atual-1][proximo["origem"]-1]
            custo_servico = proximo["custo"]
            custo += custo_ate_servico + custo_servico

            rota.append(proximo["origem"])
            rota.append(proximo["destino"]) 
            carga += proximo["demanda"]
            servicos_rota.append(proximo)
            detalhes_visitas.append({
                "servico": proximo,
                "custo_ate_servico": custo_ate_servico,
                "custo_servico": custo_servico,
                "carga_atual": carga
            })

            no_atual = proximo["destino"]
            proximo["atendido"] = True

        custo += dist[no_atual-1][deposito-1]
        rota.append(deposito)

        solucao.append({
            "rota": rota,
            "servicos_atendidos": servicos_rota,
            "demanda": carga,
            "custo": custo,
            "detalhes": detalhes_visitas,
        })

    return solucao
