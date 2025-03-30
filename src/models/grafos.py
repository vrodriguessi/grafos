class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        self.arcos = {}

    def adicionar_vertice(self, v):
        self.vertices.add(v)

    def adicionar_aresta(self, u, v, custo, demanda):
        self.arestas[(u, v)] = {"custo": custo, "demanda": demanda}
        self.arestas[(v, u)] = {"custo": custo, "demanda": demanda} 

    def adicionar_arco(self, u, v, custo, demanda):
        self.arcos[(u, v)] = {"custo": custo, "demanda": demanda} 

    def obter_vizinhos(self, v):
        vizinhos = set()
        for (u, w) in self.arestas.keys():
            if u == v:
                vizinhos.add(w)
            elif w == v:
                vizinhos.add(u)
        return vizinhos
