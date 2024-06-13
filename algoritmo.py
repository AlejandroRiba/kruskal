from Posicion import Posicion
import copy

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

    def solucionar(self):
        """
        Método principal que resuelve el problema utilizando el algoritmo de Kruskal.
        """
        ##print("iniciar")
        i = 0
        for x in range(self.a):
            self.vectorEntrada[x][x] = 0
        
        while i < self.a - 1:
            b = self.menor()
            if b is not None:
                self.t = self.buscar(b.y)
                if self.t:
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
        m = 0
        posiciones = None
        for x in range(self.a):
            for y in range(self.a):
                ##print(f"{x} {y}: {self.vectorEntrada[x][y]}")
                if m == 0 and self.vectorEntrada[x][y] != 0:
                    m = self.vectorEntrada[x][y]
                    posiciones = Posicion(x, y)
                elif self.vectorEntrada[x][y] != 0 and self.vectorEntrada[x][y] < m:
                    m = self.vectorEntrada[x][y]
                    posiciones = Posicion(x, y)
        return posiciones

    def buscar(self, z):
        """
        Método para verificar si un nodo ya está en el conjunto solución.
        
        :param z: Nodo a buscar.
        :return: True si el nodo no está en el conjunto solución, False en caso contrario.
        """
        for x in range(self.a):
            if self.vectorSalida[x][z] != 0:
                return False
        return True
