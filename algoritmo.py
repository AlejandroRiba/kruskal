from Posicion import Posicion
import copy

class UnionFind:
    """Estructura de conjuntos disjuntos para Kruskal"""
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Kruskal(object):
    """Algoritmo de Kruskal desarrollado en Python"""
    
    def __init__(self, vector, c):
        """
        Constructor de la clase Kruskal.
        
        :param vector: Matriz de adyacencia que representa el grafo.
        :param c: Número de elementos que contiene el vector.
        """
        self.a = c
        self.vectorEntrada = copy.deepcopy(vector)
        self.vectorSalida = []
        self.rellenar(c)
        self.uf = UnionFind(c)

    def solucionar(self):
        """
        Método principal que resuelve el problema utilizando el algoritmo de Kruskal.
        """
        print("iniciar")
        i = 0
        for x in range(self.a):
            self.vectorEntrada[x][x] = 0
        
        while i < self.a - 1:
            b = self.menor()
            if b is not None:
                if self.uf.find(b.x) != self.uf.find(b.y):
                    self.uf.union(b.x, b.y)
                    self.vectorSalida[b.x][b.y] = self.vectorEntrada[b.x][b.y]
                    self.vectorSalida[b.y][b.x] = self.vectorEntrada[b.x][b.y]
                    i += 1
                self.vectorEntrada[b.x][b.y] = 0
                self.vectorEntrada[b.y][b.x] = 0

    def rellenar(self, b):
        """
        Método para rellenar el vector de salida con ceros.
        
        :param b: Tamaño de la matriz.
        """
        for x in range(b):
            aux = [0] * b
            self.vectorSalida.append(aux)

    def menor(self):
        """
        Método para encontrar la arista de menor peso.
        
        :return: Objeto Posicion con las coordenadas de la arista de menor peso.
        """
        m = float('inf')
        posiciones = None
        for x in range(self.a):
            for y in range(self.a):
                if self.vectorEntrada[x][y] != 0 and self.vectorEntrada[x][y] < m:
                    m = self.vectorEntrada[x][y]
                    posiciones = Posicion(x, y)
        return posiciones

