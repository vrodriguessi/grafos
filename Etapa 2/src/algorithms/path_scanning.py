from copy import deepcopy
from src.algorithms.floyd_warshall import floyd_warshall

def path_scanning(grafo, deposito=1):
    dist, _ = floyd_warshall(grafo)
    capacidade_veiculo = grafo.capacidade

    servicos_pendentes = []
    id_global = 1
    for u, v, custo, demanda in grafo.ReE:
        servicos_pendentes.append({
            "id": id_global,
            "tipo": "aresta",
            "origem": u,
            "destino": v,
            "custo": custo,
            "demanda": demanda,
            "atendido": False
        })
        id_global += 1
    for u, v, custo, demanda in grafo.ReA:
        servicos_pendentes.append({
            "id": id_global,
            "tipo": "arco",
            "origem": u,
            "destino": v,
            "custo": custo,
            "demanda": demanda,
            "atendido": False
        })
        id_global += 1

    solucao = []

    while any(not s["atendido"] for s in servicos_pendentes):
        rota = [deposito]
        carga = 0
        custo = 0
        servicos_rota = []
        detalhes_visitas = []

        no_atual = deposito

        # Adiciona visita ao depósito (início)
        detalhes_visitas.append({
            "servico": {
                "tipo": "D",
                "origem": deposito,
                "destino": deposito,
                "custo": 0,
                "demanda": 0
            },
            "custo_ate_servico": 0,
            "custo_servico": 0,
            "carga_atual": carga
        })

        while True:
            # Filtra serviços viáveis com base na capacidade restante
            candidatos = [
                s for s in servicos_pendentes 
                if not s["atendido"] and s["demanda"] + carga <= capacidade_veiculo
            ]

            if not candidatos:
                break  # Nenhum serviço viável, encerra a rota

            # Escolhe o serviço mais próximo
            candidatos.sort(key=lambda s: dist[no_atual - 1][s["origem"] - 1])
            proximo = candidatos[0]

            custo_ate_servico = dist[no_atual - 1][proximo["origem"] - 1]
            custo_servico = proximo["custo"]
            custo += custo_ate_servico + custo_servico

            rota.append(proximo["origem"])
            rota.append(proximo["destino"])
            carga += proximo["demanda"]
            servicos_rota.append(proximo)
            detalhes_visitas.append({
                "servico": deepcopy(proximo),
                "custo_ate_servico": custo_ate_servico,
                "custo_servico": custo_servico,
                "carga_atual": carga
            })

            proximo["atendido"] = True
            no_atual = proximo["destino"]

            # Se a carga está no limite, termina a rota aqui
            if carga == capacidade_veiculo:
                break

        # Volta ao depósito
        custo_retorno = dist[no_atual - 1][deposito - 1]
        custo += custo_retorno
        rota.append(deposito)

        detalhes_visitas.append({
            "servico": {
                "tipo": "D",
                "origem": deposito,
                "destino": deposito,
                "custo": 0,
                "demanda": 0
            },
            "custo_ate_servico": custo_retorno,
            "custo_servico": 0,
            "carga_atual": carga
        })

        solucao.append({
            "rota": rota,
            "servicos_atendidos": servicos_rota,
            "demanda": carga,
            "custo": custo,
            "detalhes": detalhes_visitas,
        })

    return solucao
