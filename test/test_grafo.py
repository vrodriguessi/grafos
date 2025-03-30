import unittest
from src.models.grafos import Grafo

class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.vertices = {1, 2, 3, 4}
        self.arestas = [(1, 2, 10, 5), (2, 3, 15, 7)]
        self.arcos = [(3, 4, 20, 3)]
        self.VR = {1, 2, 3, 4}
        self.ER = [(1, 2), (2, 3)]
        self.AR = [(3, 4)]
        self.grafo = Grafo(self.vertices, self.arestas, self.arcos, self.VR, self.ER, self.AR)

    def test_qtd_vertices(self):
        self.assertEqual(self.grafo.qtd_vertices(), 4)

    def test_qtd_arestas(self):
        self.assertEqual(self.grafo.qtd_arestas(), 2)

    def test_qtd_arcos(self):
        self.assertEqual(self.grafo.qtd_arcos(), 1)

if __name__ == "__main__":
    unittest.main()
