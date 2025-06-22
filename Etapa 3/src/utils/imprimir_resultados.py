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

            total_visitas = len(visitas)
            f.write(f"0 1 {idx_rota} {demanda} {custo} {total_visitas}")

            for visita in visitas:
                servico = visita["servico"]
                tipo = servico["tipo"]

                if tipo == "D":
                    f.write(f" (D 0,1,1)")
                elif tipo in ("aresta", "arco", "no"):
                    id_servico = servico["id"]
                    origem = servico["origem"]
                    destino = servico["destino"]
                    f.write(f" (S {id_servico},{origem},{destino})")

            f.write("\n")
