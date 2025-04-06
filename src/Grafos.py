class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices  # continua existindo
        self.num_nos_total = num_vertices  # novo atributo para armazenar a quantidade total de nós
        self.num_arestas = 0
        self.num_arcos = 0
        self.num_arestas_req = 0
        self.num_arcos_req = 0

        # Componentes do grafo
        self.EDGE = []     # Arestas não obrigatórias
        self.ReE = []      # Arestas obrigatórias
        self.ARC = []      # Arcos não obrigatórios
        self.ReA = []      # Arcos obrigatórios
        self.ReN = set()   # Nós obrigatórios (ReN)

        # Matriz de adjacência com custo
        self.adj_matrix = [
            [float('inf')] * num_vertices for _ in range(num_vertices)
        ]
        for i in range(num_vertices):
            self.adj_matrix[i][i] = 0

    def adicionar_aresta_nao_obrigatoria(self, u, v, custo, demanda):
        self.EDGE.append((u, v, custo, demanda))
        self.num_arestas += 1
        self.adj_matrix[u-1][v-1] = custo
        self.adj_matrix[v-1][u-1] = custo

    def adicionar_aresta_obrigatoria(self, u, v, custo, demanda):
        self.ReE.append((u, v, custo, demanda))
        self.num_arestas += 1
        self.num_arestas_req += 1
        self.adj_matrix[u-1][v-1] = custo
        self.adj_matrix[v-1][u-1] = custo
        # NÃO adiciona u, v no ReN aqui

    def adicionar_arco_nao_obrigatorio(self, u, v, custo, demanda):
        self.ARC.append((u, v, custo, demanda))
        self.num_arcos += 1
        self.adj_matrix[u-1][v-1] = custo

    def adicionar_arco_obrigatorio(self, u, v, custo, demanda):
        self.ReA.append((u, v, custo, demanda))
        self.num_arcos += 1
        self.num_arcos_req += 1
        self.adj_matrix[u-1][v-1] = custo
        # NÃO adiciona u, v no ReN aqui

    def adicionar_no_obrigatorio(self, no):
        self.ReN.add(no)
