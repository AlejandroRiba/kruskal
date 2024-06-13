#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx  # importando la libreria Wxpython (Manejo de interfaz grafica)
from PosicionP import PosicionP  # Importando la clase PosicionP (Guarda posiciones X y Y)

class InterfazSalida(wx.Frame):  # iniciando la clase del formulario
    # constructor recibe como parámetros el título de la ventana, la cantidad de elementos y el vector resultante
    def __init__(self, parent, title, n, vectorMostrar,vectori):
        # calculamos el tamaño de la ventana
        self.zx = 200 + n * 100
        self.zy = 600 + n * 30
        self.n = n
        self.vector = vectorMostrar
        self.vectori = vectori
        # llamamos al constructor de la clase padre
        super(InterfazSalida, self).__init__(parent, title=title, size=(self.zx, self.zy))
        # creación de variables auxiliares para el manejo de los labels
        self.cajasDeTexto = []
        self.mensajex = []
        self.mensajey = []
        self.posix = 60
        self.posiy = 60
        self.caja = []
        for x in range(n):
            self.caja = []
            self.mensajex.append(wx.StaticText(self, id=-1, label="x:" + str(x + 1), pos=(self.posix + x * 75 + 30, 40)))
            for y in range(n):
                self.mensajey.append(wx.StaticText(self, id=-1, label="y: " + str(y + 1), pos=(35, self.posiy + y * 20 + 5)))
                self.caja.append(wx.StaticText(self, id=-1, label=str(vectori[x][y]), pos=(self.posix + x * 75, self.posiy + y * 20)))
            self.cajasDeTexto.append(self.caja)
        self.caja = wx.StaticText(self, id=-1, label="Algoritmo de Kruskal", pos=(self.zx / 2, 20))
        self.caja0 = wx.StaticText(self, id=-1, label="Grafica del algoritmo de Kruskal", pos=(self.zx / 4, self.zy - 500))
        peso_int = self.calcularPeso()
        peso = "El peso del grafo es de: " + str(peso_int)
        self.caja1 = wx.StaticText(self, id=-1, label=peso, pos=(self.zx / 4, self.posiy + n * 21))
        # Dibujar Círculos
        self.Bind(wx.EVT_PAINT, self.pintar)  # evento para dibujar
        self.Move((800, 250))  # posición de la ventana en el escritorio
        self.Show()  # mostrar la ventana

    # función para calcular peso
    def calcularPeso(self):
        r = 0  # peso o costo
        for x in range(self.n):
            for y in range(self.n):
                if self.vector[x][y] != 0 and x < y:
                    r += int(self.vector[x][y])
        return r

    # dibujando los grafos
    def pintar(self, event):
        aux = []
        dc = wx.PaintDC(self)
        dc.Clear()
        for x in range(self.n):
            if x == 0:
                px = 55
                py = self.zy - 300
            elif x == 7:
                px = 400
                py = self.zy - 300
            elif x == 1:
                px = 55 + (80 * x) + (10 * x)
                py = self.zy - 350
            elif x % 2 == 0:
                px = 55 + (40 * x) + (10 * x)
                py = self.zy - 250
            else:
                px = 55 + (40 * x) + (20 * x)
                py = self.zy - 350
            dc.DrawCircle(px, py, 30)
            dc.DrawText(str(x+1), px + 5, py - 10)
            aux.append(PosicionP(x, px, py))

        pen = wx.Pen("BLUE", 3, wx.SOLID)
        pen1 = wx.Pen("BLACK",1,wx.SOLID)
        for x in range(self.n):
            for y in range(self.n):
                if self.vector[x][y] != 0 and x < y:
                    x1, y1, x2, y2 = None, None, None, None
                    for z in aux:
                        if z.n == x:
                            x1 = z.x
                            y1 = z.y
                        if z.n == y:
                            x2 = z.x
                            y2 = z.y
                    dc.SetPen(pen)
                    dc.DrawLine(x1 + 27, y1 + 15, x2 - 30, y2)
                    # dibujo de texto
                    dc.DrawText(str(self.vector[x][y]), int(x1 + ((x2 - x1) / 2) + 5), int(y1 + ((y2 - y1) / 2)))
                elif self.vectori[x][y] != 0 and x < y:
                    x1, y1, x2, y2 = None, None, None, None
                    for z in aux:
                        if z.n == x:
                            x1 = z.x
                            y1 = z.y
                        if z.n == y:
                            x2 = z.x
                            y2 = z.y
                    dc.SetPen(pen1)  # Utilizar pen1 para dibujar la línea
                    dc.DrawLine(x1 + 27, y1 + 15, x2 - 30, y2)
                    # dibujo de texto
                    dc.DrawText(str(self.vectori[x][y]), int(x1 + ((x2 - x1) / 2) + 5), int(y1 + ((y2 - y1) / 2)))

if __name__ == '__main__':
    app = wx.App()
    InterfazSalida(None, title='Algoritmo de Kruskal (Salida)', n=5, vectorMostrar=[[0, 2, 0, 6, 0], [2, 0, 3, 8, 5], [0, 3, 0, 0, 7], [6, 8, 0, 0, 9], [0, 5, 7, 9, 0]])
    app.MainLoop()
