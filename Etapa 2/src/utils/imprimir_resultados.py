def salvar_resultado_path_scanning(solucao, tempo_total, tempo_encontrar_solucao, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        custo_total = sum(rota["custo"] for rota in solucao)
        total_rotas = len(solucao)
        f.write(f"{custo_total}\n")
        f.write(f"{total_rotas}\n")
        f.write(f"{tempo_total}\n")
        f.write(f"{tempo_encontrar_solucao}\n")

        for idx_rota, rota in enumerate(solucao, start=1):
            demanda = rota["demanda"]
            custo = rota["custo"]
            visitas = rota["detalhes"]

            # total de visitas = depósito (1 a mais) + serviços (n)
            total_visitas = 1 + len(visitas)

            # índice do depósito sempre 0, dia 1, identificador da rota começa em 1
            f.write(f"0 1 {idx_rota} {demanda} {custo} {total_visitas}")

            # imprime a visita ao depósito inicial
            f.write(" (D 0,1,1)")

            # agora imprime as visitas aos serviços
            for visita in visitas:
                serv = visita["servico"]
                tipo = serv["tipo"]

                if tipo == "aresta" or tipo == "arco":
                    # (S id_serviço, extremidade1, extremidade2)
                    # Presumo que id_serviço seja algum identificador, 
                    # se você tiver algum id do serviço, use ele. Se não, pode usar a posição na lista.
                    # Como não tem id explícito, pode usar o índice na lista + 1 como id.
                    id_servico = solucao.index(rota) + 1  # ou outro id que você tenha
                    # Melhor pegar a posição da visita dentro da rota:
                    id_servico = visitas.index(visita) + 1
                    f.write(f" (S {id_servico},{serv['origem']},{serv['destino']})")

            f.write("\n")
