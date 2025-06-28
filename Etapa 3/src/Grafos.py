from src.algorithms.floyd_warshall import floyd_warshall

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_arestas = 0
        self.num_arcos = 0
        self.num_arestas_req = 0
        self.num_arcos_req = 0
        self.capacidade = 0
        self.depotNode = None

        self.arestas_nao_obrigatorias = []  # Arestas não obrigatórias
        self.arestas_obrigatorias = []    # Arestas obrigatórias
        self.arcos_nao_obrigatorios = []      # Arcos não obrigatórios
        self.arcos_obrigatorios = []        # Arcos obrigatórios
        self.nos_obrigatorios = []      # Nós obrigatórios (ReN)

        self.adj_matrix = [
            [float('inf')] * num_vertices for _ in range(num_vertices)
        ]
        for i in range(num_vertices):
            self.adj_matrix[i][i] = 0

        self.distancias_minimas = None
        self.predecessores = None

    def adicionar_aresta_nao_obrigatoria(self, u, v, custo, demanda):
        self.arestas_nao_obrigatorias.append((u, v, custo, demanda))
        self.num_arestas += 1
        self.adj_matrix[u-1][v-1] = custo
        self.adj_matrix[v-1][u-1] = custo

    def adicionar_aresta_obrigatoria(self, u, v, custo, demanda):
        self.arestas_obrigatorias.append((u, v, custo, demanda))
        self.num_arestas += 1
        self.num_arestas_req += 1
        self.adj_matrix[u-1][v-1] = custo
        self.adj_matrix[v-1][u-1] = custo

    def adicionar_arco_nao_obrigatorio(self, u, v, custo, demanda):
        self.arcos_nao_obrigatorios.append((u, v, custo, demanda))
        self.num_arcos += 1
        self.adj_matrix[u-1][v-1] = custo

    def adicionar_arco_obrigatorio(self, u, v, custo, demanda):
        self.arcos_obrigatorios.append((u, v, custo, demanda))
        self.num_arcos += 1
        self.num_arcos_req += 1
        self.adj_matrix[u-1][v-1] = custo

    def adicionar_no_obrigatorio(self, no, demanda=0, custo=0):
        self.nos_obrigatorios.append({'no': no, 'demanda': demanda, 'custo': custo})

    def calcular_floyd_warshall(self):
        self.distancias_minimas, self.predecessores = floyd_warshall(self)

    def obterDistanciaMinima(self, origem, destino):
        if self.distancias_minimas is None:
            self.calcular_floyd_warshall()
        return self.distancias_minimas[origem-1][destino-1]

    def obterCaminhoMinimo(self, origem, destino):
        if self.predecessores is None:
            self.calcular_floyd_warshall()

        u = origem - 1
        v = destino - 1

        if self.predecessores[u][v] is None:
            return []  # Sem caminho

        caminho = []
        while v != u:
            caminho.insert(0, v + 1)
            v = self.predecessores[u][v] - 1
        caminho.insert(0, origem)

        return caminho

    def caminho_minimo(self, origem, destino):
        return self.obterCaminhoMinimo(origem, destino)
